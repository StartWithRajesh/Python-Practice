mat = int(input("Enter the marks in MATHS: "))
phy = int(input("Enter the marks in PHYSICS: "))
che = int(input("Enter the marks in CHEMISTRY: "))
total = mat+phy+che
avg = total/3
per = (total/300)*100
grade = ""
if per > 90:
    grade = "A"
elif per<=90 and per>80:
    grade = "B"
elif per<=80 and per>70:
    grade = "C"
else:
    grade = "Pass"

print(f"Total : {total} \nAverage : {avg:.3f} \nPercentage : {per:.2f} \nGrade : {grade}")