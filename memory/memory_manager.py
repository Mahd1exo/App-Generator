import pyodbc
import os

# SQL Server configuration
SERVER = 'DESKTOP-JV3IHPL'  # Replace with your server name
DATABASE = 'AI_ProjectDB'  # Database name
DRIVER = '{ODBC Driver 17 for SQL Server}'  # Ensure this driver is installed

def get_connection():
    """Establishes and returns a connection to SQL Server using Windows Authentication."""
    conn = pyodbc.connect(
        f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;"
    )
    return conn

def initialize_memory():
    """Ensures necessary tables exist in SQL Server."""
    conn = get_connection()
    cursor = conn.cursor()

    # Create the memory table if it doesn't exist
    cursor.execute('''
        IF OBJECT_ID('memory', 'U') IS NULL
            CREATE TABLE memory ([key] NVARCHAR(255) PRIMARY KEY, value NVARCHAR(MAX))
    ''')

    # Create the common_issues table if it doesn't exist
    cursor.execute('''
        IF OBJECT_ID('common_issues', 'U') IS NULL
            CREATE TABLE common_issues (issue NVARCHAR(255) PRIMARY KEY, count INT)
    ''')

    conn.commit()
    conn.close()

def load_memory():
    """Load memory data to guide the AI based on previous interactions."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT [key], value FROM memory")
    memory_data = {row.key: row.value for row in cursor.fetchall()}

    conn.close()
    return memory_data

def update_memory(key, value):
    """Update or insert a memory item in the database."""
    conn = get_connection()
    cursor = conn.cursor()

    # Use MERGE to perform upsert operation in SQL Server
    cursor.execute('''
        MERGE memory AS target
        USING (SELECT ? AS [key], ? AS value) AS source
        ON (target.[key] = source.[key])
        WHEN MATCHED THEN 
            UPDATE SET value = source.value
        WHEN NOT MATCHED THEN
            INSERT ([key], value) VALUES (source.[key], source.value);
    ''', (key, value))

    conn.commit()
    conn.close()

def log_common_issue(issue):
    """Increment the count for a common issue or add it if it doesn't exist."""
    conn = get_connection()
    cursor = conn.cursor()

    # Check if the issue already exists
    cursor.execute("SELECT count FROM common_issues WHERE issue = ?", (issue,))
    result = cursor.fetchone()

    if result:
        # Issue exists, so increment the count
        cursor.execute("UPDATE common_issues SET count = count + 1 WHERE issue = ?", (issue,))
    else:
        # Issue does not exist, so insert it with a count of 1
        cursor.execute("INSERT INTO common_issues (issue, count) VALUES (?, ?)", (issue, 1))

    conn.commit()
    conn.close()

def get_common_issues(min_count=2):
    """Retrieve common issues with a count equal to or greater than min_count."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT issue FROM common_issues WHERE count >= ?", (min_count,))
    common_issues = [row.issue for row in cursor.fetchall()]

    conn.close()
    return common_issues
