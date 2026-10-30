
candidates = []

n = int(input("Enter number of candidates: "))

for i in range(n):
    print("\nCandidate", i + 1)

    name = input("Enter name: ")
    maths = int(input("Enter Maths marks: "))
    physics = int(input("Enter Physics marks: "))
    chemistry = int(input("Enter Chemistry marks: "))

    total = maths + physics + chemistry
    percentage = total / 3

    # Eligibility conditions
    if (maths >= 40 and physics >= 40 and
        chemistry >= 40 and percentage >= 60):

        candidates.append(
            (name, percentage, maths)
        )

    else:
        print("Not eligible")

# Ranking: percentage first, Maths marks second
candidates.sort(key=lambda x: (x[1], x[2]), reverse=True)

print("\n--- ADMISSION RANK LIST ---")

if len(candidates) == 0:
    print("No eligible candidates")

else:
    for rank, candidate in enumerate(candidates, 1):
        print("Rank:", rank)
        print("Name:", candidate[0])
        print("Percentage:", round(candidate[1], 2))
        print("Maths Marks:", candidate[2])
        print("--------------------")
