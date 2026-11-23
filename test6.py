# Sample Input:
# Enter number of rows: 4
n = int(input("Enter number of rows: "))
if n <= 0:
    print("Enter a positive number")
else:
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end="")
        print()