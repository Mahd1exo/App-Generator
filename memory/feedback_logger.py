import pyodbc
from datetime import datetime
from memory.memory_manager import log_common_issue  # To log frequent issues

SERVER = 'DESKTOP-JV3IHPL'
DATABASE = 'AI_ProjectDB'
DRIVER = '{ODBC Driver 17 for SQL Server}'

def get_connection():
    conn = pyodbc.connect(
        f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;"
    )
    return conn

def initialize_feedback_logger():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        IF OBJECT_ID('feedback', 'U') IS NULL
            CREATE TABLE feedback (
                id INT IDENTITY(1,1) PRIMARY KEY,
                rating INT,
                comments NVARCHAR(MAX),
                prompt NVARCHAR(MAX),
                timestamp DATETIME
            )
    ''')
    conn.commit()
    conn.close()

def log_feedback(rating, comments, prompt):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO feedback (rating, comments, prompt, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (rating, comments, prompt, datetime.now()))

    conn.commit()
    conn.close()

    # Analyze feedback to identify common issues
    if int(rating) <= 2:  # Track low ratings as common issues
        log_common_issue("Low rating feedback")
    
    # Example keywords to track in comments for future prompt adjustment
    keywords = ["spacing", "missing", "incomplete", "error"]
    for keyword in keywords:
        if keyword in comments.lower():
            log_common_issue(f"Issue related to '{keyword}'")  # Track issue keywords for the AI prompt

initialize_feedback_logger()
