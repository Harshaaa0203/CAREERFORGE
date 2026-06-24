def get_skill_resources():
    """Returns a dictionary mapping skills to recommended courses, resources, and certifications."""
    return {
        # Programming Languages
        "python": {
            "course": "Python for Everybody Specialization (Coursera / University of Michigan)",
            "certification": "PCEP – Certified Entry-Level Python Programmer",
            "project": "Develop a multi-threaded web scraper or an automation script for local files.",
            "link": "https://www.coursera.org/specializations/python"
        },
        "java": {
            "course": "Java Programming Masterclass (Udemy by Tim Buchalka)",
            "certification": "Oracle Certified Associate (OCA) Java Programmer",
            "project": "Build an inventory management CLI app using Java Collections and OOP principles.",
            "link": "https://www.udemy.com/course/java-the-complete-java-developer-course/"
        },
        "javascript": {
            "course": "The Complete JavaScript Course 2026 (Udemy by Jonas Schmedtmann)",
            "certification": "OpenJS Node.js Application Developer (LFW211)",
            "project": "Create a rich dynamic dashboard utilizing async APIs and DOM manipulation.",
            "link": "https://javascript.info/"
        },
        "typescript": {
            "course": "Understanding TypeScript (Udemy by Maximilian Schwarzmüller)",
            "certification": "Microsoft Certified: Power Platform Developer",
            "project": "Refactor a JavaScript project into a strictly-typed Node.js script or component.",
            "link": "https://www.typescriptlang.org/docs/"
        },
        "c++": {
            "course": "Beginning C++ Programming - From Beginner to Advanced (Udemy)",
            "certification": "C++ Certified Associate Programmer (CPA)",
            "project": "Implement standard data structures (BST, AVL, Graphs) and algorithms from scratch.",
            "link": "https://www.learncpp.com/"
        },
        "sql": {
            "course": "SQL BootCamp: Go from Zero to Hero (Udemy)",
            "certification": "Oracle Database SQL Certified Associate",
            "project": "Create a database schema for an e-commerce shop, write complex joins and subqueries.",
            "link": "https://www.khanacademy.org/computing/computer-programming/sql"
        },
        
        # Machine Learning / AI
        "machine learning": {
            "course": "Machine Learning Specialization (Coursera by Andrew Ng / DeepLearning.AI)",
            "certification": "Professional Data Engineer (Google Cloud)",
            "project": "Build a predictive model using Linear Regression, Random Forest, and evaluate metrics.",
            "link": "https://www.coursera.org/specializations/machine-learning-introduction"
        },
        "deep learning": {
            "course": "Deep Learning Specialization (Coursera by Andrew Ng)",
            "certification": "TensorFlow Developer Certificate",
            "project": "Train an Image Classification CNN or a Time Series LSTM model from scratch.",
            "link": "https://www.deeplearning.ai/program/deep-learning-specialization/"
        },
        "tensorflow": {
            "course": "Introduction to TensorFlow for AI, Machine Learning, and Deep Learning (Coursera)",
            "certification": "Google TensorFlow Developer Certification",
            "project": "Build and train a classification neural network on a public dataset (e.g. Fashion-MNIST).",
            "link": "https://www.tensorflow.org/tutorials"
        },
        "pytorch": {
            "course": "Deep Learning with PyTorch: Zero to GANs (Jovian)",
            "certification": "Meta AI PyTorch Certification path",
            "project": "Implement a custom Neural Network model class in PyTorch, write custom training loop.",
            "link": "https://pytorch.org/tutorials/"
        },
        "nlp": {
            "course": "Natural Language Processing Specialization (Coursera by DeepLearning.AI)",
            "certification": "Hugging Face NLP Certification (Free course)",
            "project": "Build a text-sentiment classifier or a resume keyword parsing regex engine.",
            "link": "https://huggingface.co/learn/nlp-course/chapter1/1"
        },
        "scikit-learn": {
            "course": "Machine Learning with Python (Scikit-Learn docs & freeCodeCamp)",
            "certification": "Scikit-Learn Machine Learning Associate (via Kaggle)",
            "project": "Create a pipeline for feature scaling, imputation, and classification using RandomForest.",
            "link": "https://scikit-learn.org/stable/tutorial/index.html"
        },
        "transformers": {
            "course": "Hugging Face NLP Course / Generative AI Path",
            "certification": "Hugging Face Certified Practitioner",
            "project": "Fine-tune a BERT model for text classification or text summarization.",
            "link": "https://huggingface.co/docs/transformers/index"
        },
        
        # Web Development
        "react": {
            "course": "React - The Complete Guide (Udemy by Academind)",
            "certification": "Meta Front-End Developer Professional Certificate (Coursera)",
            "project": "Build a responsive dashboard using React hooks, routing, and context API.",
            "link": "https://react.dev/"
        },
        "node.js": {
            "course": "Node.js, Express, MongoDB & More (Udemy by Jonas Schmedtmann)",
            "certification": "OpenJS Node.js Application Developer (LFW211)",
            "project": "Develop a RESTful API backend with authentication, database schemas, and input validation.",
            "link": "https://nodejs.org/en/docs/"
        },
        "mongodb": {
            "course": "MongoDB Basics (MongoDB University)",
            "certification": "MongoDB Certified Developer Associate",
            "project": "Set up a database for a blogging platform with nested schema models (comments, users).",
            "link": "https://learn.mongodb.com/"
        },
        "postgresql": {
            "course": "SQL and PostgreSQL: The Complete Developer's Guide (Udemy)",
            "certification": "PostgreSQL Associate Certification",
            "project": "Design database constraints, triggers, and indices for high performance query execution.",
            "link": "https://www.postgresqltutorial.com/"
        },
        
        # Cloud / DevOps
        "docker": {
            "course": "Docker Technologies for DevOps and Developers (Udemy)",
            "certification": "Docker Certified Associate (DCA)",
            "project": "Containerize a Flask/Node.js web application and connect it with a database container.",
            "link": "https://docs.docker.com/get-started/"
        },
        "kubernetes": {
            "course": "Certified Kubernetes Administrator (CKA) (Udemy by Mumshad Mannambeth)",
            "certification": "Certified Kubernetes Administrator (CKA)",
            "project": "Deploy a multi-tier web application using Kubernetes Pods, Services, and Deployments.",
            "link": "https://kubernetes.io/docs/tutorials/"
        },
        "aws": {
            "course": "AWS Certified Solutions Architect Associate (Udemy by Stephane Maarek)",
            "certification": "AWS Certified Solutions Architect - Associate",
            "project": "Host a static website on S3, deploy backend on EC2, and configure an RDS database.",
            "link": "https://aws.amazon.com/training/"
        },
        
        # Cybersecurity
        "network security": {
            "course": "CompTIA Security+ Exam Prep (Udemy by Jason Dion)",
            "certification": "CompTIA Security+",
            "project": "Configure a local virtual network with distinct subnets, firewall rules, and entry points.",
            "link": "https://www.comptia.org/certifications/security"
        },
        "penetration testing": {
            "course": "Ethical Hacking: Penetration Testing (Pluralsight / TCM Security)",
            "certification": "Certified Ethical Hacker (CEH) / PNPT",
            "project": "Set up a virtual lab with Metasploitable, identify vulnerabilities, and perform exploits.",
            "link": "https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/"
        }
    }

def get_role_details(target_role):
    """Returns general profile details, default timeline phases, and interview strategies for a role."""
    roles_info = {
        "AI Engineer": {
            "timeline": [
                {"phase": "Phase 1: Foundations (Week 1-2)", "focus": "Brush up Python, learn PyTorch/TensorFlow basics, study core Linear Algebra & Probability.", "checklist": ["Complete NumPy/Pandas tutorials", "Implement basic feedforward neural network"]},
                {"phase": "Phase 2: NLP & CV Concepts (Week 3-4)", "focus": "Deep dive into spaCy/NLTK, word embeddings, Transformers, and Hugging Face pipelines.", "checklist": ["Complete Hugging Face course Chapter 1-3", "Build a text similarity parser"]},
                {"phase": "Phase 3: LLM & GenAI Apps (Week 5-6)", "focus": "Learn LangChain, OpenAI APIs, Vector Databases (Chroma/Pinecone), RAG pipeline implementation.", "checklist": ["Implement RAG chatbot using LangChain", "Upload project to GitHub"]},
                {"phase": "Phase 4: Optimization & Prep (Week 7-8)", "focus": "Model quantization, API deployment (FastAPI/Docker), study systems design for AI and interview FAQs.", "checklist": ["Deploy AI model via Docker container", "Review LLM fine-tuning interview Qs"]}
            ],
            "interview_strategy": "Be ready for math questions (activation functions, gradients), hands-on coding of neural network layers in PyTorch, and designing a RAG system at scale.",
            "certifications": ["Google Cloud Professional Machine Learning Engineer", "TensorFlow Developer Certificate"]
        },
        "Data Scientist": {
            "timeline": [
                {"phase": "Phase 1: Advanced Statistics (Week 1-2)", "focus": "Study probability distributions, hypothesis testing, A/B testing, and Python statistics libraries.", "checklist": ["Write statistical scripts using SciPy", "Solve 50 SQL queries on LeetCode"]},
                {"phase": "Phase 2: ML Algorithms (Week 3-4)", "focus": "Learn regression, decision trees, clustering, and Scikit-Learn hyperparameter tuning.", "checklist": ["Build regression model on housing dataset", "Apply PCA for feature reduction"]},
                {"phase": "Phase 3: Visualization & Dashboards (Week 5-6)", "focus": "Master Tableau/PowerBI or Plotly/Seaborn for storytelling, data cleaning pipelines.", "checklist": ["Build a comprehensive Tableau dashboard", "Prepare dataset report using Pandas"]},
                {"phase": "Phase 4: Business Case Study & Prep (Week 7-8)", "focus": "Practice ML system design, feature engineering strategies, SQL optimization, and mock case studies.", "checklist": ["Practice 10 mock business case studies", "Optimize model inference speed"]}
            ],
            "interview_strategy": "Expect intense SQL questions (joins, window functions), ML model trade-offs (bias-variance, precision-recall), and business scenario analytics problems.",
            "certifications": ["Microsoft Certified: Power BI Data Analyst", "IBM Data Science Professional Certificate"]
        },
        "Software Developer": {
            "timeline": [
                {"phase": "Phase 1: Data Structures & Algorithms (Week 1-2)", "focus": "Practice arrays, linked lists, stacks, queues, hash maps, sorting, and time complexity analyses.", "checklist": ["Solve 30 Easy DSA problems on LeetCode", "Analyze Big-O time of code snippets"]},
                {"phase": "Phase 2: Advanced DSA & OOP (Week 3-4)", "focus": "Master trees, graphs, recursion, dynamic programming, and Object-Oriented Design patterns.", "checklist": ["Solve 20 Medium DSA problems", "Implement 3 structural design patterns"]},
                {"phase": "Phase 3: Databases & Tooling (Week 5-6)", "focus": "Learn SQL optimization, indexing, Git version control, Unit Testing, and CLI basics.", "checklist": ["Write unit tests for a CRUD project", "Manage feature branches in Git"]},
                {"phase": "Phase 4: Mock Coding & System Design (Week 7-8)", "focus": "Practice interview coding under time pressure, review basic operating systems (threads, memory) and network protocols.", "checklist": ["Complete 3 mock interviews on Pramp", "Review SOLID design principles"]}
            ],
            "interview_strategy": "Prepare for DSA live coding rounds (LeetCode standard), Object-Oriented Design (OOD) scenarios (like parking lot system), and standard software engineering principles.",
            "certifications": ["AWS Certified Cloud Practitioner", "Oracle Certified Professional Programmer"]
        },
        "Full Stack Developer": {
            "timeline": [
                {"phase": "Phase 1: Advanced Frontend (Week 1-2)", "focus": "Master React Hooks, Context API, state management, responsive designs, and CSS Frameworks.", "checklist": ["Build a responsive portfolio page", "Implement authentication state in React"]},
                {"phase": "Phase 2: Backend Development (Week 3-4)", "focus": "Learn Node.js, Express routes, REST APIs, JSON web tokens (JWT), and server-side logic.", "checklist": ["Create a secure login API route", "Implement CORS policies"]},
                {"phase": "Phase 3: Database & Integration (Week 5-6)", "focus": "Connect backend to MySQL/MongoDB, design schemas, handle migrations, and verify API responses.", "checklist": ["Connect DB, execute mock CRUD actions", "Integrate front-end form with backend API"]},
                {"phase": "Phase 4: Deployment & DevOps (Week 7-8)", "focus": "Learn Docker basics, host server on AWS/Render/Vercel, write API docs, and practice system design.", "checklist": ["Deploy React + Node application to cloud", "Add Postman collection for API endpoints"]}
            ],
            "interview_strategy": "Focus on system design (scalable architectures), performance optimization (caching, database indexing), and front-end coding assessments.",
            "certifications": ["AWS Certified Solutions Architect", "Meta Full-End/Back-End Developer Certificates"]
        },
        "Data Analyst": {
            "timeline": [
                {"phase": "Phase 1: Excel & SQL Foundations (Week 1-2)", "focus": "Learn advanced Excel (Pivot tables, VLOOKUPs) and database queries (GROUP BY, Joins, subqueries).", "checklist": ["Solve 40 SQL problems on HackerRank", "Perform data aggregation on Excel"]},
                {"phase": "Phase 2: BI Dashboards (Week 3-4)", "focus": "Master Tableau or Power BI. Learn how to import data, model relationships, and build visual dashboards.", "checklist": ["Build a sales tracking dashboard", "Publish dashboard online for peer review"]},
                {"phase": "Phase 3: Python Data Analytics (Week 5-6)", "focus": "Learn Pandas, NumPy, and Matplotlib/Seaborn for automated data cleaning and plotting.", "checklist": ["Write a Python script to clean a CSV file", "Plot correlations between customer features"]},
                {"phase": "Phase 4: Portfolio & Presentation (Week 7-8)", "focus": "Compile dashboard screenshots, practice presenting data insights to non-technical audiences, review metric formulas.", "checklist": ["Upload analysis case study to GitHub", "Practice mock presentation of dashboard"]}
            ],
            "interview_strategy": "Be ready to write SQL queries on a whiteboard, explain metric definitions, and talk through how you translate data patterns into actionable business decisions.",
            "certifications": ["Google Data Analytics Professional Certificate", "Microsoft Certified: Power BI Data Analyst"]
        },
        "Machine Learning Engineer": {
            "timeline": [
                {"phase": "Phase 1: Math & ML Models (Week 1-2)", "focus": "Review calculus, statistics, linear algebra, and classic ML algorithm mechanics (SVM, RF, Gradient Boosting).", "checklist": ["Implement gradient descent from scratch", "Train and compare 3 models in Scikit-Learn"]},
                {"phase": "Phase 2: Deep Learning & Frameworks (Week 3-4)", "focus": "Master PyTorch/TensorFlow, model training loops, regularization techniques, and hyperparameter tuning.", "checklist": ["Create a neural network with dropout layers", "Perform grid search tuning on models"]},
                {"phase": "Phase 3: MLOps & Pipelines (Week 5-6)", "focus": "Learn feature stores, model tracking (MLflow), pipeline creation, and Docker orchestration.", "checklist": ["Track hyperparameters with MLflow", "Dockerize an ML inference API service"]},
                {"phase": "Phase 4: Cloud Deployment & Scaling (Week 7-8)", "focus": "Deploy models to AWS SageMaker / GCP AI Platform, monitor drift, and review ML system design concepts.", "checklist": ["Deploy model with endpoints on AWS", "Study predictive latency optimizations"]}
            ],
            "interview_strategy": "You will face ML System Design questions (e.g. recommend system for YouTube), math theory questions, and programming questions about pipelines and tensor shapes.",
            "certifications": ["Google Cloud Professional ML Engineer", "AWS Certified Machine Learning - Specialty"]
        },
        "Cybersecurity Analyst": {
            "timeline": [
                {"phase": "Phase 1: Networks & Protocols (Week 1-2)", "focus": "Study TCP/IP stack, DNS, subnets, routing, and command-line network diagnostic commands (ping, nslookup).", "checklist": ["Diagram a corporate subnet structure", "Perform port scanning inside a VM lab"]},
                {"phase": "Phase 2: Security & Threat Vector (Week 3-4)", "focus": "Learn about firewalls, intrusion detection systems, malware categories, and security policies.", "checklist": ["Write a firewall iptables config", "Analyze network packets in Wireshark"]},
                {"phase": "Phase 3: Vulnerabilities & Auditing (Week 5-6)", "focus": "Learn to run Nmap, Nessus scans, analyze log files (Linux/Apache), and identify security gaps.", "checklist": ["Run Nmap scanning on a host VM", "Locate suspicious IP addresses in server log"]},
                {"phase": "Phase 4: SOC Procedures & Incident Response (Week 7-8)", "focus": "Review standard incident response guidelines, threat modeling, study OWASP Top 10 web vulnerabilities.", "checklist": ["Document a mock incident response flow", "Complete OWASP Juice Shop lab exercises"]}
            ],
            "interview_strategy": "Expect questions on how you would investigate a suspicious server alert, how standard network protocols work, and details on cryptographic handshakes.",
            "certifications": ["CompTIA Security+", "Certified Ethical Hacker (CEH)"]
        },
        "Java Developer": {
            "timeline": [
                {"phase": "Phase 1: Java & OOP Foundations (Week 1-2)", "focus": "Review Java Collections, Exceptions, Generics, Stream API, and OOP core pillars.", "checklist": ["Solve 20 Java-based DSA problems", "Write a Java console app with multithreading"]},
                {"phase": "Phase 2: Database & ORM (Week 3-4)", "focus": "Learn SQL basics, JDBC connections, JPA, and Hibernate configuration.", "checklist": ["Set up a local database connection", "Configure Hibernate entity relationships"]},
                {"phase": "Phase 3: Spring Framework & Spring Boot (Week 5-6)", "focus": "Study dependency injection, Spring MVC, REST controllers, Spring Data JPA, and security concepts.", "checklist": ["Build a complete REST API using Spring Boot", "Secure API endpoints with simple config"]},
                {"phase": "Phase 4: Testing & Deployment (Week 7-8)", "focus": "Write JUnit tests, use Maven/Gradle build tools, build jar files, and deploy to container environments.", "checklist": ["Write 15 JUnit tests with Mockito mock object", "Build Docker image of Spring Boot app"]}
            ],
            "interview_strategy": "Prepare for JVM internals (Garbage Collection, Memory model), design patterns in Java, Spring Boot configurations, and SQL performance tuning questions.",
            "certifications": ["Oracle Certified Professional: Java SE Developer", "Spring Professional Certification"]
        }
    }
    
    # Fallback default configuration
    default_role = {
        "timeline": [
            {"phase": "Phase 1: Skill Foundations (Week 1-2)", "focus": "Learn fundamental programming languages, basic syntax, and documentation setup.", "checklist": ["Complete basic tutorial online", "Write hello-world and sample scripts"]},
            {"phase": "Phase 2: Tools & Frameworks (Week 3-4)", "focus": "Set up developer environment, learn git commands, and explore relevant core frameworks.", "checklist": ["Set up Git repositories", "Write a basic functional component"]},
            {"phase": "Phase 3: Building Core Projects (Week 5-6)", "focus": "Synthesize learning by building a complete working model, site, or backend utility.", "checklist": ["Implement key functional features", "Publish prototype on GitHub"]},
            {"phase": "Phase 4: Interview & Portfolio (Week 7-8)", "focus": "Optimize performance, complete unit tests, practice behavioral questions, and polish resume details.", "checklist": ["Run system diagnostics checks", "Review typical interview questions"]}
        ],
        "interview_strategy": "Emphasize core programming skills, explain project choices, and demonstrate standard problem-solving methodologies.",
        "certifications": ["AWS Certified Cloud Practitioner"]
    }
    
    return roles_info.get(target_role, default_role)

def generate_personalized_roadmap(target_role, missing_skills):
    """
    Generate a complete personalized roadmap including learning resources, timelines, and strategies.
    """
    role_details = get_role_details(target_role)
    skill_resources = get_skill_resources()
    
    # 1. Map missing skills to specific learning actions
    mapped_skills_roadmap = []
    for skill in missing_skills:
        skill_lower = skill.lower()
        if skill_lower in skill_resources:
            info = skill_resources[skill_lower]
            mapped_skills_roadmap.append({
                "skill": skill,
                "course": info["course"],
                "certification": info["certification"],
                "project_idea": info["project"],
                "link": info["link"]
            })
        else:
            # Generic mapping for skills not explicitly in library
            mapped_skills_roadmap.append({
                "skill": skill,
                "course": f"Complete {skill} Guide / Crash Course (Available on Coursera / YouTube)",
                "certification": f"{skill} Certified Associate (Verify official vendor program)",
                "project_idea": f"Implement a functional application or library integrating {skill}.",
                "link": "https://www.google.com/search?q=" + skill.replace(' ', '+') + "+learning+course"
            })
            
    # 2. Inject missing skills recommendations directly into the timeline phases
    personalized_timeline = []
    for i, phase in enumerate(role_details["timeline"]):
        phase_copy = {
            "phase": phase["phase"],
            "focus": phase["focus"],
            "checklist": list(phase["checklist"])
        }
        
        # Inject skill gap recommendations based on phase index
        if i == 0 and len(mapped_skills_roadmap) > 0:
            # Inject fundamental syntax missing skills in Phase 1
            skills_to_add = [item["skill"] for item in mapped_skills_roadmap if item["skill"].lower() in ["python", "java", "javascript", "c++", "sql"]]
            if skills_to_add:
                phase_copy["focus"] += f" Prioritize learning syntax for missing basic skills: {', '.join(skills_to_add)}."
                for skill in skills_to_add[:2]:
                    phase_copy["checklist"].append(f"Complete intro tutorials on {skill}")
        elif i == 1 and len(mapped_skills_roadmap) > 1:
            # Inject intermediate libraries/concepts in Phase 2
            skills_to_add = [item["skill"] for item in mapped_skills_roadmap if item["skill"].lower() in ["react", "node.js", "scikit-learn", "numpy", "pandas", "statistics"]]
            if skills_to_add:
                phase_copy["focus"] += f" Master core libraries: {', '.join(skills_to_add)}."
                for skill in skills_to_add[:2]:
                    phase_copy["checklist"].append(f"Build mini module showcasing {skill}")
        elif i == 2 and len(mapped_skills_roadmap) > 0:
            # Inject building project ideas in Phase 3
            project_skills = [item for item in mapped_skills_roadmap if item["skill"].lower() not in ["python", "java", "javascript", "c++"]]
            if project_skills:
                phase_copy["focus"] += f" Build your project integrating: {', '.join([p['skill'] for p in project_skills[:2]])}."
                phase_copy["checklist"].append(f"Project Milestone: Integrate {project_skills[0]['skill']}")
                
        personalized_timeline.append(phase_copy)
        
    return {
        "target_role": target_role,
        "missing_skills_recommendations": mapped_skills_roadmap,
        "timeline": personalized_timeline,
        "interview_strategy": role_details["interview_strategy"],
        "recommended_certifications": role_details["certifications"]
    }

def get_cert_recommendations_with_links(target_role, missing_skills=None):
    """
    Returns certification recommendations with direct clickable hyperlinks.
    """
    # 1. Fetch general certifications for the target role
    role_details = get_role_details(target_role)
    certs = list(role_details.get("certifications", []))
    
    # 2. Append certifications corresponding to missing skills
    skill_resources = get_skill_resources()
    if missing_skills:
        for skill in missing_skills:
            skill_lower = skill.lower().strip()
            if skill_lower in skill_resources:
                cert_name = skill_resources[skill_lower].get("certification")
                if cert_name and cert_name not in certs:
                    certs.append(cert_name)
                    
    # Map certification names to registration links
    cert_links = {
        "Google Cloud Professional Machine Learning Engineer": "https://cloud.google.com/learn/certification/machine-learning-engineer",
        "TensorFlow Developer Certificate": "https://www.coursera.org/professional-certificates/tensorflow-in-practice",
        "Professional Data Engineer (Google Cloud)": "https://cloud.google.com/learn/certification/data-engineer",
        "Microsoft Certified: Power BI Data Analyst": "https://learn.microsoft.com/en-us/credentials/certifications/power-bi-data-analyst-associate/",
        "IBM Data Science Professional Certificate": "https://www.coursera.org/professional-certificates/ibm-data-science",
        "AWS Certified Cloud Practitioner": "https://aws.amazon.com/certification/certified-cloud-practitioner/",
        "Oracle Certified Professional Programmer": "https://education.oracle.com/java-se-17-developer/pexam_1Z0-829",
        "Oracle Certified Associate (OCA) Java Programmer": "https://education.oracle.com/java-se-17-developer/pexam_1Z0-829",
        "AWS Certified Solutions Architect": "https://aws.amazon.com/certification/certified-solutions-architect-associate/",
        "AWS Certified Solutions Architect - Associate": "https://aws.amazon.com/certification/certified-solutions-architect-associate/",
        "Meta Front-End Developer Professional Certificate (Coursera)": "https://www.coursera.org/professional-certificates/meta-front-end-developer",
        "Meta Back-End Developer Professional Certificate (Coursera)": "https://www.coursera.org/professional-certificates/meta-back-end-developer",
        "Meta Front-End/Back-End Developer Certificates": "https://www.coursera.org/professional-certificates/meta-front-end-developer",
        "Google Data Analytics Professional Certificate": "https://www.coursera.org/professional-certificates/google-data-analytics",
        "AWS Certified Machine Learning - Specialty": "https://aws.amazon.com/certification/certified-machine-learning-specialty/",
        "CompTIA Security+": "https://www.comptia.org/certifications/security",
        "Certified Ethical Hacker (CEH)": "https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/",
        "Oracle Certified Professional: Java SE Developer": "https://education.oracle.com/java-se-17-developer/pexam_1Z0-829",
        "Spring Professional Certification": "https://spring.io/learning",
        "PCEP – Certified Entry-Level Python Programmer": "https://pythoninstitute.org/pcep",
        "OpenJS Node.js Application Developer (LFW211)": "https://training.linuxfoundation.org/certification/jsnad/",
        "C++ Certified Associate Programmer (CPA)": "https://cppinstitute.org/cpa-c-certified-associate-programmer",
        "Oracle Database SQL Certified Associate": "https://education.oracle.com/oracle-database-sql/pexam_1Z0-071",
        "Docker Certified Associate (DCA)": "https://training.linuxfoundation.org/certification/docker-certified-associate/",
        "Certified Kubernetes Administrator (CKA)": "https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/",
        "MongoDB Certified Developer Associate": "https://learn.mongodb.com/pages/certification",
        "PostgreSQL Associate Certification": "https://www.postgresql.org/about/"
    }
    
    result = []
    for cert in certs:
        link = cert_links.get(cert, f"https://www.google.com/search?q={cert.replace(' ', '+')}+certification")
        result.append({
            "name": cert,
            "link": link
        })
        
    return result

def get_detailed_project_recommendations(target_role):
    """
    Returns 2 structured high-impact project suggestions for the selected job role.
    """
    catalog = {
        "AI Engineer": [
            {
                "title": "LLM-Powered Document Semantic Search Engine",
                "difficulty": "Advanced",
                "time_estimate": "3-4 Weeks",
                "tech_stack": ["Python", "LangChain", "OpenAI API / Llama-3", "ChromaDB / Pinecone", "Streamlit"],
                "description": "Build a Retrieval-Augmented Generation (RAG) system that reads PDF/Word files, performs text chunking and creates vector embeddings, indexes them in a vector database, and lets users ask questions with semantic search context.",
                "steps": [
                    "Extract and clean text from PDFs/documents.",
                    "Generate vector embeddings using OpenAI or Hugging Face models.",
                    "Store and index embeddings in ChromaDB or Pinecone vector database.",
                    "Write LangChain chains to fetch relevant chunks and feed them as context to an LLM query.",
                    "Build a dynamic web interface in Streamlit to upload files and chat with documents."
                ],
                "reference_link": "https://github.com/langchain-ai/langchain"
            },
            {
                "title": "Fine-Tuning BERT for Sentiment Analysis",
                "difficulty": "Intermediate",
                "time_estimate": "2 Weeks",
                "tech_stack": ["Python", "PyTorch", "Hugging Face Transformers", "Datasets", "Scikit-Learn"],
                "description": "Fine-tune a pre-trained BERT transformer model on an IMDb movie review dataset for positive/negative sentiment classification. Implement evaluation metrics (Accuracy, F1-Score).",
                "steps": [
                    "Load and tokenize the IMDb movie reviews dataset using Hugging Face tokenizers.",
                    "Load a pre-trained BERT model and configure a classification head.",
                    "Set up a PyTorch training loop or use Hugging Face Trainer API.",
                    "Track training metrics, evaluate loss curves, and analyze F1 scores.",
                    "Package the fine-tuned model for local inference queries."
                ],
                "reference_link": "https://huggingface.co/docs/transformers/training"
            }
        ],
        "Data Scientist": [
            {
                "title": "Predictive Customer Churn Analysis Pipeline",
                "difficulty": "Intermediate",
                "time_estimate": "2 Weeks",
                "tech_stack": ["Python", "Pandas", "Scikit-Learn", "XGBoost", "Matplotlib", "Seaborn"],
                "description": "Build an end-to-end classification pipeline to predict customer churn. Includes feature engineering, handling class imbalance (SMOTE), training ensemble models, and building an interactive dashboard.",
                "steps": [
                    "Perform exploratory data analysis (EDA) to understand churn correlates.",
                    "Clean data, handle missing values, and encode categorical variables.",
                    "Apply SMOTE or random oversampling to handle class imbalance.",
                    "Train Logistic Regression, Random Forest, and XGBoost models, tuning hyperparameters via GridSearch.",
                    "Evaluate using Precision-Recall curves, ROC-AUC, and feature importances."
                ],
                "reference_link": "https://scikit-learn.org/stable/supervised_learning.html"
            },
            {
                "title": "A/B Testing Simulator & Analysis Tool",
                "difficulty": "Intermediate",
                "time_estimate": "1-2 Weeks",
                "tech_stack": ["Python", "SciPy", "Statsmodels", "Streamlit", "Plotly"],
                "description": "Develop a web application that simulates A/B test datasets, conducts statistical hypothesis tests (t-test, chi-square), computes statistical power and minimum sample size, and visualizes conversion metrics.",
                "steps": [
                    "Generate control and variation conversion datasets based on user inputs.",
                    "Perform t-tests for continuous metrics and Chi-Square tests for binomial conversion rates.",
                    "Calculate confidence intervals, p-values, and statistical power metrics.",
                    "Implement a sample size calculator using effect size formulas.",
                    "Build a clean Streamlit interface with interactive Plotly conversion graphs."
                ],
                "reference_link": "https://docs.scipy.org/doc/scipy/reference/stats.html"
            }
        ],
        "Software Developer": [
            {
                "title": "Multi-Threaded HTTP Web Server from Scratch",
                "difficulty": "Advanced",
                "time_estimate": "3 Weeks",
                "tech_stack": ["C++ / Java", "Socket Programming", "Multithreading", "POSIX Threads"],
                "description": "Build a high-performance HTTP web server from scratch without external frameworks. Implement socket listening, thread pools for handling concurrent requests, and basic HTTP parser for serving static files.",
                "steps": [
                    "Initialize TCP sockets and bind to local ports to listen for connections.",
                    "Implement a parsing engine to extract HTTP request verbs, headers, and paths.",
                    "Design a thread pool using worker threads and task queues to handle multiple clients concurrently.",
                    "Form HTTP responses (HTML, images, CSS) with correct response headers.",
                    "Handle edge cases, invalid routing, and concurrent socket timeouts."
                ],
                "reference_link": "https://beej.us/guide/bgnet/"
            },
            {
                "title": "Distributed Key-Value Store",
                "difficulty": "Advanced",
                "time_estimate": "4 Weeks",
                "tech_stack": ["Python / Go", "gRPC", "Raft Consensus", "Protocol Buffers"],
                "description": "Build a basic replica-consistent distributed key-value store using the Raft consensus algorithm, with data persistence and crash recovery.",
                "steps": [
                    "Define gRPC APIs for key-value storage endpoints (GET, SET).",
                    "Implement leader election and heartbeat loops according to Raft specifications.",
                    "Create log replication mechanics between node replicas.",
                    "Build a persistent log file system to recover state after server crashes.",
                    "Perform network partition testing to evaluate consensus consistency."
                ],
                "reference_link": "https://raft.github.io/"
            }
        ],
        "Full Stack Developer": [
            {
                "title": "Real-Time Collaborative Project Management Tool",
                "difficulty": "Advanced",
                "time_estimate": "3-4 Weeks",
                "tech_stack": ["React", "Node.js", "Express", "MongoDB", "Socket.io", "TailwindCSS"],
                "description": "Build a Trello-like project management dashboard where users can create tasks, drag/drop columns, invite team members, and see updates in real-time using WebSockets.",
                "steps": [
                    "Set up a Node.js and Express backend with JWT user authentication.",
                    "Define Mongo schemas for boards, columns, tasks, and users.",
                    "Integrate Socket.io in both client and server to synchronize workspace modifications instantly.",
                    "Create a React drag-and-drop workspace using react-beautiful-dnd or similar library.",
                    "Deploy both frontend and backend to cloud providers (e.g. Vercel, Render) with environment configurations."
                ],
                "reference_link": "https://socket.io/"
            },
            {
                "title": "SaaS E-Commerce Platform with Stripe API",
                "difficulty": "Intermediate",
                "time_estimate": "3 Weeks",
                "tech_stack": ["Next.js", "PostgreSQL", "Prisma ORM", "Stripe API", "TailwindCSS"],
                "description": "Build a full-stack e-commerce marketplace featuring product catalog search, shopping cart state management, checkout with Stripe payment integration, and a customer dashboard for order history.",
                "steps": [
                    "Design relational database schemas in PostgreSQL with Prisma ORM mappings.",
                    "Create Next.js Server Actions or API routes for product queries and user sessions.",
                    "Build checkout flows using the Stripe Node.js SDK and webhook handlers.",
                    "Design responsive layouts for shopping carts, product search filters, and checkout states.",
                    "Configure admin dashboard tables to track payments, deliveries, and stock counts."
                ],
                "reference_link": "https://stripe.com/docs/api"
            }
        ],
        "Data Analyst": [
            {
                "title": "Global Sales Performance Dashboard",
                "difficulty": "Beginner",
                "time_estimate": "1 Week",
                "tech_stack": ["SQL", "Tableau / Power BI", "Excel", "ETL"],
                "description": "Import dirty sales records, clean them using Excel/SQL, perform cohort analysis and revenue trend forecasting, and build an interactive 5-page executive dashboard with drill-down filters.",
                "steps": [
                    "Clean raw sales records, handling dates, invalid characters, and currency mismatches.",
                    "Write SQL queries to join customer, product, and region tables and aggregate monthly totals.",
                    "Perform cohort retention analysis using SQL window functions.",
                    "Import finalized queries into Tableau or Power BI and configure data modeling keys.",
                    "Design interactive executive reports containing regional maps, trend lines, and filtering controls."
                ],
                "reference_link": "https://public.tableau.com/"
            },
            {
                "title": "Web Scraper & ETL Analytics Pipeline",
                "difficulty": "Intermediate",
                "time_estimate": "2 Weeks",
                "tech_stack": ["Python", "BeautifulSoup / Scrapy", "SQLite", "Plotly Dash"],
                "description": "Extract real-estate pricing listings from websites, transform raw text, geocode address data, load into a local SQLite database, and run automated cron scripts to refresh data charts weekly.",
                "steps": [
                    "Develop BeautifulSoup scrapers, handling pagination, request headers, and rate limits.",
                    "Clean listing text, parsing integers for prices, areas, and bedrooms.",
                    "Geocode coordinates based on textual addresses using Nominatim API.",
                    "Load cleaned tables into a local SQLite database.",
                    "Build an interactive Plotly dashboard showing price distribution by neighborhood."
                ],
                "reference_link": "https://beautiful-soup-4.readthedocs.io/en/latest/"
            }
        ],
        "Machine Learning Engineer": [
            {
                "title": "Scalable Real-time ML Inference Service with FastAPI & Docker",
                "difficulty": "Intermediate",
                "time_estimate": "2 Weeks",
                "tech_stack": ["Python", "FastAPI", "Docker", "MLflow", "Scikit-Learn"],
                "description": "Deploy a classification model behind a REST API. Write custom unit tests, implement request validation, package the model using Docker, track experiments with MLflow, and benchmark request throughput.",
                "steps": [
                    "Train a Random Forest model using Scikit-Learn and track parameters/metrics via MLflow.",
                    "Build a FastAPI application exposing endpoint inputs validated with Pydantic schemas.",
                    "Write automated test scripts using PyTest to check inference validation.",
                    "Package the application inside a multi-stage Docker container.",
                    "Benchmark performance and latency using Locust or ab (Apache Benchmark)."
                ],
                "reference_link": "https://fastapi.tiangolo.com/"
            },
            {
                "title": "End-to-End Object Detection Pipeline with YOLO",
                "difficulty": "Advanced",
                "time_estimate": "3 Weeks",
                "tech_stack": ["Python", "PyTorch", "OpenCV", "Roboflow", "YOLOv8"],
                "description": "Train a custom object detection model on a labeled dataset (e.g. traffic signs, PPE). Perform data augmentation, hyperparameter tuning, model validation, and run real-time inference on video streams.",
                "steps": [
                    "Collect and annotate custom images using Roboflow interfaces.",
                    "Configure YOLOv8 training pipelines, tuning learning rates and batch sizes.",
                    "Validate models using precision, recall, and mAP@0.5 score curves.",
                    "Write OpenCV scripts to capture video streams, apply bounding boxes, and draw classification labels in real-time.",
                    "Optimize inference speed by exporting weights to ONNX or TensorRT models."
                ],
                "reference_link": "https://github.com/ultralytics/ultralytics"
            }
        ],
        "Cybersecurity Analyst": [
            {
                "title": "Automated Network Vulnerability Scanner & Reporter",
                "difficulty": "Intermediate",
                "time_estimate": "2 Weeks",
                "tech_stack": ["Python", "Nmap API", "Shodan API", "ReportLab"],
                "description": "Design a script that automatically scans local subnets, checks for open ports and services, queries Shodan for known CVEs, and generates an executive PDF vulnerability assessment report.",
                "steps": [
                    "Integrate python-nmap to scan host ports and discover running services.",
                    "Query Shodan API with service signatures to locate vulnerabilities and CVE numbers.",
                    "Rank discovered items by severity (CVSS Score ratings).",
                    "Format findings using Python ReportLab library, creating structured PDF report pages.",
                    "Add mitigation strategies for common weaknesses (e.g. open ports, outdated servers)."
                ],
                "reference_link": "https://nmap.org/book/man-port-scanning-techniques.html"
            },
            {
                "title": "Intrusion Detection Log Parser & Alerting System",
                "difficulty": "Intermediate",
                "time_estimate": "2 Weeks",
                "tech_stack": ["Python", "Linux Logs", "Elasticsearch", "Kibana (ELK)", "SMTP"],
                "description": "Build a pipeline to parse Linux syslog and auth.log files in real-time. Write custom regex rules to detect brute-force SSH attacks or unauthorized sudo attempts, trigger email alerts, and visualize logins in Kibana.",
                "steps": [
                    "Configure Logstash or write a custom Python watchdog script to parse auth.log files.",
                    "Apply regex filters to detect repetitive failed login attempts or sudo anomalies.",
                    "Index parsed log documents into an Elasticsearch cluster.",
                    "Write alerting logic that fires email notifications when specific thresholds are breached.",
                    "Create Kibana maps and gauges tracking user login distributions."
                ],
                "reference_link": "https://www.elastic.co/what-is/elk-stack"
            }
        ],
        "Java Developer": [
            {
                "title": "Cloud-Native Microservices E-Commerce Backend",
                "difficulty": "Advanced",
                "time_estimate": "4 Weeks",
                "tech_stack": ["Java", "Spring Boot", "Spring Cloud", "PostgreSQL", "Docker", "Eureka"],
                "description": "Build a backend microservices system featuring an API gateway, service discovery (Eureka), configuration server, and independent services for products, orders, and users.",
                "steps": [
                    "Set up independent Spring Boot applications for User, Product, and Order services.",
                    "Configure Eureka Server for dynamic registry and discovery of microservices.",
                    "Implement Spring Cloud Gateway for centralized routing and JWT security filters.",
                    "Enable inter-service communication using Feign clients and configure resilience with Circuit Breakers.",
                    "Dockerize each service and coordinate startup using docker-compose."
                ],
                "reference_link": "https://spring.io/projects/spring-cloud"
            },
            {
                "title": "Enterprise Library Management System with JUnit & Mockito",
                "difficulty": "Intermediate",
                "time_estimate": "2 Weeks",
                "tech_stack": ["Java", "Spring Boot", "Spring Security", "Hibernate", "H2", "JUnit 5", "Mockito"],
                "description": "Build a secure library portal with role-based access control (Admin/User). Implement lending rules, write 90%+ coverage unit and integration tests using JUnit 5 and Mockito, and automate database migrations with Liquibase.",
                "steps": [
                    "Implement domain models (Book, Transaction, Member) with JPA mappings.",
                    "Configure Spring Security with role authorities (ADMIN, MEMBER) for web routes.",
                    "Write Unit tests targeting service logic using JUnit 5 and Mockito mocks.",
                    "Perform Integration tests against a local H2 database using SpringBootTest configurations.",
                    "Set up database schema versioning scripts using Liquibase migrations."
                ],
                "reference_link": "https://site.mockito.org/"
            }
        ]
    }
    
    default_projects = [
        {
            "title": "Custom Portfolio & Solution Engineering Project",
            "difficulty": "Intermediate",
            "time_estimate": "2-3 Weeks",
            "tech_stack": ["Git", "GitHub Actions", "Docker", "Cloud Deployments"],
            "description": "Build a comprehensive application that implements a core feature set of your custom role. Package the project in a container or deploy to the cloud.",
            "steps": [
                "Plan and design a modular project architecture.",
                "Implement a Git repository with feature branches.",
                "Build the core functionality of the custom application.",
                "Create a Dockerfile to package the environment.",
                "Set up continuous integration pipelines on GitHub."
            ],
            "reference_link": "https://github.com"
        },
        {
            "title": "System Architecture Case Study",
            "difficulty": "Advanced",
            "time_estimate": "2 Weeks",
            "tech_stack": ["System Design", "UML", "Databases", "APIs"],
            "description": "Design the technical architecture for a large scale system related to your custom role. Document data schemas, API flows, and hosting topologies.",
            "steps": [
                "Define structural requirements and traffic/storage metrics.",
                "Design detailed UML sequence and entity-relationship diagrams.",
                "Document REST or gRPC API specs for server interactions.",
                "Present scaling strategies for database replication and caching.",
                "Write a comprehensive markdown technical architecture review."
            ],
            "reference_link": "https://github.com/donnemartin/system-design-primer"
        }
    ]
    
    return catalog.get(target_role, default_projects)

