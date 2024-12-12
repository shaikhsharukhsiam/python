marks=input("enter your marks: ")
marks=int(marks)
if marks >=80:
    grade = "A+"
elif marks >=70:
    grade = "A"
elif marks >=60:
    grade = "C"
else:
    grade="F"
print("your grade is",grade)