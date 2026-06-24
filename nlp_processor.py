import re
import pdfplumber
import PyPDF2
import os

# Define core job roles and their required/highly relevant technical skills
JOB_ROLES = {
    "AI Engineer": [
        "python", "tensorflow", "pytorch", "deep learning", "nlp", "computer vision", 
        "transformers", "huggingface", "keras", "generative ai", "llm", "langchain", 
        "scikit-learn", "numpy", "pandas", "openai", "machine learning"
    ],
    "Data Scientist": [
        "python", "r", "sql", "pandas", "numpy", "scikit-learn", "machine learning", 
        "statistics", "tableau", "power bi", "matplotlib", "seaborn", "git", 
        "data visualization", "regression", "clustering"
    ],
    "Software Developer": [
        "java", "c++", "python", "git", "data structures", "algorithms", "oop", 
        "sql", "unit testing", "agile", "linux", "docker", "ci/cd", "design patterns"
    ],
    "Full Stack Developer": [
        "javascript", "typescript", "react", "node.js", "express", "html", "css", 
        "mongodb", "postgresql", "sql", "rest api", "git", "docker", "bootstrap", "aws"
    ],
    "Data Analyst": [
        "sql", "excel", "tableau", "power bi", "python", "statistics", "pandas", 
        "data cleaning", "dashboard", "reporting", "business intelligence", "numpy"
    ],
    "Machine Learning Engineer": [
        "python", "tensorflow", "pytorch", "machine learning", "scikit-learn", 
        "mlops", "docker", "kubernetes", "pandas", "git", "nlp", "deep learning",
        "aws", "gcp", "model deployment"
    ],
    "Cybersecurity Analyst": [
        "network security", "linux", "cryptography", "firewalls", "penetration testing", 
        "wireshark", "siem", "ethical hacking", "iam", "soc", "vulnerability assessment", 
        "cissp", "ceh", "owasp", "incident response"
    ],
    "Java Developer": [
        "java", "spring boot", "spring", "hibernate", "sql", "maven", "gradle", 
        "junit", "microservices", "rest api", "git", "oop", "multithreading"
    ]
}

# A comprehensive list of technical skills to look for in a resume (all roles)
ALL_SKILLS = set(
    [skill for skills in JOB_ROLES.values() for skill in skills] + [
        "c", "c#", "go", "rust", "scala", "kotlin", "swift", "php", "ruby", "perl",
        "angular", "vue", "next.js", "svelte", "django", "flask", "fastapi", "spring",
        "mysql", "oracle", "sqlite", "redis", "elasticsearch", "cassandra",
        "aws", "azure", "gcp", "docker", "kubernetes", "jenkins", "terraform", "ansible",
        "hadoop", "spark", "hive", "kafka", "flask", "scipy", "graphql", "jquery",
        "tailwind", "sass", "postman", "jira", "numpy", "pandas", "scikit-learn",
        "matplotlib", "seaborn", "nltk", "spacy", "opencv", "powerbi", "tableau"
    ]
)

def extract_text_from_pdf(pdf_path):
    """Extract all text from a PDF resume using pdfplumber with PyPDF2 as fallback."""
    text = ""
    # Try pdfplumber first
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"pdfplumber failed: {e}. Falling back to PyPDF2.")
        text = ""
        
    # Fallback to PyPDF2 if pdfplumber failed or returned empty text
    if not text.strip():
        try:
            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            print(f"PyPDF2 fallback also failed: {e}")
            
    return text

def parse_contact_info(text):
    """Extract email and phone number from text."""
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    phone_pattern = r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'
    
    email_match = re.search(email_pattern, text)
    phone_match = re.search(phone_pattern, text)
    
    email = email_match.group(0) if email_match else "Not Found"
    phone = phone_match.group(0) if phone_match else "Not Found"
    
    # Simple Name extraction heuristic: search for the first line or capitalized words at the top
    # We look for the first 2-3 words on the first non-empty line
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    candidate_name = "Candidate Name"
    if lines:
        for line in lines[:3]:
            # If the line contains words but no numbers/special chars, it's likely the name
            if re.match(r'^[a-zA-Z\s]{3,30}$', line) and "resume" not in line.lower() and "cv" not in line.lower():
                candidate_name = line
                break
        if candidate_name == "Candidate Name" and lines:
            # Fallback to just the first line if it's relatively short
            if len(lines[0]) < 40 and not any(c in lines[0] for c in ['@', ':', '/']):
                candidate_name = lines[0]
                
    return candidate_name, email, phone

def parse_cgpa(text):
    """Extract CGPA/GPA or Percentage from text and normalize to a 10.0 scale."""
    # Pattern to match: CGPA: 9.2, GPA: 3.8/4, CGPA of 8.56, 85%, etc.
    cgpa_patterns = [
        r'\b(?:cgpa|gpa|pointer|g.p.a|c.g.p.a)\b\s*(?:of|is|:|-|=)?\s*([0-9]\.[0-9]{1,2})',
        r'\b([0-9]\.[0-9]{1,2})\s*/\s*(?:10|4)\b',
        r'\b([0-9]{2}(?:\.[0-9]{1,2})?)\s*%',
        r'\b(?:percentage|aggregate|marks)\b\s*(?:of|is|:|-|=)?\s*([0-9]{2}(?:\.[0-9]{1,2})?)'
    ]
    
    extracted_vals = []
    
    # 1. Look for explicit pattern matches
    for pattern in cgpa_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for val in matches:
            try:
                extracted_vals.append(float(val))
            except ValueError:
                pass
                
    # 2. Heuristics for normalizing values
    if extracted_vals:
        val = extracted_vals[0]
        # If it looks like a 4.0 GPA scale (e.g. between 2.0 and 4.0)
        if 2.0 <= val <= 4.0:
            return round(val * 2.5, 2)
        # If it looks like a 10.0 CGPA scale
        elif 4.0 < val <= 10.0:
            return round(val, 2)
        # If it looks like a percentage (e.g. between 40 and 100)
        elif 40.0 <= val <= 100.0:
            return round(val / 10.0, 2)
            
    # 3. Fallback scan: Search for any standalone float in the text between 5.0 and 10.0 in proximity to education terms
    edu_terms = ["btech", "b.tech", "be", "b.e", "bsc", "b.sc", "mtech", "m.tech", "mca", "university", "college", "hsc", "ssc", "school"]
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if any(term in line.lower() for term in edu_terms):
            # Look for floats in this or next 2 lines
            search_window = lines[i:min(i+3, len(lines))]
            combined_window = " ".join(search_window)
            floats = re.findall(r'\b([5-9]\.[0-9]{1,2}|10\.0)\b', combined_window)
            if floats:
                return round(float(floats[0]), 2)
                
    # Default return if nothing found
    return 7.5

def parse_experience_and_internships(text):
    """Estimate number of internships and years of experience."""
    text_lower = text.lower()
    
    # Count internships
    internship_matches = len(re.findall(r'\b(?:intern|internship|trainee|apprenticeship)\b', text_lower))
    # We estimate based on word counts. If "intern" is found multiple times in different context blocks
    # let's assume internships count based on occurrences but capped at 3.
    internships = min(3, max(0, internship_matches // 2))
    if "intern" in text_lower and internships == 0:
        internships = 1
        
    # Estimate projects
    # Scan for project headings or bullet indicators
    project_sections = re.findall(r'\b(?:project|projects|academic projects|personal projects)\b', text_lower)
    project_bullets = len(re.findall(r'\b(?:project|developed|implemented|designed|created|built)\b', text_lower))
    
    # Estimate project count
    projects = 1
    if project_sections:
        projects = max(2, min(5, project_bullets // 3))
    else:
        projects = max(1, min(4, project_bullets // 4))
        
    # Estimate certifications
    cert_matches = len(re.findall(r'\b(?:certified|certification|certifications|certificate|course|nanodegree)\b', text_lower))
    # Let's check common cert providers
    cert_providers = ["aws", "azure", "gcp", "cisco", "oracle", "scrum", "red hat", "coursera", "udemy", "nptel"]
    provider_matches = sum(1 for provider in cert_providers if provider in text_lower)
    certifications = max(provider_matches, min(5, cert_matches // 2))
    
    # Estimate years of experience
    experience_years = 0
    exp_matches = re.findall(r'(\d+)\+?\s*(?:year|yr)s?\b(?:\s*of)?\s*(?:experience|work|industry)', text_lower)
    if exp_matches:
        try:
            experience_years = int(exp_matches[0])
        except ValueError:
            pass
    else:
        # If no explicit "X years of experience" match, look for date patterns (e.g. 2021 - 2023, 2022 to Present)
        # and check if the word "experience" or "employment" is nearby.
        if "experience" in text_lower or "work history" in text_lower or "employment" in text_lower:
            # Default to 1 year if experience keywords are prominent, else 0 (student profile)
            experience_years = 1 if len(re.findall(r'\b(?:experience|engineer|developer|analyst)\b', text_lower)) > 4 else 0
            
    return internships, projects, certifications, experience_years

def extract_skills(text):
    """Extract technical skills matching our pre-defined skills dictionary."""
    extracted = []
    text_lower = text.lower()
    
    # Match skills using word boundaries or custom contains logic for complex terms
    for skill in ALL_SKILLS:
        # Escape characters like c++ or .net
        escaped_skill = re.escape(skill)
        # Check word boundaries for alphabetic skills
        if skill.isalpha():
            pattern = rf'\b{escaped_skill}\b'
        else:
            # For skills like c++, .net, react.js, etc.
            pattern = rf'{escaped_skill}'
            
        if re.search(pattern, text_lower):
            extracted.append(skill)
            
    return sorted(list(set(extracted)))

def calculate_ats_and_skill_gap(text, target_role):
    """
    Perform ATS score calculation, missing keyword analysis, and skill gap calculation.
    """
    text_lower = text.lower()
    
    # 1. Get required skills for job role
    required_skills = JOB_ROLES.get(target_role, JOB_ROLES["Software Developer"])
    
    # 2. Extract skills from resume
    extracted_skills = extract_skills(text)
    
    # 3. Compute skill gaps
    matched_skills = [skill for skill in required_skills if skill in extracted_skills]
    missing_skills = [skill for skill in required_skills if skill not in extracted_skills]
    
    skill_match_percentage = 0.0
    if required_skills:
        skill_match_percentage = round((len(matched_skills) / len(required_skills)) * 100, 1)
        
    # 4. ATS Scoring Algorithm
    # a. Keyword/Skill Match Score (Max: 40 points)
    keyword_score = (len(matched_skills) / len(required_skills)) * 40 if required_skills else 0
    
    # b. Section completeness Check (Max: 30 points)
    section_score = 0
    sections = {
        "education": ["education", "qualification", "academic", "university", "college", "school"],
        "skills": ["skills", "technical skills", "technologies", "expertise", "core competencies"],
        "experience": ["experience", "work history", "employment", "professional experience", "internship", "intern"],
        "projects": ["projects", "academic projects", "personal projects", "key projects"],
        "certifications": ["certifications", "certifications & achievements", "achievements", "courses", "certificates"]
    }
    
    found_sections = []
    missing_sections = []
    for section_name, keywords in sections.items():
        found = False
        for kw in keywords:
            if kw in text_lower:
                found = True
                break
        if found:
            section_score += 6
            found_sections.append(section_name.capitalize())
        else:
            missing_sections.append(section_name.capitalize())
            
    # c. Resume Formatting and Quality Score (Max: 30 points)
    formatting_score = 0
    
    # Quality metric 1: Length check (10 points)
    word_count = len(text.split())
    if 200 <= word_count <= 1000:
        formatting_score += 10
    elif 100 <= word_count < 200 or 1000 < word_count <= 1500:
        formatting_score += 6
    else:
        formatting_score += 2  # Very short or extremely long
        
    # Quality metric 2: Contact info check (20 points - 10 for email, 10 for phone)
    candidate_name, email, phone = parse_contact_info(text)
    if email != "Not Found":
        formatting_score += 10
    if phone != "Not Found":
        formatting_score += 10
        
    # Combine scores
    ats_score = round(keyword_score + section_score + formatting_score, 1)
    # Clamp between 0 and 100
    ats_score = max(0.0, min(100.0, ats_score))
    
    # 5. Generate Suggestions for Improvement
    suggestions = []
    if missing_skills:
        suggestions.append(f"Add key technical skills required for {target_role}: {', '.join(missing_skills[:3])}.")
    if missing_sections:
        suggestions.append(f"Include the following missing sections to improve structure: {', '.join(missing_sections)}.")
    if word_count < 200:
        suggestions.append("Your resume is too short. Elaborate more on your projects, certifications, and responsibilities.")
    elif word_count > 1000:
        suggestions.append("Your resume is very long. Try to condense it to 1-2 pages focusing on impact and key metrics.")
    if email == "Not Found":
        suggestions.append("Ensure your email address is clearly visible at the top of the resume.")
    if phone == "Not Found":
        suggestions.append("Ensure your contact phone number is clearly visible at the top of the resume.")
        
    # Strengths and Weaknesses analysis
    strengths = []
    weaknesses = []
    
    if skill_match_percentage >= 70:
        strengths.append(f"Strong technical alignment with the {target_role} profile.")
    elif skill_match_percentage >= 40:
        strengths.append(f"Moderate coverage of core {target_role} skills.")
    else:
        weaknesses.append(f"Low coverage of core technical skills required for {target_role}.")
        
    if section_score >= 24:
        strengths.append("Excellent resume structure with all standard sections included.")
    else:
        weaknesses.append("Incomplete resume structure. Some standard sections are missing.")
        
    if email != "Not Found" and phone != "Not Found":
        strengths.append("Contact details are complete and easy to locate.")
    else:
        weaknesses.append("Missing essential contact details (email or phone).")
        
    internships, projects, certifications, exp_years = parse_experience_and_internships(text)
    if internships > 0:
        strengths.append(f"Practical industry experience through {internships} internship(s).")
    else:
        weaknesses.append("Lack of industry internship experience. Consider applying for internship roles.")
        
    if projects >= 3:
        strengths.append(f"Demonstrates hands-on engineering capability with {projects} projects.")
    elif projects == 0:
        weaknesses.append("No technical projects found. Projects are vital to showcase your skills.")
        
    if certifications >= 2:
        strengths.append(f"Credibility enhanced by {certifications} professional certifications.")
        
    # Missing keywords (other than direct technical skills, we can check for action verbs or domain terms)
    domain_keywords = {
        "AI Engineer": ["model optimization", "neural networks", "training", "deployment", "fine-tuning", "inference"],
        "Data Scientist": ["statistical modeling", "hypothesis testing", "data pipelines", "predictive modeling", "insights"],
        "Software Developer": ["object-oriented design", "version control", "software lifecycle", "debugging", "architecture"],
        "Full Stack Developer": ["responsive design", "database schema", "front-end", "back-end", "state management"],
        "Data Analyst": ["data cleaning", "ad-hoc reporting", "trend analysis", "spreadsheets", "data collection"],
        "Machine Learning Engineer": ["hyperparameter tuning", "ml pipeline", "model training", "feature engineering", "scalability"],
        "Cybersecurity Analyst": ["vulnerability scanning", "log analysis", "security controls", "compliance", "threat detection"],
        "Java Developer": ["enterprise applications", "restful service", "concurrency", "orm", "dependency injection"]
    }
    
    missing_domain_keywords = []
    for kw in domain_keywords.get(target_role, ["version control", "agile"]):
        if kw not in text_lower:
            missing_domain_keywords.append(kw)
            
    return {
        "candidate_name": candidate_name,
        "email": email,
        "phone": phone,
        "ats_score": ats_score,
        "skill_match_percentage": skill_match_percentage,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "suggestions": suggestions,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "missing_keywords": missing_skills[:4] + missing_domain_keywords[:3],
        "metrics": {
            "projects_count": projects,
            "certifications_count": certifications,
            "internships_count": internships,
            "experience_years": exp_years
        }
    }

def calculate_interview_readiness(text, analysis_data):
    """
    Calculate an Interview Readiness Score (0-100) with category breakdowns and feedback tips.
    Weights:
        Technical (Skill Match): 35%
        Projects: 25%
        Experience: 20%
        ATS/Formatting: 10%
        Certifications: 10%
    """
    metrics = analysis_data.get("metrics", {})
    skill_match = analysis_data.get("skill_match_percentage", 0.0)
    ats_score = analysis_data.get("ats_score", 0.0)
    
    projects_count = metrics.get("projects_count", 0)
    certifications_count = metrics.get("certifications_count", 0)
    internships_count = metrics.get("internships_count", 0)
    experience_years = metrics.get("experience_years", 0)
    
    # 1. Technical Score (Skill Match Percentage is 0-100)
    tech_score = skill_match
    
    # 2. Project Score (0 -> 10, 1 -> 40, 2 -> 75, 3+ -> 100)
    if projects_count == 0:
        proj_score = 10.0
    elif projects_count == 1:
        proj_score = 40.0
    elif projects_count == 2:
        proj_score = 75.0
    else:
        proj_score = 100.0
        
    # 3. Experience Score (0 -> 20, 1 -> 70, 2+ -> 100)
    # Scale based on internships and years of experience
    exp_factor = internships_count + min(2, experience_years)
    if exp_factor == 0:
        exp_score = 20.0
    elif exp_factor == 1:
        exp_score = 70.0
    else:
        exp_score = 100.0
        
    # 4. ATS/Formatting Score (ATS score is 0-100)
    ats_formatting_score = ats_score
    
    # 5. Certification Score (0 -> 20, 1 -> 60, 2+ -> 100)
    if certifications_count == 0:
        cert_score = 20.0
    elif certifications_count == 1:
        cert_score = 60.0
    else:
        cert_score = 100.0
        
    # Weighted calculation
    score = (
        0.35 * tech_score +
        0.25 * proj_score +
        0.20 * exp_score +
        0.10 * ats_formatting_score +
        0.10 * cert_score
    )
    score = round(max(0.0, min(100.0, score)), 1)
    
    # Generate targeted feedback tips for interview readiness
    tips = []
    if tech_score < 50:
        tips.append("Revise fundamental technical concepts and system design matching the target role.")
    elif tech_score < 75:
        tips.append("Strengthen intermediate domain libraries and practical tools to boost your technical depth.")
        
    if proj_score < 50:
        tips.append("Build at least one comprehensive, end-to-end project utilizing your target tech stack.")
    elif proj_score < 80:
        tips.append("Incorporate another detailed project into your resume to showcase multiple architectures.")
        
    if exp_score < 50:
        tips.append("Gain practical exposure via internships, freelance gigs, or collaborative open-source contributions.")
    elif exp_score < 80:
        tips.append("Practice behavioral questions focused on collaborative and real-world development environments.")
        
    if cert_score < 50:
        tips.append("Enroll in industry-standard credentials (e.g. AWS, CompTIA, Google Cloud) to validate your skill set.")
        
    if ats_formatting_score < 60:
        tips.append("Format your resume with clear headers, standard sections, and simple fonts to pass parsing checks.")
        
    if not tips:
        tips.append("Outstanding profile! Continue practicing mock interviews and system architecture questions.")
        
    return {
        "score": score,
        "categories": {
            "technical": round(tech_score, 1),
            "project": round(proj_score, 1),
            "experience": round(exp_score, 1),
            "ats_formatting": round(ats_formatting_score, 1),
            "certification": round(cert_score, 1)
        },
        "tips": tips[:3]  # Return top 3 most critical tips
    }

def recommend_job_roles(extracted_skills, current_target_role):
    """
    Recommend alternative job roles by comparing candidate's extracted skills with our JOB_ROLES library.
    Returns the top 3 alternative matching roles.
    """
    extracted_skills_set = set([s.lower().strip() for s in extracted_skills])
    
    recommendations = []
    for role, required_skills in JOB_ROLES.items():
        if role.lower().strip() == current_target_role.lower().strip():
            continue
            
        required_set = set([s.lower().strip() for s in required_skills])
        if not required_set:
            continue
            
        matched = required_set.intersection(extracted_skills_set)
        match_pct = round((len(matched) / len(required_set)) * 100, 1)
        
        # We only recommend if there is at least some skill match
        if match_pct > 0:
            recommendations.append({
                "role": role,
                "match_percentage": match_pct,
                "matched_skills": sorted(list(matched)),
                "missing_skills": sorted(list(required_set.difference(extracted_skills_set)))
            })
            
    # Sort recommendations by match percentage descending
    recommendations.sort(key=lambda x: x["match_percentage"], reverse=True)
    
    # Return top 3, or if empty, select default top related roles
    if not recommendations:
        # Fallback to general roles
        fallback_roles = [r for r in JOB_ROLES.keys() if r.lower().strip() != current_target_role.lower().strip()]
        for r in fallback_roles[:3]:
            recommendations.append({
                "role": r,
                "match_percentage": 0.0,
                "matched_skills": [],
                "missing_skills": JOB_ROLES[r]
            })
            
    return recommendations[:3]

def generate_hr_questions(target_role):
    """
    Returns 5 behavioral/situational HR interview questions tailored to the target role.
    """
    hr_questions_db = {
        "AI Engineer": [
            "Tell me about a challenging machine learning or generative AI problem you faced, and how you resolved it.",
            "How do you keep yourself updated with the extremely fast-moving advancements in LLMs and AI models?",
            "Describe a situation where an AI model you built did not perform well in production. How did you diagnose and fix it?",
            "Explain a complex technical AI concept (like transformers or backpropagation) as if you were explaining it to a non-technical client.",
            "Why do you want to work as an AI Engineer at our company specifically?"
        ],
        "Data Scientist": [
            "Describe a time when you had to clean a highly messy, incomplete dataset. What strategies did you use?",
            "How do you explain the statistical significance of an A/B test result to business executives who don't understand math?",
            "Tell me about a project where you built a predictive model. What metrics did you prioritize (e.g. precision vs. recall) and why?",
            "Share an experience where your data insights directly influenced a product or business decision.",
            "Why did you choose Data Science as your career path?"
        ],
        "Software Developer": [
            "Tell me about a time when you had to debug a critical issue in production under tight deadlines.",
            "How do you handle disagreement with a technical lead or teammate regarding software architecture or code style?",
            "Describe a personal project where you built a system from scratch. What design choices did you make?",
            "What is your approach to unit testing, and how do you ensure code quality in your developer workflow?",
            "Why do you want to work as a Software Developer with us?"
        ],
        "Full Stack Developer": [
            "How do you decide between front-end performance vs. back-end query optimization when scaling a feature?",
            "Tell me about a time you had to implement user authentication and authorization securely. What design did you choose?",
            "Describe a challenging bug that involved both client-side React rendering and server-side APIs. How did you resolve it?",
            "How do you approach creating a responsive, highly usable design for non-technical users?",
            "Why are you interested in a Full Stack role rather than specializing in just front-end or back-end?"
        ],
        "Data Analyst": [
            "Describe a time you noticed an anomaly or error in a business dashboard. How did you track it down and correct it?",
            "How do you communicate structural data findings to stakeholders who prefer visual insights over raw SQL aggregates?",
            "Tell me about a time you had to deliver a critical report on a very tight timeline. How did you organize your analytical process?",
            "What is your process for gathering requirements from business managers before writing SQL analysis scripts?",
            "Why do you want to work as a Data Analyst with us?"
        ],
        "Machine Learning Engineer": [
            "Describe a scenario where you dockerized and deployed an ML model. What were the latency considerations?",
            "How do you deal with training data drift over time, and what monitoring checks do you put in place?",
            "Tell me about a model optimization technique (like pruning or quantization) you have applied to speed up inference.",
            "Explain how you would design a training pipeline that automatically runs when new labeled data is added.",
            "Why do you want to work as a Machine Learning Engineer with us?"
        ],
        "Cybersecurity Analyst": [
            "Tell me about a time you detected a security alert or suspicious activity. How did you triage and investigate it?",
            "How do you educate non-technical employees about phishing threats and general system security hygiene?",
            "Describe a vulnerability assessment or penetration test you conducted. What did you discover and how did you report it?",
            "How do you keep up with newly published CVEs and zero-day exploits in the industry?",
            "Why do you want to work as a Cybersecurity Analyst with us?"
        ],
        "Java Developer": [
            "Describe a scenario where you had to troubleshoot memory leaks or thread bottlenecks in a JVM environment.",
            "Tell me about a time you designed database mappings using Hibernate. How did you prevent N+1 query problems?",
            "Explain how you design REST API endpoints to follow standard microservices patterns in Spring Boot.",
            "What is your approach to writing unit tests using JUnit and Mockito for mock database responses?",
            "Why do you want to work as a Java Developer with us?"
        ]
    }
    
    default_hr_questions = [
        "Tell me about yourself and why you're interested in the target role.",
        "Describe a time you worked on a team project and had to resolve a conflict or disagreement.",
        "Tell me about a technical project you are most proud of. What was your contribution?",
        "How do you manage your time and prioritize tasks when handling multiple strict deadlines?",
        "Where do you see yourself professionally in the next three to five years?"
    ]
    
    return hr_questions_db.get(target_role, default_hr_questions)

def evaluate_mock_response(question, response, target_role):
    """
    Evaluates a candidate's answer to an HR interview question using heuristic NLP rules.
    Checks length, structure (STAR method clues), action verbs, and keyword alignment.
    """
    response_clean = response.strip()
    word_count = len(response_clean.split())
    
    score = 40.0 # base score
    feedback = []
    star_check = {"situation": False, "task": False, "action": False, "result": False}
    
    # 1. Length evaluation
    if word_count == 0:
        return {
            "score": 0.0,
            "grammar_check": "N/A",
            "star_check": star_check,
            "feedback": ["Response is empty. Please enter your answer."]
        }
    elif word_count < 15:
        score -= 20.0
        feedback.append("Your response is extremely short. Try to elaborate and provide specific context.")
    elif word_count < 45:
        score += 10.0
        feedback.append("Good start, but try to provide more details about your specific actions and results.")
    else:
        score += 25.0
        feedback.append("Excellent length. You have provided a detailed response.")
        
    # 2. STAR structure parsing
    response_lower = response_clean.lower()
    
    # Situation keys
    situation_keys = ["project", "situation", "problem", "context", "role", "background", "company", "when", "team", "university", "academic"]
    if any(k in response_lower for k in situation_keys):
        star_check["situation"] = True
        score += 7.0
    else:
        feedback.append("Add details about the setup or background (Situation) - e.g., 'During my internship at X...'")
        
    # Task keys
    task_keys = ["task", "responsibility", "goal", "assigned", "required", "objective", "challenge"]
    if any(k in response_lower for k in task_keys):
        star_check["task"] = True
        score += 7.0
    else:
        feedback.append("Clarify the core problem or assignment (Task) - e.g., 'My task was to build...'")
        
    # Action keys
    action_keys = ["action", "wrote", "built", "implemented", "designed", "developed", "solved", "analyzed", "coded", "configured", "debugged", "fixed", "created", "refactored"]
    if any(k in response_lower for k in action_keys):
        star_check["action"] = True
        score += 8.0
    else:
        feedback.append("Incorporate specific action verbs showing what YOU did (Action) - e.g., 'I refactored the database schema...'")
        
    # Result keys
    result_keys = ["result", "outcome", "impact", "consequently", "achieved", "completed", "percent", "performance", "speed", "improved", "increased", "reduced", "led to"]
    if any(k in response_lower for k in result_keys):
        star_check["result"] = True
        score += 8.0
    else:
        feedback.append("Describe the outcome, lessons learned, or metrics (Result) - e.g., 'This reduced latency by 30%.'")
        
    # 3. Action verbs and role terminology check
    tech_skills = JOB_ROLES.get(target_role, [])
    matched_skills_in_ans = [skill for skill in tech_skills if skill.lower() in response_lower]
    if matched_skills_in_ans:
        score += min(10.0, len(matched_skills_in_ans) * 3.0)
        feedback.insert(0, f"Great job referencing role-relevant tech stack keywords: {', '.join(matched_skills_in_ans[:3])}.")
        
    action_words = ["managed", "resolved", "led", "communicated", "collaborated", "optimized", "delivered"]
    matched_actions = [word for word in action_words if word in response_lower]
    if matched_actions:
        score += min(5.0, len(matched_actions) * 1.5)
        
    # Clamp score
    score = round(max(5.0, min(100.0, score)), 1)
    
    # Grammar heuristic (based on structure/punctuation/length)
    if word_count > 30 and response_clean[0].isupper() and (response_clean.endswith('.') or response_clean.endswith('?')):
        grammar = "Excellent"
    elif word_count > 15:
        grammar = "Good"
    else:
        grammar = "Needs Polish"
        
    return {
        "score": score,
        "grammar_check": grammar,
        "star_check": star_check,
        "feedback": feedback[:3] # Limit to top 3 tips
    }

def predict_salary_lpa(target_role, metrics, skill_match):
    """
    Predict entry-level salary packages (Low, Median, High) in Lakhs per Annum (LPA).
    Based on baseline packages for roles and candidate statistics.
    """
    baselines = {
        "AI Engineer": 8.5,
        "Data Scientist": 8.0,
        "Software Developer": 6.5,
        "Full Stack Developer": 7.0,
        "Data Analyst": 5.5,
        "Machine Learning Engineer": 8.5,
        "Cybersecurity Analyst": 7.5,
        "Java Developer": 6.2
    }
    
    base_lpa = baselines.get(target_role, 6.0)
    
    # Calculate modifiers
    cgpa = metrics.get("cgpa", 7.5)
    projects = metrics.get("projects_count", 0)
    certifications = metrics.get("certifications_count", 0)
    internships = metrics.get("internships_count", 0)
    
    modifiers = 0.0
    
    # CGPA modifier
    if cgpa >= 9.0:
        modifiers += 0.20
    elif cgpa >= 8.0:
        modifiers += 0.10
    elif cgpa < 7.0:
        modifiers -= 0.10
        
    # Projects modifier
    if projects >= 3:
        modifiers += 0.15
    elif projects == 2:
        modifiers += 0.05
    elif projects <= 1:
        modifiers -= 0.05
        
    # Certifications modifier
    if certifications >= 2:
        modifiers += 0.10
    elif certifications == 1:
        modifiers += 0.05
        
    # Internships modifier
    if internships >= 2:
        modifiers += 0.25
    elif internships == 1:
        modifiers += 0.15
        
    # Skill match modifier
    if skill_match >= 75:
        modifiers += 0.15
    elif skill_match >= 50:
        modifiers += 0.05
    elif skill_match < 40:
        modifiers -= 0.10
        
    median_lpa = base_lpa * (1.0 + modifiers)
    
    # Range constraints
    low_lpa = max(3.0, median_lpa * 0.8)
    high_lpa = max(low_lpa + 1.5, median_lpa * 1.35)
    
    return {
        "low": round(low_lpa, 1),
        "median": round(median_lpa, 1),
        "high": round(high_lpa, 1)
    }

def get_chat_assistant_response(query, candidate_profile):
    """
    Context-aware Career Chat response builder based on local candidate details.
    """
    query_lower = query.lower()
    target_role = candidate_profile.get("target_role", "Software Developer")
    missing_skills = candidate_profile.get("missing_skills", [])
    matched_skills = candidate_profile.get("matched_skills", [])
    roadmap = candidate_profile.get("roadmap", {})
    interview_score = candidate_profile.get("interview_readiness", {}).get("score", 70.0)
    salary = candidate_profile.get("salary_prediction", {"median": 6.5})
    
    # 1. Topic: Missing Skills / Learn
    if any(word in query_lower for word in ["learn", "skill", "missing", "gap", "study", "acquire"]):
        if missing_skills:
            skills_list = ", ".join(missing_skills[:3])
            courses = [item.get("course") for item in roadmap.get("missing_skills_recommendations", []) if item.get("skill") in missing_skills]
            course_text = f" I recommend starting with '{courses[0]}'." if courses else ""
            return (
                f"Based on your profile, you need to learn key technical skills for the **{target_role}** role. "
                f"Your most critical missing skills are **{skills_list}**.{course_text} "
                f"Check the 'Career & Credentials' or 'Learning Roadmap' tab for direct course links!"
            )
        else:
            return f"Fantastic news! You have no missing skills required for **{target_role}**. You are fully aligned."
            
    # 2. Topic: Projects / Portfolio
    if any(word in query_lower for word in ["project", "portfolio", "build", "create", "practical"]):
        projects_list = candidate_profile.get("project_recommendations", [])
        if projects_list:
            proj = projects_list[0]
            techs = ", ".join(proj.get("tech_stack", []))
            return (
                f"To strengthen your portfolio for **{target_role}**, I highly recommend building: **{proj['title']}** ({proj['difficulty']}). "
                f"This project uses **{techs}** and helps bridge your skill gaps. "
                f"I've added detailed implementation milestones under your 'Project Recommendations' tab!"
            )
        else:
            return "To boost your profile, try building multi-tier applications or deploying backend containers using Git and Docker."
            
    # 3. Topic: Salary / Package / Placed
    if any(word in query_lower for word in ["salary", "package", "lpa", "earning", "placement", "predict", "money"]):
        return (
            f"Based on your credentials (CGPA, projects, internships), your predicted placement package for a **{target_role}** "
            f"role is **₹{salary['low']}L - ₹{salary['high']}L LPA**, with a median of **₹{salary['median']}L LPA**. "
            f"To push towards the higher range, consider completing your missing certifications."
        )
        
    # 4. Topic: Interview / Mock / HR
    if any(word in query_lower for word in ["interview", "mock", "question", "hr", "behavioral", "prep", "ready"]):
        return (
            f"Your current Interview Readiness score is **{interview_score}%**. "
            f"I recommend clicking on the **'Mock HR Interview'** tab to practice questions. "
            f"I can grade your answers dynamically using the STAR methodology!"
        )
        
    # 5. Topic: Certifications / Target
    if any(word in query_lower for word in ["certify", "certification", "credential", "exam", "course"]):
        certs = candidate_profile.get("cert_recommendations", [])
        if certs:
            cert_list = ", ".join([c["name"] for c in certs[:2]])
            return (
                f"To boost your resume filters, I recommend registering for: **{cert_list}**. "
                f"You can find official registration links in the 'Career & Credentials' tab on your dashboard."
            )
        else:
            return "Professional certifications from AWS, Microsoft, CompTIA, or Google Cloud add substantial credibility to your resume."
            
    # 6. Default Fallback
    return (
        f"Hi! I am your CareerForge AI coach. You are analyzing your resume for a **{target_role}** role. "
        f"You can ask me questions like: 'How do I learn my missing skills?', 'What project should I build?', "
        f"'What is my predicted salary?', or 'How can I prepare for interviews?'"
    )

