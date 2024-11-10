# memory/brain.py
import re
import logging
import os
from utils.clean_output import clean_code_output
from memory.memory_manager import log_common_issue

# Ensure logging directory
log_directory = "memory"
log_file = os.path.join(log_directory, "incomplete_responses.log")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")

class AIBrain:
    def __init__(self, chat):
        self.chat = chat

    def strip_markdown(self, response_text):
        """Remove markdown-like code fences from response text."""
        return re.sub(r"^```(?:python)?|```$", "", response_text, flags=re.MULTILINE).strip()

    def get_first_response(self, prompt):
        """Request code generation once, clean it, and return the response."""
        response = self.chat.send_message(prompt)
        response_text = self.strip_markdown(response.text.strip())

        if "import" in response_text and "__main__" in response_text:
            final_code = clean_code_output(response_text)
            if final_code:
                return final_code

        logging.info(f"Incomplete response:\n{response_text}")
        log_common_issue("incomplete_code")
        return response_text  # Return as-is for review
