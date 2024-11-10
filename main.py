import os
import google.generativeai as genai
from memory.brain import AIBrain  # Import AIBrain class
from memory.memory_manager import initialize_memory, get_common_issues
from prompt.prompt_loader import load_prompt
import subprocess

# Import the clean_code_output function
from utils.clean_output import clean_code_output

# API setup
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key is missing. Please set GOOGLE_API_KEY in your environment variables.")
genai.configure(api_key=api_key)
model_name = 'gemini-pro'
model = genai.GenerativeModel(model_name)
chat = model.start_chat(history=[])

log_file = "responses/generated_project.py"
initialize_memory()  # Ensure tables exist

def generate_prompt(user_prompt):
    """Generate the initial prompt with memory feedback based on past issues."""
    base_prompt = load_prompt()
    common_issues = get_common_issues(min_count=2)

    if common_issues:
        issues_text = "\n".join(f"- {issue}" for issue in common_issues)
        prompt_text = (
            f"{base_prompt}\n\nAddress these known issues from previous feedback:\n"
            f"{issues_text}\n\nUser Prompt: {user_prompt}\n\n"
            "Please provide a complete and executable Python code response. "
            "The code should include all necessary components, such as imports, class definitions, "
            "function definitions, and the 'if __name__ == '__main__':' block. "
            "Do not include comments, explanations, or extra text."
        )
    else:
        prompt_text = (
            f"{base_prompt}\n\nUser Prompt: {user_prompt}\n\n"
            "Please provide a complete and executable Python code response. "
            "The code should include all necessary components, such as imports, class definitions, "
            "function definitions, and the 'if __name__ == '__main__':' block. "
            "Do not include comments, explanations, or extra text."
        )
    return prompt_text

def run_generated_code():
    """Execute the generated Python script to check for errors."""
    try:
        result = subprocess.run(["python", log_file], check=True, capture_output=True, text=True)
        print(result.stdout)  # Display standard output if any
        print("Generated code executed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        error_message = str(e)
        print(f"Error in generated code: {error_message}")
        print(f"Error details:\n{e.stderr}")
        return False

def chat_with_bot():
    """Main chat loop with the user, using AIBrain to get a direct response."""
    brain = AIBrain(chat)  # Initialize AIBrain without iterations
    
    while True:
        user_prompt = input("You: ")
        if user_prompt.lower() == "exit":
            break

        initial_prompt = generate_prompt(user_prompt)
        final_code = brain.get_first_response(initial_prompt)

        if final_code:
            with open(log_file, "w", encoding="utf-8") as file:
                file.write(final_code)
            print("Code saved to generated_project.py.")

            if run_generated_code():
                print("Code executed successfully.")
            else:
                print("Error detected in the final response.")
        else:
            print("Received an incomplete response. Please check the logs for details.")

        rating = input("Rate the response (1-5): ")
        comments = input("Additional comments: ")
        # Log feedback and issues if further refinements are needed

if __name__ == "__main__":
    chat_with_bot()
