# Sample Input:
# Enter exam mark: 60
# Enter exam mark: 70
# Enter exam mark: 80
marks = []
for i in range(3):
    mark = int(input("Enter exam mark: "))
    if mark < 0 or mark > 100:
        print("Invalid mark")
        break
    marks.append(mark)
if len(marks) == 3:
    for i in range(1, 3):
        if marks[i] > marks[i-1]:
            print("Exam", i + 1, ": Improved")
        elif marks[i] < marks[i-1]:
            print("Exam", i + 1, ": Declined")
        else:
            print("Exam", i + 1, ": No change")