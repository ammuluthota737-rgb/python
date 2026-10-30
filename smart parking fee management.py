
print("SMART PARKING SYSTEM")

vehicle = input("Enter vehicle type (car/bike): ").lower()

entry = int(input("Enter entry hour (0-23): "))
exit = int(input("Enter exit hour (0-23): "))

if vehicle not in ["car", "bike"]:
    print("Invalid vehicle type")

elif not (0 <= entry <= 23 and 0 <= exit <= 23):
    print("Invalid time")

else:
    if exit <= entry:
        hours = (24 - entry) + exit
    else:
        hours = exit - entry

    if hours == 0:
        hours = 24

    if vehicle == "car":
        rate = 30
    else:
        rate = 15

    fee = hours * rate

    # Daily maximum limit
    fee = min(fee, 300 if vehicle == "car" else 150)

    # Overnight parking penalty
    if exit <= entry:
        fee += 50

    print("\n--- PARKING BILL ---")
    print("Vehicle:", vehicle)
    print("Parking Hours:", hours)
    print("Parking Fee: Rs.", fee)
