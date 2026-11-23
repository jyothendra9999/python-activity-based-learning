# Sample Input:
# Enter product price: 250
# Enter quantity: 4
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
if price <= 0 or quantity <= 0:
    print("Invalid input")
else:
    bill = price * quantity
    if bill >= 1000:
        discount = bill * 0.10
    else:
        discount = 0
    final_amount = bill - discount
    print("Bill amount:", bill)
    print("Discount:", discount)
    print("Final amount:", final_amount)