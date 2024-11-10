import pyodbc
from datetime import datetime

# SQL Server configuration
SERVER = 'DESKTOP-JV3IHPL'  # Replace with your server name
DATABASE = 'AI_ProjectDB'  # Replace with your database name
DRIVER = '{ODBC Driver 17 for SQL Server}'  # Ensure this driver is installed

def get_connection():
    """Establishes and returns a connection to SQL Server using Windows Authentication."""
    conn = pyodbc.connect(
        f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;"
    )
    return conn

def initialize_bug_logger():
    """Ensures the bugs table exists in SQL Server."""
    conn = get_connection()
    cursor = conn.cursor()

    # Create the bugs table if it doesn't exist
    cursor.execute('''
        IF OBJECT_ID('bugs', 'U') IS NULL
            CREATE TABLE bugs (
                id INT IDENTITY(1,1) PRIMARY KEY,
                error_type NVARCHAR(255),
                description NVARCHAR(MAX),
                prompt NVARCHAR(MAX),
                timestamp DATETIME
            )
    ''')
    conn.commit()
    conn.close()

def log_bug(error_type, description, prompt):
    """Logs a bug to the bugs table in SQL Server."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Insert the error into the bugs table with the current timestamp
    cursor.execute('''
        INSERT INTO bugs (error_type, description, prompt, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (error_type, description, prompt, datetime.now()))

    conn.commit()
    conn.close()

# Ensure the bugs table is created when this module is loaded
initialize_bug_logger()
