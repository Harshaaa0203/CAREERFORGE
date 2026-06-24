import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

def generate_synthetic_data(num_samples=1200, random_seed=42):
    np.random.seed(random_seed)
    
    # Features:
    # 1. CGPA (5.5 to 10.0)
    cgpa = np.random.uniform(5.5, 10.0, num_samples)
    
    # 2. Number of Projects (0 to 5)
    projects = np.random.randint(0, 6, num_samples)
    
    # 3. Number of Certifications (0 to 5)
    certifications = np.random.randint(0, 6, num_samples)
    
    # 4. Number of Internships (0 to 3)
    internships = np.random.randint(0, 4, num_samples)
    
    # 5. ATS Score (35 to 95)
    ats_score = np.random.uniform(35, 95, num_samples)
    
    # 6. Skill Match Percentage (20 to 100)
    skill_match = np.random.uniform(20, 100, num_samples)
    
    # Formulate placement decision logic with noise
    w_cgpa = 0.28
    w_projects = 0.15
    w_certs = 0.10
    w_interns = 0.18
    w_ats = 0.14
    w_skills = 0.15
    
    # Calculate base score (0.0 to 1.0)
    base_score = (
        w_cgpa * ((cgpa - 5.5) / 4.5) +
        w_projects * (projects / 5.0) +
        w_certs * (certifications / 5.0) +
        w_interns * (internships / 3.0) +
        w_ats * ((ats_score - 35) / 60.0) +
        w_skills * ((skill_match - 20) / 80.0)
    )
    
    # Add random noise to make it realistic
    noise = np.random.normal(0, 0.06, num_samples)
    final_score = base_score + noise
    
    # Threshold for placement (placed if final score >= 0.48)
    placed = (final_score >= 0.48).astype(int)
    
    df = pd.DataFrame({
        'cgpa': np.round(cgpa, 2),
        'projects': projects,
        'certifications': certifications,
        'internships': internships,
        'ats_score': np.round(ats_score, 1),
        'skill_match': np.round(skill_match, 1),
        'placed': placed
    })
    
    return df

def train_and_save_models():
    print("Generating synthetic placement dataset...")
    df = generate_synthetic_data()
    
    X = df[['cgpa', 'projects', 'certifications', 'internships', 'ats_score', 'skill_match']]
    y = df['placed']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 1. Random Forest Classifier
    print("Training Random Forest Classifier...")
    rf_model = RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_y_pred = rf_model.predict(X_test)
    rf_acc = accuracy_score(y_test, rf_y_pred)
    print(f"Random Forest Accuracy: {rf_acc:.4f}")
    
    # 2. Logistic Regression Classifier
    print("Training Logistic Regression...")
    lr_model = LogisticRegression(max_iter=1000, random_state=42)
    lr_model.fit(X_train, y_train)
    lr_y_pred = lr_model.predict(X_test)
    lr_acc = accuracy_score(y_test, lr_y_pred)
    print(f"Logistic Regression Accuracy: {lr_acc:.4f}")
    
    # Print Classification Report for Random Forest
    print("\nRandom Forest Classification Report:")
    print(classification_report(y_test, rf_y_pred))
    
    # Print Feature Importances
    print("Feature Importances (Random Forest):")
    for name, importance in zip(X.columns, rf_model.feature_importances_):
        print(f"  {name}: {importance:.4f}")
        
    # Ensure models directory exists
    os.makedirs('models', exist_ok=True)
    
    # Save the models
    rf_path = 'models/placement_rf.joblib'
    lr_path = 'models/placement_lr.joblib'
    joblib.dump(rf_model, rf_path)
    joblib.dump(lr_model, lr_path)
    print(f"\nModels successfully saved to '{rf_path}' and '{lr_path}'")
    
if __name__ == '__main__':
    train_and_save_models()
