# Sample Input:
# Enter number of late days: 7
days = int(input("Enter number of late days: "))
if days <= 0:
    fine = 0
elif days <= 5:
    fine = days * 2
else:
    fine = 10 + (days - 5) * 5
print("Library fine: Rs.", fine)