name = input("enter student's name")

rollnumber = input("roll number")
coursename = input("course name")
totalmarks = float (input("total marks"))

print 
if totalmarks >= 40:
    result = "pass"
else:                                   
     result = "fail"

print("student name : {}" . format  (name))
print("roll number : {}" . format (rollnumber))
print("course name : {}" . format  (coursename))
print("totalmarks : {} " . format (totalmarks) )
print("result : {}" . format (result))

