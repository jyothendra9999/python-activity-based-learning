# Sample Input:
# Enter total classes held: 40
# Enter classes attended: 28
# Enter target percentage: 75
total = int(input("Enter total classes held: "))
attended = int(input("Enter classes attended: "))
target = float(input("Enter target percentage: "))
if total <= 0 or attended < 0 or attended > total or target < 0 or target >= 100:
    print("Invalid input")
else:
    percentage = (attended / total) * 100
    extra = 0
    while percentage < target:
        extra += 1
        percentage = ((attended + extra) / (total + extra)) * 100
    print("Current attendance:", round((attended / total) * 100, 2), "%")
    print("Additional classes required:", extra)