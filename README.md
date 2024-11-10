
# AI-Enhanced Code Generator with Feedback Loop 🧠

An intelligent code generation system that leverages OpenAI's generative models to create Python applications with Tkinter or other GUI frameworks. This project integrates a feedback loop, allowing users to request iterative improvements to generated code, capture common issues, and log feedback for ongoing enhancement.

---

## Features ✨

- **Automated Code Generation**: Uses OpenAI's model to generate Python applications based on user prompts.
- **Feedback-Based Refinement**: Iteratively improves responses by analyzing and logging incomplete or error-prone outputs.
- **Customizable Prompting System**: Enables users to specify prompt details, including layout requirements, functionality, and responsiveness.
- **Dark Theme and Responsiveness**: Code generated adheres to a modern dark theme with responsive design.
- **Error Logging and Issue Tracking**: Logs incomplete or problematic responses for future improvement and debugging.
  
---

## File Structure 🗂️

```
project_root/
├── main.py                     # Main program to run the AI-based chat loop for code generation
├── memory/
│   ├── brain.py                # Core logic for analyzing AI responses and refining prompts
│   ├── memory_manager.py       # Manages logging and retrieval of common issues for prompt refinement
│   └── incomplete_responses.log # Log file for storing incomplete or problematic responses
├── prompt/
│   ├── prompt_loader.py        # Loads prompt templates and user inputs
│   └── templates/
│       ├── base_prompt.txt     # Base prompt template for initial AI queries
│       └── feedback_prompt.txt # Feedback prompt template for re-evaluation
├── responses/
│   ├── generated_project.py    # AI-generated Python application file
│   └── conversation_log.txt    # Log file storing the conversation history with the AI
├── utils/
│   ├── clean_output.py         # Utility function to clean AI responses of markdown and extraneous text
│   └── validation.py           # Validation functions to check completeness and accuracy of AI-generated code
└── README.md                   # Documentation for the project setup, usage, and structure
```

---

## Getting Started 🚀

### Prerequisites

- **Python 3.8+**: Ensure Python is installed on your system.
- **OpenAI API Key**: Set up your OpenAI API key for access to generative models.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key:
   ```bash
   export GOOGLE_API_KEY='your_api_key'
   ```

4. Run the main program:
   ```bash
   python main.py
   ```

---

## Usage 🛠️

### Basic Commands

1. **Start the program**:
   Run `python main.py` and follow the prompts to input requests for code generation, like `"Write a Python program for a calculator with Tkinter."`

2. **Provide Feedback**:
   After code execution, rate the response (1-5) and add any additional comments. This feedback helps refine future outputs.

3. **Exit the Program**:
   Type `"exit"` at any prompt to terminate the session.

### Example Prompts

- **Basic GUI Application**: `"Create a basic Tkinter application for a calculator."`
- **Responsive Layout**: `"Write a responsive Tkinter GUI with a dark theme."`
- **Error Handling**: `"Generate a Python GUI with error handling for a calculator app."`

---

## Logging and Issue Tracking 📋

- **Logging**: Every response is logged in `responses/conversation_log.txt`, and incomplete responses are stored in `memory/incomplete_responses.log`.
- **Feedback Tracking**: User feedback on responses is recorded to improve iterative performance.

---

## Project Highlights 🌟

- **Generative Model Integration**: Powered by OpenAI's generative models to create dynamic Python applications.
- **Iterative Feedback Loop**: AIBrain class ensures improvements based on previous shortcomings.
- **Dark Theme & Responsiveness**: Designed with modern UI/UX principles for engaging applications.

---

## Contact 📧

For questions, suggestions, or contributions, please reach out to:

- **GitHub**: [yourusername](https://github.com/yourusername)
- **Email**: your.email@example.com

Happy coding! 🧑‍💻🚀
