
balance = float(input("Enter initial balance: "))
n = int(input("Enter number of transactions: "))

deposits = 0
withdrawals = 0
rejected = 0

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
        rejected += 1

    elif choice == 1:
        balance += amount
        deposits += 1
        print("Deposit successful")

    elif choice == 2:
        if amount > 10000:
            print("Withdrawal limit exceeded")
            rejected += 1
        elif amount > balance:
            print("Insufficient balance")
            rejected += 1
        else:
            balance -= amount
            withdrawals += 1
            print("Withdrawal successful")

    else:
        print("Invalid transaction type")
        rejected += 1

print("\n--- ATM SUMMARY ---")
print("Final Balance:", balance)
print("Successful Deposits:", deposits)
print("Successful Withdrawals:", withdrawals)
print("Rejected Transactions:", rejected)
