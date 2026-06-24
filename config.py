import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'careerforge-secret-key-9x8y7z')
    # Use Vercel's temp directory if running serverlessly or in a read-only filesystem
    if os.environ.get('VERCEL') or not os.access(os.path.abspath(os.path.dirname(__file__)), os.W_OK):
        UPLOAD_FOLDER = '/tmp/uploads'
    else:
        UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
        
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload size
    
    # DB configuration
    DB_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    DB_USER = os.environ.get('MYSQL_USER', None)
    DB_PASSWORD = os.environ.get('MYSQL_PASSWORD', None)
    DB_NAME = os.environ.get('MYSQL_DATABASE', 'careerforge_db')
    
    if DB_USER and DB_PASSWORD:
        # MySQL connection
        SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
        USE_MYSQL = True
    else:
        # Local SQLite fallback
        db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'careerforge.db')
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"
        USE_MYSQL = False
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False
