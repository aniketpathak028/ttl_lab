# 10. WAP to input password for 3 times and check password must start with one upper case, one special character, one digit

import re

def check_password(password):
    if (len(password) < 8):
        return False
    elif not re.search("[A-Z]", password):
        return False
    elif not re.search("[0-9]", password):
        return False
    elif not re.search("[@#$%^&+=]", password):
        return False
    else:
        return True

attempt = 1
while attempt <= 3:
    password = input("Enter a password: ")
    if check_password(password):
        print("Password accepted.")
        break
    else:
        print("Invalid password.")
        attempt += 1

if attempt > 3:
    print("Too many attempts. Access denied.")