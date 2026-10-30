
print("HOSPITAL BILLING SYSTEM")

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

consultation = float(input("Enter consultation charge: "))
diagnostic = float(input("Enter diagnostic charge: "))
treatment = float(input("Enter treatment charge: "))

if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges!")
else:
    total = consultation + diagnostic + treatment

    if age >= 60:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    print("Total Bill:", total)
    print("Concession:", discount)
    print("Final Bill:", final_bill)

    paid = float(input("Enter amount paid: "))

    if paid < 0 or paid > final_bill:
        print("Invalid payment amount!")
    elif paid == final_bill:
        print("Payment Status: Fully Paid")
    elif paid > 0:
        print("Payment Status: Partially Paid")
    else:
        print("Payment Status: Payment Pending")

    if 0 <= paid <= final_bill:
        print("Balance Amount:", final_bill - paid)
        print("Patient Name:", name)
