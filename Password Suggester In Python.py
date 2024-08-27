import re

def assess_password_strength(password):
    feedback = []
    strength = 0  # To keep track of how many criteria are met

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    else:
        feedback.append("Password length is sufficient.")
        strength += 1

    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should contain at least one uppercase letter.")
    else:
        feedback.append("Password contains uppercase letters.")
        strength += 1

    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        feedback.append("Password should contain at least one lowercase letter.")
    else:
        feedback.append("Password contains lowercase letters.")
        strength += 1

    # Check for numbers
    if not re.search(r'[0-9]', password):
        feedback.append("Password should contain at least one number.")
    else:
        feedback.append("Password contains numbers.")
        strength += 1

    # Check for special characters
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?/\\|`~]', password):
        feedback.append("Password should contain at least one special character.")
    else:
        feedback.append("Password contains special characters.")
        strength += 1

    # Check overall strength
    if strength == 5:
        feedback.append("Your password is strong!")
    else:
        feedback.append("Your password could be improved. Consider the feedback above.")

    return feedback

def main():
    password = input("Enter a password to assess its strength: ")
    feedback = assess_password_strength(password)
    print("\nPassword Assessment Feedback:")
    for message in feedback:
        print(f"- {message}")

if __name__ == "__main__":
    main()