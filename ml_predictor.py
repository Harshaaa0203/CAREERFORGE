import os
import joblib
import pandas as pd
from train_model import train_and_save_models

# File paths for models
RF_MODEL_PATH = os.path.join('models', 'placement_rf.joblib')
LR_MODEL_PATH = os.path.join('models', 'placement_lr.joblib')

def load_models():
    """Load models, training them first if they do not exist."""
    if not os.path.exists(RF_MODEL_PATH) or not os.path.exists(LR_MODEL_PATH):
        print("Models not found. Training models now...")
        train_and_save_models()
        
    rf_model = joblib.load(RF_MODEL_PATH)
    lr_model = joblib.load(LR_MODEL_PATH)
    return rf_model, lr_model

def predict_placement(cgpa, projects, certifications, internships, ats_score, skill_match):
    """
    Predict placement probability and return feedback.
    Inputs:
        cgpa (float): 5.5 - 10.0
        projects (int): 0 - 5
        certifications (int): 0 - 5
        internships (int): 0 - 3
        ats_score (float): 0 - 100
        skill_match (float): 0 - 100
    Returns:
        dict containing probability, classification label, and model details.
    """
    try:
        rf_model, lr_model = load_models()
    except Exception as e:
        print(f"Error loading models: {e}. Falling back to heuristic prediction.")
        # Heuristic fallback if ML fails to load (ensures system stability)
        score = (
            0.30 * ((cgpa - 5.5) / 4.5) +
            0.15 * (projects / 5.0) +
            0.10 * (certifications / 5.0) +
            0.18 * (internships / 3.0) +
            0.13 * (ats_score / 100.0) +
            0.14 * (skill_match / 100.0)
        )
        prob = max(0.05, min(0.98, score))
        return {
            "placement_probability": round(prob * 100, 1),
            "status": "Placed" if prob >= 0.50 else "Not Placed",
            "rf_probability": round(prob * 100, 1),
            "lr_probability": round(prob * 100, 1),
            "is_fallback": True
        }
        
    # Standardize data for Scikit-learn
    features = pd.DataFrame([{
        'cgpa': cgpa,
        'projects': projects,
        'certifications': certifications,
        'internships': internships,
        'ats_score': ats_score,
        'skill_match': skill_match
    }])
    
    # Predict probabilities (probability of class 1: Placed)
    rf_prob = rf_model.predict_proba(features)[0][1]
    lr_prob = lr_model.predict_proba(features)[0][1]
    
    # Combine predictions: Weighted average favoring Random Forest (which is more robust to non-linear features)
    combined_prob = 0.6 * rf_prob + 0.4 * lr_prob
    combined_prob_pct = round(combined_prob * 100, 1)
    
    # Determine placement status label
    status = "Highly Probable" if combined_prob >= 0.75 else "Probable" if combined_prob >= 0.5 else "Needs Improvement"
    
    # Generate predictive insights based on feature importances and standards
    positive_factors = []
    negative_factors = []
    
    if cgpa >= 8.5:
        positive_factors.append(f"Outstanding academic record (CGPA: {cgpa}) serves as a strong filter bypass.")
    elif cgpa >= 7.5:
        positive_factors.append(f"Good academic standing (CGPA: {cgpa}) meets standard placement cut-offs.")
    else:
        negative_factors.append(f"CGPA of {cgpa} is below the preferred threshold of 7.5. Many tier-1 recruiters filter below 7.5.")
        
    if internships >= 2:
        positive_factors.append(f"Having {internships} internships shows strong industrial experience and hands-on exposure.")
    elif internships == 1:
        positive_factors.append("Completed 1 internship, demonstrating standard industry exposure.")
    else:
        negative_factors.append("No professional internship experience detected. Internships carry high weight for recruiters.")
        
    if projects >= 3:
        positive_factors.append(f"Multiple technical projects ({projects}) show strong practical engineering skills.")
    elif projects <= 1:
        negative_factors.append("Very few projects listed. Candidates with 3+ projects stand out in technical screenings.")
        
    if skill_match >= 75:
        positive_factors.append(f"Excellent alignment of core skills ({skill_match}%) with the target role.")
    elif skill_match < 45:
        negative_factors.append(f"Skill match of {skill_match}% is low. You are missing more than half of the role's essential skills.")
        
    if ats_score >= 75:
        positive_factors.append(f"High ATS compatibility score ({ats_score}%) ensures the resume is parsed correctly by automated filters.")
    elif ats_score < 60:
        negative_factors.append("Low resume ATS formatting score. The structure needs structural changes to pass resume parsers.")
        
    return {
        "placement_probability": combined_prob_pct,
        "status": status,
        "rf_probability": round(rf_prob * 100, 1),
        "lr_probability": round(lr_prob * 100, 1),
        "positive_factors": positive_factors,
        "negative_factors": negative_factors,
        "is_fallback": False
    }
