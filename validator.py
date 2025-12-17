def validate_password(password):
    if len(password) < 9:
        return False

    has_upper = any(char.isupper() for char in password)
    has_digit_1 = any(char.isdigit() for char in password)

    return has_upper and has_digit

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    print(f"Password is valid: {validate_password(pwd)}")
