import subprocess
import tempfile
import os

def run_code(code: str, language: str = "python") -> dict:
    """
    Executes the provided code and returns the output or error.
    Supports Python, Java, C++, and C.
    For production, use a secure sandbox or third-party API!
    """
    if language == "python":
        suffix = ".py"
    elif language == "java":
        suffix = ".java"
    elif language in ["cpp", "c++"]:
        suffix = ".cpp"
    elif language == "c":
        suffix = ".c"
    else:
        return {"error": f"Language {language} not supported for execution."}

    with tempfile.NamedTemporaryFile(mode="w+", suffix=suffix, delete=False) as tmp:
        tmp.write(code)
        tmp.flush()
        tmp_name = tmp.name

    try:
        if language == "python":
            result = subprocess.run(
                ["python", tmp_name],
                capture_output=True,
                text=True,
                timeout=5
            )
            return {"output": result.stdout, "error": result.stderr}

        elif language == "java":
            # Compile
            compile_proc = subprocess.run(
                ["javac", tmp_name],
                capture_output=True,
                text=True,
                timeout=5
            )
            if compile_proc.returncode != 0:
                return {"output": "", "error": compile_proc.stderr}
            # Run
            class_name = os.path.splitext(os.path.basename(tmp_name))[0]
            run_proc = subprocess.run(
                ["java", class_name],
                capture_output=True,
                text=True,
                timeout=5
            )
            return {"output": run_proc.stdout, "error": run_proc.stderr}

        elif language in ["cpp", "c++"]:
            exe_file = tmp_name.replace(suffix, "")
            compile_proc = subprocess.run(
                ["g++", tmp_name, "-o", exe_file],
                capture_output=True,
                text=True,
                timeout=5
            )
            if compile_proc.returncode != 0:
                return {"output": "", "error": compile_proc.stderr}
            run_proc = subprocess.run(
                [exe_file],
                capture_output=True,
                text=True,
                timeout=5
            )
            return {"output": run_proc.stdout, "error": run_proc.stderr}

        elif language == "c":
            exe_file = tmp_name.replace(suffix, "")
            compile_proc = subprocess.run(
                ["gcc", tmp_name, "-o", exe_file],
                capture_output=True,
                text=True,
                timeout=5
            )
            if compile_proc.returncode != 0:
                return {"output": "", "error": compile_proc.stderr}
            run_proc = subprocess.run(
                [exe_file],
                capture_output=True,
                text=True,
                timeout=5
            )
            return {"output": run_proc.stdout, "error": run_proc.stderr}

    except Exception as e:
        return {"error": str(e)}

def check_syntax(code: str, language: str = "python") -> dict:
    """
    Checks syntax of the code for multiple languages.
    Returns error message if syntax is invalid, else empty string.
    """
    if language == "python":
        try:
            compile(code, '<string>', 'exec')
            return {"error": ""}
        except SyntaxError as e:
            return {"error": str(e)}

    elif language == "java":
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".java", delete=False) as tmp:
            tmp.write(code)
            tmp.flush()
            try:
                result = subprocess.run(
                    ["javac", tmp.name],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode != 0:
                    return {"error": result.stderr}
                return {"error": ""}
            except Exception as e:
                return {"error": str(e)}

    elif language in ["c", "cpp", "c++"]:
        suffix = ".c" if language == "c" else ".cpp"
        with tempfile.NamedTemporaryFile(mode="w+", suffix=suffix, delete=False) as tmp:
            tmp.write(code)
            tmp.flush()
            try:
                compiler = "gcc" if language == "c" else "g++"
                result = subprocess.run(
                    [compiler, "-fsyntax-only", tmp.name],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode != 0:
                    return {"error": result.stderr}
                return {"error": ""}
            except Exception as e:
                return {"error": str(e)}
    else:
        return {"error": f"Syntax checking not supported for {language}."}
