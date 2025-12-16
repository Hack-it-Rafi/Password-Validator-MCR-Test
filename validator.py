def check_password(password):
    if len(password) <= 8:
        return False

    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_upper and has_digit

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    print(f"Password is valid: {check_password(pwd)}")