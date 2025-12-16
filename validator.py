def check_password(password):
    # TODO: Add more checks later
    if len(password) > 8:
        return True
    else:
        return False

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    print(f"Password is valid: {check_password(pwd)}")