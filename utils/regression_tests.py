def check_button_spacing(ai_code):
    """Check generated code for excessive button spacing."""
    # Simple pattern to detect excessive spacing; adjust as needed
    spacing_issue = "pad" in ai_code and any(gap in ai_code for gap in ["padx=20", "pady=20", "padx=15", "pady=15"])
    return not spacing_issue
