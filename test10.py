# Sample Input:
# Enter opening stock: 50
# Enter received quantity: 20
# Enter dispatched quantity: 15
# Enter actual closing stock: 55
opening = int(input("Enter opening stock: "))
received = int(input("Enter received quantity: "))
dispatched = int(input("Enter dispatched quantity: "))
actual = int(input("Enter actual closing stock: "))
if min(opening, received, dispatched, actual) < 0:
    print("Invalid quantity")
else:
    expected = opening + received - dispatched
    print("Expected closing stock:", expected)
    if expected == actual:
        print("Stock matches")
    else:
        print("Stock discrepancy found")
        print("Difference:", abs(expected - actual))