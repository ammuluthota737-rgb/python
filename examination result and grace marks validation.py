
n = int(input("Enter number of subjects: "))

total = 0
max_total = 0
failed = 0

for i in range(1, n + 1):
    print("\nSubject", i)

    maximum = int(input("Enter maximum marks: "))
    marks = int(input("Enter obtained marks: "))
    pass_mark = int(input("Enter pass marks: "))

    grace = 5

    if marks < 0 or marks > maximum:
        print("Invalid marks")
        failed += 1
        continue

    if marks < pass_mark:
        if pass_mark - marks <= grace:
            marks = min(marks + grace, maximum)
            print("Grace marks applied:", marks)
        else:
            failed += 1

    total += marks
    max_total += maximum

    if marks >= pass_mark:
        print("Pass")
    else:
        print("Fail")

percentage = (total / max_total) * 100

print("\nTotal Marks:", total, "/", max_total)
print("Percentage:", round(percentage, 2), "%")

if failed > 0:
    print("Final Result: FAIL")
elif percentage >= 75:
    print("Classification: DISTINCTION")
elif percentage >= 60:
    print("Classification: FIRST CLASS")
elif percentage >= 50:
    print("Classification: SECOND CLASS")
else:
    print("Classification: PASS")
