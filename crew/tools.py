from crewai_tools import tool

@tool("Code Validator")
def validate_code(code: str, language: str = "python") -> str:
    """Validates code syntax and structure for common errors in Python, Java, C, and C++"""
    lang = language.lower()
    
    if lang == "python":
        if "def " not in code:
            return "Missing function definition"
        if "return " not in code:
            return "No return statement found"
        return "Code structure appears valid"
    
    elif lang in ["c", "c++", "cpp"]:
        if not ("int main" in code or "void main" in code):
            return "Missing main function"
        if ";" not in code:
            return "Missing semicolon"
        return "Code structure appears valid"
    
    elif lang == "java":
        if "class " not in code:
            return "Missing class definition"
        if "public static void main" not in code:
            return "Missing main method"
        if ";" not in code:
            return "Missing semicolon"
        return "Code structure appears valid"
    
    else:
        return "Language not supported for validation"
