import sqlite3
import json
import os
import mysql.connector
from config import Config

def get_db_connection():
    """Establish a connection to either MySQL or SQLite based on configuration."""
    if Config.USE_MYSQL:
        try:
            return mysql.connector.connect(
                host=Config.DB_HOST,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_NAME
            )
        except mysql.connector.Error as err:
            # If the database doesn't exist, connect without database to create it
            if err.errno == 1049:  # Unknown database
                conn = mysql.connector.connect(
                    host=Config.DB_HOST,
                    user=Config.DB_USER,
                    password=Config.DB_PASSWORD
                )
                cursor = conn.cursor()
                cursor.execute(f"CREATE DATABASE {Config.DB_NAME}")
                cursor.close()
                conn.close()
                # Try connecting again
                return mysql.connector.connect(
                    host=Config.DB_HOST,
                    user=Config.DB_USER,
                    password=Config.DB_PASSWORD,
                    database=Config.DB_NAME
                )
            else:
                raise err
    else:
        # Local SQLite
        # Use Vercel's temp directory if running serverlessly or in a read-only filesystem
        if os.environ.get('VERCEL') or not os.access(os.path.abspath(os.path.dirname(__file__)), os.W_OK):
            db_file = '/tmp/careerforge.db'
        else:
            db_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'careerforge.db')
        conn = sqlite3.connect(db_file)
        # Enable dictionary-like row factory for easy access
        conn.row_factory = sqlite3.Row
        return conn

def init_db():
    """Initialize database tables for resumes and comparisons."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if Config.USE_MYSQL:
        # Create resumes table for MySQL
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS resumes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                filename VARCHAR(255) NOT NULL,
                candidate_name VARCHAR(255),
                email VARCHAR(255),
                target_role VARCHAR(255) NOT NULL,
                cgpa FLOAT,
                ats_score FLOAT,
                skill_match FLOAT,
                placement_prob FLOAT,
                analysis_data LONGTEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create comparisons table for MySQL
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS comparisons (
                id INT AUTO_INCREMENT PRIMARY KEY,
                filename_a VARCHAR(255) NOT NULL,
                filename_b VARCHAR(255) NOT NULL,
                target_role VARCHAR(255) NOT NULL,
                comparison_data LONGTEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    else:
        # Create resumes table for SQLite
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS resumes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                candidate_name TEXT,
                email TEXT,
                target_role TEXT NOT NULL,
                cgpa REAL,
                ats_score REAL,
                skill_match REAL,
                placement_prob REAL,
                analysis_data TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create comparisons table for SQLite
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS comparisons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename_a TEXT NOT NULL,
                filename_b TEXT NOT NULL,
                target_role TEXT NOT NULL,
                comparison_data TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
    conn.commit()
    cursor.close()
    conn.close()
    print("Database tables initialized successfully.")
