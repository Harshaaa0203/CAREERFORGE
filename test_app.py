import sys
import os

def run_diagnostics():
    print("=== CareerForge AI Diagnostics ===")
    
    # Test 1: Imports
    print("Testing imports...")
    try:
        from config import Config
        from database import get_db_connection, init_db
        from nlp_processor import calculate_ats_and_skill_gap, extract_skills, parse_cgpa
        from ml_predictor import predict_placement
        from roadmap_generator import generate_personalized_roadmap
        print("[OK] Imports successful!")
    except Exception as e:
        print(f"[FAIL] Import test failed: {e}")
        sys.exit(1)
        
    # Test 2: Database Initialization
    print("\nTesting Database Initialization...")
    try:
        init_db()
        print("[OK] Database initialized successfully!")
    except Exception as e:
        print(f"[FAIL] Database initialization failed: {e}")
        sys.exit(1)
        
    # Test 3: NLP Parser on Mock Text
    print("\nTesting NLP Parser on mock text...")
    mock_resume_text = """
    Rishank Reddy
    rishank@example.com | +91 98765 43210
    
    Education:
    B.Tech in Computer Science and Engineering
    CGPA: 8.74/10.0
    
    Skills:
    Python, TensorFlow, PyTorch, SQL, Git, Docker, Machine Learning, Deep Learning, HTML, CSS
    
    Experience:
    AI Research Intern at TechCorp (6 months)
    - Developed and fine-tuned BERT transformers for sentiment classification.
    
    Projects:
    1. Sentiment Analysis Platform: Built using Python, NLP, and Hugging Face.
    2. E-Commerce Backend: Developed using Flask and PostgreSQL.
    
    Certifications:
    AWS Certified Solutions Architect
    """
    
    try:
        analysis = calculate_ats_and_skill_gap(mock_resume_text, "AI Engineer")
        print("Extracted Details:")
        print(f"  Name: {analysis['candidate_name']}")
        print(f"  Email: {analysis['email']}")
        print(f"  Phone: {analysis['phone']}")
        print(f"  ATS Score: {analysis['ats_score']}%")
        print(f"  Skill Match: {analysis['skill_match_percentage']}%")
        print(f"  Matched Skills: {analysis['matched_skills']}")
        print(f"  Projects Count: {analysis['metrics']['projects_count']}")
        print(f"  Internships Count: {analysis['metrics']['internships_count']}")
        print(f"  Certifications Count: {analysis['metrics']['certifications_count']}")
        print("[OK] NLP parsing successful!")
    except Exception as e:
        print(f"[FAIL] NLP parser test failed: {e}")
        sys.exit(1)
        
    # Test 4: ML Predictor
    print("\nTesting Machine Learning Predictor...")
    try:
        cgpa = parse_cgpa(mock_resume_text)
        projects = analysis["metrics"]["projects_count"]
        certifications = analysis["metrics"]["certifications_count"]
        internships = analysis["metrics"]["internships_count"]
        ats_score = analysis["ats_score"]
        skill_match = analysis["skill_match_percentage"]
        
        prediction = predict_placement(cgpa, projects, certifications, internships, ats_score, skill_match)
        print("Prediction Outputs:")
        print(f"  Placement Probability: {prediction['placement_probability']}%")
        print(f"  Status: {prediction['status']}")
        print(f"  Positive Factors count: {len(prediction['positive_factors'])}")
        print("[OK] ML Predictor successful!")
    except Exception as e:
        print(f"[FAIL] ML Predictor test failed: {e}")
        sys.exit(1)
        
    # Test 5: Roadmap Generator
    print("\nTesting Roadmap Generator...")
    try:
        roadmap = generate_personalized_roadmap("AI Engineer", analysis["missing_skills"])
        print("Roadmap Details:")
        print(f"  Target Role: {roadmap['target_role']}")
        print(f"  Missing Skills Recommendations count: {len(roadmap['missing_skills_recommendations'])}")
        print(f"  Timeline Phases count: {len(roadmap['timeline'])}")
        print("[OK] Roadmap Generator successful!")
    except Exception as e:
        print(f"[FAIL] Roadmap Generator test failed: {e}")
        sys.exit(1)

    # Test 6: New Career Diagnostics Features
    print("\nTesting New Career Diagnostics features...")
    try:
        from nlp_processor import calculate_interview_readiness, recommend_job_roles, extract_skills
        from roadmap_generator import get_cert_recommendations_with_links, get_detailed_project_recommendations
        
        # Test Interview Readiness Score
        readiness = calculate_interview_readiness(mock_resume_text, analysis)
        print(f"  Interview Readiness Score: {readiness['score']}%")
        print(f"  Category scores: {readiness['categories']}")
        print(f"  Feedback tips count: {len(readiness['tips'])}")
        assert readiness['score'] > 0
        
        # Test Job Role Recommendations
        skills = extract_skills(mock_resume_text)
        recs = recommend_job_roles(skills, "AI Engineer")
        print(f"  Job Recommendations count: {len(recs)}")
        for r in recs:
            print(f"    - Recommended: {r['role']} ({r['match_percentage']}% match)")
        assert len(recs) > 0
        
        # Test Project Recommendation Engine
        projects_rec = get_detailed_project_recommendations("AI Engineer")
        print(f"  Project Recommendations count: {len(projects_rec)}")
        for p in projects_rec:
            print(f"    - Project: {p['title']} ({p['difficulty']})")
        assert len(projects_rec) == 2
        
        # Test Certification Recommendations with Links
        certs_rec = get_cert_recommendations_with_links("AI Engineer", analysis["missing_skills"])
        print(f"  Certification Recommendations count: {len(certs_rec)}")
        for c in certs_rec:
            print(f"    - Cert: {c['name']} -> Link: {c['link']}")
        assert len(certs_rec) > 0
        
        print("[OK] New Career Diagnostics features successful!")
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        print(f"[FAIL] Career Diagnostics features test failed: {e}")
        sys.exit(1)
        
    # Test 7: Mock Interview, Salary Prediction & Chat Assistant
    print("\nTesting Mock HR Interview, Salary Prediction & Chat Assistant...")
    try:
        from nlp_processor import generate_hr_questions, evaluate_mock_response, predict_salary_lpa, get_chat_assistant_response
        
        # Test HR Question Generator
        questions = generate_hr_questions("AI Engineer")
        print(f"  Tailored HR questions count: {len(questions)}")
        assert len(questions) > 0
        
        # Test Interview Response Evaluation Heuristic
        mock_answer = "In my previous project, we faced a situation where the model latency was high. My task was to optimize inference. I implemented model quantization and caching. As a result, latency decreased by 40%."
        eval_result = evaluate_mock_response(questions[0], mock_answer, "AI Engineer")
        print(f"  Mock Evaluation Score: {eval_result['score']}%")
        print(f"  STAR check: {eval_result['star_check']}")
        print(f"  Feedback tips count: {len(eval_result['feedback'])}")
        assert eval_result['score'] > 0
        assert eval_result['star_check']['situation'] is True
        assert eval_result['star_check']['result'] is True
        
        # Test Salary Prediction Engine
        salary = predict_salary_lpa("AI Engineer", analysis["metrics"], analysis["skill_match_percentage"])
        print(f"  Salary Prediction: Low: {salary['low']} LPA, Median: {salary['median']} LPA, High: {salary['high']} LPA")
        assert salary['median'] > 0
        assert salary['low'] < salary['high']
        
        # Test Career Chat Response
        profile_context = {
            "target_role": "AI Engineer",
            "missing_skills": ["Docker", "Kubernetes"],
            "matched_skills": ["Python", "TensorFlow"],
            "roadmap": {
                "missing_skills_recommendations": [
                    {"skill": "Docker", "course": "Docker Deep Dive"}
                ]
            },
            "interview_readiness": {"score": 75.0},
            "salary_prediction": salary,
            "project_recommendations": [{"title": "MLOps Pipeline", "difficulty": "Advanced", "tech_stack": ["Git", "Docker"]}]
        }
        
        chat_resp_skills = get_chat_assistant_response("How do I learn my missing skills?", profile_context)
        print(f"  Chat response (missing skills): {chat_resp_skills.replace('₹', 'Rs.')}")
        assert "Docker" in chat_resp_skills
        
        chat_resp_salary = get_chat_assistant_response("What is my predicted salary range?", profile_context)
        print(f"  Chat response (salary): {chat_resp_salary.replace('₹', 'Rs.')}")
        assert "LPA" in chat_resp_salary
        
        chat_resp_default = get_chat_assistant_response("Hello, tell me about your helper functions", profile_context)
        print(f"  Chat response (default): {chat_resp_default.replace('₹', 'Rs.')}")
        assert "CareerForge AI" in chat_resp_default
        
        print("[OK] Mock Interview, Salary Prediction & Chat Assistant features tested successfully!")
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        print(f"[FAIL] Mock Interview, Salary Prediction & Chat Assistant test failed: {e}")
        sys.exit(1)
        
    print("\n======================================")
    print("ALL DIAGNOSTIC TESTS PASSED SUCCESSFULLY!")
    print("======================================")

if __name__ == '__main__':
    run_diagnostics()

