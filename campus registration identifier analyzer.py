
n = int(input("Enter number of student IDs: "))

branches = {
    "CSE": "Computer Science",
    "AIML": "Artificial Intelligence",
    "ECE": "Electronics",
    "EEE": "Electrical"
}

for i in range(n):
    sid = input("\nEnter Student ID: ").upper()

    if (len(sid) == 9 and
        sid[:2].isdigit() and
        sid[2:6] in branches and
        sid[6:].isdigit()):

        year = "20" + sid[:2]
        branch = branches[sid[2:6]]
        number = sid[6:]

        print("Valid Registration ID")
        print("Admission Year:", year)
        print("Branch:", branch)
        print("Student Number:", number)

    else:
        print("Invalid Registration ID")
