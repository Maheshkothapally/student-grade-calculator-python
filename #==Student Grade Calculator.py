
name=input("enter name:")

english=int(input("enter marks python:"))
operating_system=int(input("enter marks os:"))
mathematics=int(input("enter mathematics marks: "))
dbms=int(input("enter dbms marks:"))

total_marks=english+operating_system+mathematics+dbms

percentage=(total_marks/4)
grade=" "

if percentage >=90:
    grade="A+"
elif percentage >=80:
    grade="A"
elif percentage >70:
    grade="B"
elif percentage >=60:
    grade="c"
elif percentage >50:
    grade="D"
else:
    grade="F"

if percentage>=50:
    result="pass"
else:
    result="FAIL"

print("\n===== student result=====")
print("Student Name:", name)
print("Total Marks:", total_marks, "/ 400")
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("result:",result)





