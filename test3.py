# Sample Input:
# Enter marks in subject 1: 80
# Enter marks in subject 2: 70
# Enter marks in subject 3: 60
m1 = int(input("Enter marks in subject 1: "))
m2 = int(input("Enter marks in subject 2: "))
m3 = int(input("Enter marks in subject 3: "))
if min(m1, m2, m3) < 0 or max(m1, m2, m3) > 100:
    print("Invalid marks")
else:
    total = m1 + m2 + m3
    percentage = total / 3
    if m1 >= 35 and m2 >= 35 and m3 >= 35:
        print("Result: PASS")
    else:
        print("Result: FAIL")
    print("Total marks:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")