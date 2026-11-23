# Sample Input:
# Enter password: Hello123
password = input("Enter password: ")
length_ok = len(password) >= 8
digit_found = False
for ch in password:
    if ch.isdigit():
        digit_found = True
if length_ok and digit_found:
    print("Valid password")
else:
    print("Invalid password")
    if not length_ok:
        print("Password must have at least 8 characters")
    if not digit_found:
        print("Password must contain at least one digit")