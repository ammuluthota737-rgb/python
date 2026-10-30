
months = int(input("Enter number of months: "))

bills = []

for i in range(months):
    units = int(input(f"Enter units for month {i+1}: "))

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    elif units <= 300:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5
    else:
        bill = 100 * 2 + 100 * 3 + 100 * 5 + (units - 300) * 7

    fixed = 50
    surcharge = bill * 0.05
    rebate = 20 if units < 100 else 0

    total = bill + fixed + surcharge - rebate
    bills.append(total)

    print("Monthly Bill:", round(total, 2))

print("\nBill Comparison")

for i in range(months):
    print("Month", i+1, ":", round(bills[i], 2))

    if i > 0 and bills[i] > bills[i-1] * 1.2:
        print("Unusual increase detected!")
