
import string

n = int(input("Enter number of passwords: "))

prohibited = ["password", "admin", "123456"]

for i in range(n):
    pwd = input("\nEnter password: ")
    errors = []

    if len(pwd) < 8:
        errors.append("Minimum 8 characters required")

    if not any(c.isupper() for c in pwd):
        errors.append("Missing uppercase letter")

    if not any(c.islower() for c in pwd):
        errors.append("Missing lowercase letter")

    if not any(c.isdigit() for c in pwd):
        errors.append("Missing digit")

    if not any(c in string.punctuation for c in pwd):
        errors.append("Missing special character")

    if any(pwd[j] == pwd[j+1] for j in range(len(pwd)-1)):
        errors.append("Repeated consecutive characters")

    if any(word in pwd.lower() for word in prohibited):
        errors.append("Contains prohibited substring")

    if len(errors) == 0:
        print("Valid Password")
    else:
        print("Invalid Password")
        print("Failed Conditions:")
        for error in errors:
            print("-", error)
