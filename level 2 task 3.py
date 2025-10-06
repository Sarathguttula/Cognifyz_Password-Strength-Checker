import re

def check_password_strength(password):
    """
    Evaluates the strength of a password based on:
    - Length (at least 8 characters)
    - Uppercase letters
    - Lowercase letters
    - Digits
    - Special characters
    """
    length = len(password) >= 8
    upper = re.search(r'[A-Z]', password) is not None
    lower = re.search(r'[a-z]', password) is not None
    digit = re.search(r'\d', password) is not None
    special = re.search(r'[\W_]', password) is not None

    score = sum([length, upper, lower, digit, special])

    if score == 5:
        return "Strong password."
    elif score >= 3:
        return "Moderate password."
    else:
        return "Weak password."

if __name__ == "__main__":
    pwd = input("Enter a password to check its strength: ")
    print(check_password_strength(pwd))