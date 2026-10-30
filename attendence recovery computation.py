
total = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))
threshold = float(input("Enter eligibility percentage: "))

if total <= 0 or attended < 0 or attended > total or not 0 < threshold <= 100:
    print("Invalid input")
else:
    current = (attended / total) * 100
    print("Current Attendance:", round(current, 2), "%")

    if current >= threshold:
        print("Already eligible!")
    else:
        required = 0
        while ((attended + required) / (total + required)) * 100 < threshold:
            required += 1

        print("Required consecutive classes:", required)

        # Future attendance scenarios
        for rate in [1.0, 0.8, 0.5]:
            a = 0
            t = 0
            while ((attended + a) / (total + t)) * 100 < threshold:
                a += rate
                t += 1
            print("Future attendance rate:", rate * 100,
                  "% - Required classes:", t)
