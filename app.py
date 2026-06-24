import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename

from config import Config
from database import get_db_connection, init_db
from nlp_processor import (
    extract_text_from_pdf, calculate_ats_and_skill_gap, JOB_ROLES, 
    calculate_interview_readiness, recommend_job_roles, extract_skills,
    generate_hr_questions, evaluate_mock_response, predict_salary_lpa, get_chat_assistant_response
)
from ml_predictor import predict_placement
from roadmap_generator import generate_personalized_roadmap, get_cert_recommendations_with_links, get_detailed_project_recommendations

app = Flask(__name__)
app.config.from_object(Config)

# Ensure upload and chart directories exist
try:
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
except Exception as e:
    print(f"Could not create upload directory: {e}")

try:
    os.makedirs(os.path.join(app.root_path, 'static', 'css'), exist_ok=True)
    os.makedirs(os.path.join(app.root_path, 'static', 'js'), exist_ok=True)
    os.makedirs(os.path.join(app.root_path, 'static', 'charts'), exist_ok=True)
except Exception as e:
    print(f"Could not create static subdirectories (might be read-only): {e}")

# Initialize database tables on startup/import
try:
    init_db()
except Exception as e:
    print(f"Database initialization failed: {e}")

def get_row_as_dict(row):
    """Convert SQLite Row or MySQL Dict row into standard Python dict."""
    if row is None:
        return None
    # If SQLite Row
    if hasattr(row, 'keys'):
        return dict(row)
    # MySQL dictionary cursor already returns dict
    return row

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'

@app.route('/')
def index():
    # Provide list of available roles for the select dropdown
    roles = sorted(list(JOB_ROLES.keys()))
    return render_template('index.html', roles=roles)

@app.route('/analyze', methods=['POST'])
def analyze():
    # 1. Validation
    if 'resume' not in request.files:
        flash("No file part found in request.")
        return redirect(url_for('index'))
        
    file = request.files['resume']
    target_role = request.form.get('target_role')
    
    # Handle user custom target role if selected "Other"
    custom_role = request.form.get('custom_role')
    custom_skills = request.form.get('custom_skills')
    
    if target_role == "Other" and custom_role:
        target_role = custom_role.strip()
        # Register custom role skills dynamically
        if custom_skills:
            from nlp_processor import JOB_ROLES, ALL_SKILLS
            skills_list = [s.strip().lower() for s in custom_skills.split(',') if s.strip()]
            JOB_ROLES[target_role] = skills_list
            for s in skills_list:
                ALL_SKILLS.add(s)
    
    if file.filename == '':
        flash("No selected file.")
        return redirect(url_for('index'))
        
    if not target_role:
        flash("Please select a target job role.")
        return redirect(url_for('index'))
        
    if file and allowed_file(file.filename):
        # Save file securely
        filename = secure_filename(file.filename)
        # Add uniqueness to filename using timestamp or basic prefix
        import time
        unique_filename = f"{int(time.time())}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        
        # 2. Extract and parse resume content
        try:
            text = extract_text_from_pdf(filepath)
            if not text.strip():
                flash("Could not extract text from the PDF. It might be scanned or corrupted.")
                return redirect(url_for('index'))
                
            # Perform NLP calculations
            analysis = calculate_ats_and_skill_gap(text, target_role)
            
            # Perform ML placement predictions
            # Extract inputs
            cgpa = parse_cgpa_helper(text)
            projects = analysis["metrics"]["projects_count"]
            certifications = analysis["metrics"]["certifications_count"]
            internships = analysis["metrics"]["internships_count"]
            ats_score = analysis["ats_score"]
            skill_match = analysis["skill_match_percentage"]
            
            prediction = predict_placement(cgpa, projects, certifications, internships, ats_score, skill_match)
            
            # Generate Roadmap
            roadmap = generate_personalized_roadmap(target_role, analysis["missing_skills"])
            
            # Additional analyses
            extracted_skills = extract_skills(text)
            interview_readiness = calculate_interview_readiness(text, analysis)
            role_recommendations = recommend_job_roles(extracted_skills, target_role)
            project_recommendations = get_detailed_project_recommendations(target_role)
            cert_recommendations = get_cert_recommendations_with_links(target_role, analysis["missing_skills"])
            
            # Predict Salary Package
            salary_prediction = predict_salary_lpa(target_role, analysis["metrics"], skill_match)
            
            # Industry Benchmarking definitions
            role_benchmarks = {
                "AI Engineer": {"cgpa": 8.5, "projects_count": 3, "certifications_count": 2, "internships_count": 1, "ats_score": 78.0, "skill_match_percentage": 75.0},
                "Data Scientist": {"cgpa": 8.3, "projects_count": 3, "certifications_count": 2, "internships_count": 1, "ats_score": 76.0, "skill_match_percentage": 72.0},
                "Software Developer": {"cgpa": 7.8, "projects_count": 3, "certifications_count": 1, "internships_count": 1, "ats_score": 72.0, "skill_match_percentage": 68.0},
                "Full Stack Developer": {"cgpa": 7.9, "projects_count": 4, "certifications_count": 1, "internships_count": 1, "ats_score": 74.0, "skill_match_percentage": 70.0}
            }
            benchmarks = role_benchmarks.get(target_role, {"cgpa": 8.0, "projects_count": 3, "certifications_count": 1, "internships_count": 1, "ats_score": 74.0, "skill_match_percentage": 70.0})
            
            # Generate HR Questions
            hr_questions = generate_hr_questions(target_role)
            
            # Combine analysis, prediction, and roadmap into a single dictionary
            full_analysis_data = {
                "candidate_name": analysis["candidate_name"],
                "email": analysis["email"],
                "phone": analysis["phone"],
                "target_role": target_role,
                "ats_score": ats_score,
                "skill_match_percentage": skill_match,
                "matched_skills": analysis["matched_skills"],
                "missing_skills": analysis["missing_skills"],
                "suggestions": analysis["suggestions"],
                "strengths": analysis["strengths"],
                "weaknesses": analysis["weaknesses"],
                "missing_keywords": analysis["missing_keywords"],
                "metrics": {
                    "cgpa": cgpa,
                    "projects_count": projects,
                    "certifications_count": certifications,
                    "internships_count": internships,
                    "experience_years": analysis["metrics"]["experience_years"]
                },
                "placement_prediction": prediction,
                "interview_readiness": interview_readiness,
                "role_recommendations": role_recommendations,
                "project_recommendations": project_recommendations,
                "cert_recommendations": cert_recommendations,
                "salary_prediction": salary_prediction,
                "benchmarks": benchmarks,
                "hr_questions": hr_questions,
                "roadmap": roadmap
            }
            
            # 3. Store in Database
            conn = get_db_connection()
            if Config.USE_MYSQL:
                cursor = conn.cursor(dictionary=True)
                query = """
                    INSERT INTO resumes (filename, candidate_name, email, target_role, cgpa, ats_score, skill_match, placement_prob, analysis_data)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (
                    unique_filename,
                    full_analysis_data["candidate_name"],
                    full_analysis_data["email"],
                    target_role,
                    cgpa,
                    ats_score,
                    skill_match,
                    prediction["placement_probability"],
                    json.dumps(full_analysis_data)
                ))
            else:
                cursor = conn.cursor()
                query = """
                    INSERT INTO resumes (filename, candidate_name, email, target_role, cgpa, ats_score, skill_match, placement_prob, analysis_data)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
                cursor.execute(query, (
                    unique_filename,
                    full_analysis_data["candidate_name"],
                    full_analysis_data["email"],
                    target_role,
                    cgpa,
                    ats_score,
                    skill_match,
                    prediction["placement_probability"],
                    json.dumps(full_analysis_data)
                ))
                
            conn.commit()
            resume_id = cursor.lastrowid
            cursor.close()
            conn.close()
            
            return redirect(url_for('dashboard', resume_id=resume_id))
            
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            flash(f"An error occurred during resume processing: {str(e)}")
            return redirect(url_for('index'))
    else:
        flash("Invalid file format. Please upload a PDF resume.")
        return redirect(url_for('index'))

def parse_cgpa_helper(text):
    # Retrieve CGPA using nlp_processor logic
    from nlp_processor import parse_cgpa
    return parse_cgpa(text)

@app.route('/dashboard/<int:resume_id>')
def dashboard(resume_id):
    conn = get_db_connection()
    if Config.USE_MYSQL:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM resumes WHERE id = %s", (resume_id,))
    else:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM resumes WHERE id = ?", (resume_id,))
        
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if not row:
        flash("Resume analysis record not found.")
        return redirect(url_for('index'))
        
    resume_data = get_row_as_dict(row)
    analysis_details = json.loads(resume_data["analysis_data"])
    
    return render_template('dashboard.html', resume_id=resume_id, analysis=analysis_details)

@app.route('/roadmap/<int:resume_id>')
def roadmap(resume_id):
    conn = get_db_connection()
    if Config.USE_MYSQL:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM resumes WHERE id = %s", (resume_id,))
    else:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM resumes WHERE id = ?", (resume_id,))
        
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if not row:
        flash("Resume record not found.")
        return redirect(url_for('index'))
        
    resume_data = get_row_as_dict(row)
    analysis_details = json.loads(resume_data["analysis_data"])
    roadmap_details = analysis_details.get("roadmap", {})
    
    return render_template('roadmap.html', resume_id=resume_id, roadmap=roadmap_details, name=resume_data["candidate_name"], analysis=analysis_details)

@app.route('/compare', methods=['POST'])
def compare():
    if 'resume_a' not in request.files or 'resume_b' not in request.files:
        flash("Please upload both resumes to compare.")
        return redirect(url_for('index'))
        
    file_a = request.files['resume_a']
    file_b = request.files['resume_b']
    target_role = request.form.get('target_role')
    
    if file_a.filename == '' or file_b.filename == '':
        flash("Both resume files must be selected.")
        return redirect(url_for('index'))
        
    if not target_role:
        flash("Please select a target job role.")
        return redirect(url_for('index'))
        
    if file_a and allowed_file(file_a.filename) and file_b and allowed_file(file_b.filename):
        import time
        filename_a = f"{int(time.time())}_A_{secure_filename(file_a.filename)}"
        filename_b = f"{int(time.time())}_B_{secure_filename(file_b.filename)}"
        
        path_a = os.path.join(app.config['UPLOAD_FOLDER'], filename_a)
        path_b = os.path.join(app.config['UPLOAD_FOLDER'], filename_b)
        
        file_a.save(path_a)
        file_b.save(path_b)
        
        try:
            # Process Resume A
            text_a = extract_text_from_pdf(path_a)
            analysis_a = calculate_ats_and_skill_gap(text_a, target_role)
            cgpa_a = parse_cgpa_helper(text_a)
            pred_a = predict_placement(cgpa_a, analysis_a["metrics"]["projects_count"], analysis_a["metrics"]["certifications_count"], analysis_a["metrics"]["internships_count"], analysis_a["ats_score"], analysis_a["skill_match_percentage"])
            readiness_a = calculate_interview_readiness(text_a, analysis_a)
            
            # Process Resume B
            text_b = extract_text_from_pdf(path_b)
            analysis_b = calculate_ats_and_skill_gap(text_b, target_role)
            cgpa_b = parse_cgpa_helper(text_b)
            pred_b = predict_placement(cgpa_b, analysis_b["metrics"]["projects_count"], analysis_b["metrics"]["certifications_count"], analysis_b["metrics"]["internships_count"], analysis_b["ats_score"], analysis_b["skill_match_percentage"])
            readiness_b = calculate_interview_readiness(text_b, analysis_b)
            
            # Form comparison structures
            comp_a = {
                "name": analysis_a["candidate_name"],
                "email": analysis_a["email"],
                "ats_score": analysis_a["ats_score"],
                "skill_match": analysis_a["skill_match_percentage"],
                "placement_prob": pred_a["placement_probability"],
                "interview_readiness": readiness_a["score"],
                "projects": analysis_a["metrics"]["projects_count"],
                "certifications": analysis_a["metrics"]["certifications_count"],
                "internships": analysis_a["metrics"]["internships_count"],
                "experience": analysis_a["metrics"]["experience_years"],
                "cgpa": cgpa_a,
                "skills": analysis_a["matched_skills"],
                "missing_skills": analysis_a["missing_skills"]
            }
            
            comp_b = {
                "name": analysis_b["candidate_name"],
                "email": analysis_b["email"],
                "ats_score": analysis_b["ats_score"],
                "skill_match": analysis_b["skill_match_percentage"],
                "placement_prob": pred_b["placement_probability"],
                "interview_readiness": readiness_b["score"],
                "projects": analysis_b["metrics"]["projects_count"],
                "certifications": analysis_b["metrics"]["certifications_count"],
                "internships": analysis_b["metrics"]["internships_count"],
                "experience": analysis_b["metrics"]["experience_years"],
                "cgpa": cgpa_b,
                "skills": analysis_b["matched_skills"],
                "missing_skills": analysis_b["missing_skills"]
            }
            
            # Compare head to head and decide winner
            a_wins = 0
            b_wins = 0
            
            categories = ["ats_score", "skill_match", "placement_prob", "interview_readiness", "projects", "certifications", "internships", "cgpa"]
            category_winners = {}
            for cat in categories:
                if comp_a[cat] > comp_b[cat]:
                    category_winners[cat] = "A"
                    a_wins += 1
                elif comp_b[cat] > comp_a[cat]:
                    category_winners[cat] = "B"
                    b_wins += 1
                else:
                    category_winners[cat] = "Tie"
                    
            if a_wins > b_wins:
                winner = comp_a["name"]
                verdict = f"{comp_a['name']} presents a stronger overall profile for the {target_role} role. They lead in {a_wins} out of {len(categories)} evaluation metrics, including higher {', '.join([c.replace('_', ' ') for c, w in category_winners.items() if w == 'A'][:3])}."
            elif b_wins > a_wins:
                winner = comp_b["name"]
                verdict = f"{comp_b['name']} presents a stronger overall profile for the {target_role} role. They lead in {b_wins} out of {len(categories)} evaluation metrics, including higher {', '.join([c.replace('_', ' ') for c, w in category_winners.items() if w == 'B'][:3])}."
            else:
                # If tied wins, compare placement probability first
                if comp_a["placement_prob"] > comp_b["placement_prob"]:
                    winner = comp_a["name"]
                    verdict = f"{comp_a['name']} is slightly preferred due to higher placement probability score, despite tied metric wins."
                elif comp_b["placement_prob"] > comp_a["placement_prob"]:
                    winner = comp_b["name"]
                    verdict = f"{comp_b['name']} is slightly preferred due to higher placement probability score, despite tied metric wins."
                else:
                    winner = "Tie"
                    verdict = "Both candidates present highly comparable profiles with matching metrics. Selection should be based on cultural fit and coding test performance."
                    
            comparison_report = {
                "role": target_role,
                "candidate_a": comp_a,
                "candidate_b": comp_b,
                "winners": category_winners,
                "winner_name": winner,
                "verdict": verdict,
                "improvement_suggestions_a": analysis_a["suggestions"],
                "improvement_suggestions_b": analysis_b["suggestions"]
            }
            
            # Generate static Matplotlib chart for head-to-head comparison
            chart_filename = f"comp_chart_{int(time.time())}.png"
            generate_matplotlib_comparison_chart(comp_a, comp_b, chart_filename)
            comparison_report["chart_path"] = f"charts/{chart_filename}"
            
            # Store in DB
            conn = get_db_connection()
            if Config.USE_MYSQL:
                cursor = conn.cursor(dictionary=True)
                query = """
                    INSERT INTO comparisons (filename_a, filename_b, target_role, comparison_data)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (filename_a, filename_b, target_role, json.dumps(comparison_report)))
            else:
                cursor = conn.cursor()
                query = """
                    INSERT INTO comparisons (filename_a, filename_b, target_role, comparison_data)
                    VALUES (?, ?, ?, ?)
                """
                cursor.execute(query, (filename_a, filename_b, target_role, json.dumps(comparison_report)))
                
            conn.commit()
            comp_id = cursor.lastrowid
            cursor.close()
            conn.close()
            
            return redirect(url_for('comparison_dashboard', comp_id=comp_id))
            
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            flash(f"An error occurred during resume comparison: {str(e)}")
            return redirect(url_for('index'))
    else:
        flash("Invalid file format. Make sure both uploaded files are PDFs.")
        return redirect(url_for('index'))

def generate_matplotlib_comparison_chart(comp_a, comp_b, filename):
    """Generate a horizontal comparison bar chart using Matplotlib and save it."""
    try:
        import matplotlib
        matplotlib.use('Agg')  # Non-interactive backend
        import matplotlib.pyplot as plt
        import numpy as np
        
        labels = ['ATS Score', 'Skill Match %', 'Placement Prob %', 'Interview Readiness %', 'CGPA x10']
        values_a = [comp_a['ats_score'], comp_a['skill_match'], comp_a['placement_prob'], comp_a.get('interview_readiness', 0.0), comp_a['cgpa'] * 10]
        values_b = [comp_b['ats_score'], comp_b['skill_match'], comp_b['placement_prob'], comp_b.get('interview_readiness', 0.0), comp_b['cgpa'] * 10]
        
        x = np.arange(len(labels))
        width = 0.35
        
        fig, ax = plt.subplots(figsize=(8, 4.5), facecolor='#1e1e2e')
        ax.set_facecolor('#1e1e2e')
        
        # Plot bars
        rects1 = ax.bar(x - width/2, values_a, width, label=comp_a['name'][:15], color='#89b4fa')
        rects2 = ax.bar(x + width/2, values_b, width, label=comp_b['name'][:15], color='#f38ba8')
        
        # Styling
        ax.set_title('Head-to-Head Profile Comparison', fontsize=14, color='#cdd6f4', pad=15)
        ax.set_xticks(x)
        ax.set_xticklabels(labels, color='#cdd6f4')
        ax.tick_params(colors='#cdd6f4')
        
        # Remove spines
        for spine in ax.spines.values():
            spine.set_visible(False)
            
        ax.yaxis.grid(True, linestyle='--', alpha=0.15, color='#cdd6f4')
        ax.legend(facecolor='#181825', edgecolor='#313244', labelcolor='#cdd6f4')
        
        # Add value labels on top of bars
        def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                ax.annotate(f'{height:.1f}',
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom', color='#cdd6f4', fontsize=9)
                            
        autolabel(rects1)
        autolabel(rects2)
        
        fig.tight_layout()
        chart_dir = os.path.join(app.root_path, 'static', 'charts')
        plt.savefig(os.path.join(chart_dir, filename), dpi=150, facecolor=fig.get_facecolor(), edgecolor='none')
        plt.close()
    except Exception as ex:
        print(f"Failed to generate Matplotlib chart: {ex}")

@app.route('/comparison/<int:comp_id>')
def comparison_dashboard(comp_id):
    conn = get_db_connection()
    if Config.USE_MYSQL:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM comparisons WHERE id = %s", (comp_id,))
    else:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM comparisons WHERE id = ?", (comp_id,))
        
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if not row:
        flash("Comparison record not found.")
        return redirect(url_for('index'))
        
    comp_row = get_row_as_dict(row)
    comparison_details = json.loads(comp_row["comparison_data"])
    return render_template('compare.html', comp_id=comp_id, comparison=comparison_details)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'query' not in data or 'resume_id' not in data:
        return jsonify({"response": "Invalid request payload."}), 400
        
    resume_id = data['resume_id']
    query = data['query']
    
    conn = get_db_connection()
    if Config.USE_MYSQL:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT analysis_data FROM resumes WHERE id = %s", (resume_id,))
    else:
        cursor = conn.cursor()
        cursor.execute("SELECT analysis_data FROM resumes WHERE id = ?", (resume_id,))
        
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if not row:
        return jsonify({"response": "Candidate record not found."}), 404
        
    row_dict = get_row_as_dict(row)
    analysis_details = json.loads(row_dict["analysis_data"])
    
    response = get_chat_assistant_response(query, analysis_details)
    return jsonify({"response": response})

@app.route('/evaluate_interview', methods=['POST'])
def evaluate_interview():
    data = request.get_json()
    if not data or 'question' not in data or 'response' not in data or 'target_role' not in data:
        return jsonify({"error": "Invalid request payload."}), 400
        
    question = data['question']
    response = data['response']
    target_role = data['target_role']
    
    evaluation = evaluate_mock_response(question, response, target_role)
    return jsonify(evaluation)


if __name__ == '__main__':
    # Initialize DB tables on startup
    init_db()
    
    # Run the server
    app.run(debug=True, host='127.0.0.1', port=5000)
