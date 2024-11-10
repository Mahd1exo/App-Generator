import os

# Load API key securely from environment variables or .env file
API_KEY = os.getenv("GOOGLE_API_KEY")
LOG_FILE_PATH = "responses/generated_project.py"
MEMORY_DB_PATH = "memory/ai_memory.db"
