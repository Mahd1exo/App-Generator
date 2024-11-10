# utils/validation.py

def check_spacing_issues(response_text):
    """Check if the response has excessive or inconsistent spacing issues."""
    lines = response_text.splitlines()
    excessive_spacing = any(line == "" for line in lines)  # Check for double blank lines
    return not excessive_spacing  # Returns False if excessive spacing is found


def check_missing_components(response_text, required_components):
    """Ensure the response includes required components."""
    missing_components = [component for component in required_components if component not in response_text]
    return missing_components  # Return list of missing components


def validate_response(response_text, feedback_issues):
    """Validate response based on feedback issues like spacing or missing components."""
    results = {}
    
    # Check for spacing issues if 'spacing' is flagged in feedback issues
    if "spacing" in feedback_issues:
        spacing_check = check_spacing_issues(response_text)
        results['spacing'] = spacing_check
    
    # Check for missing components if 'missing' is flagged in feedback issues
    if "missing" in feedback_issues:
        required_components = ["+", "-", "*", "/"]  # Example components for a calculator app
        missing_components = check_missing_components(response_text, required_components)
        results['missing_components'] = missing_components  # List of missing components
    
    return results
