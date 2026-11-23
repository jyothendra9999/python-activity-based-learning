# Sample Input:
# Enter opening balance: 1000
# How many transactions? 2
# Enter D for deposit or W for withdrawal: D
# Enter amount: 500
# Enter D for deposit or W for withdrawal: W
# Enter amount: 200
balance = float(input("Enter opening balance: "))
n = int(input("How many transactions? "))
for i in range(n):
    kind = input("Enter D for deposit or W for withdrawal: ").upper()
    amount = float(input("Enter amount: "))
    if amount <= 0:
        print("Invalid amount")
    elif kind == "D":
        balance += amount
        print("Deposit successful")
    elif kind == "W":
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    else:
        print("Invalid transaction type")
print("Final balance:", balance)
