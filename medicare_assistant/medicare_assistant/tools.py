import re
from datetime import datetime


def get_current_datetime() -> str:
    try:
        now = datetime.now()
        return now.strftime("Current date: %A, %d %B %Y | Current time: %I:%M %p")
    except Exception as e:
        return f"Error getting date/time: {str(e)}"


def calculate(expression: str) -> str:
    try:
        cleaned = expression
        cleaned = re.sub(r'\bplus\b', '+', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'\bminus\b', '-', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'\btimes\b', '*', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'\bdivided by\b', '/', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'\band\b', '+', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'\bsubtract\b', '-', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'\badd\b', '+', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'\bmultiply\b', '*', cleaned, flags=re.IGNORECASE)
        # Keep only safe characters
        cleaned = re.sub(r'[^0-9+\-*/().,\s]', '', cleaned).strip()
        if not cleaned:
            return "Could not parse the mathematical expression. Please provide a simple arithmetic expression."
        # Restricted eval — no builtins, no globals
        result = eval(cleaned, {"__builtins__": {}}, {})
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Calculation error: Division by zero is not allowed."
    except Exception as e:
        return f"Calculation error: {str(e)}. Please provide a simple arithmetic expression like '500 + 800'."


def get_helpline() -> str:
    return "MediCare Helpline: 040-99887766 | Emergency: 040-12345678"
