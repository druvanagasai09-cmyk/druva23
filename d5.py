name = input("Enter student's name: ")
roll_number = input("Enter roll number: ")
marks = float(input("Enter marks obtained: "))
attendance = float(input("Enter attendance percentage: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

if attendance >= 75:
    attendance_status = "Satisfactory"
else:
    attendance_status = "Insufficient"

if attendance >= 75 and marks >= 40:
    eligibility = "Eligible for examination"
else:
    eligibility = "Not eligible for examination"

print("\n--- Student Details ---")
print("Name:", name)
print("Roll Number:", roll_number)
print("Grade:", grade)
print("Attendance Status:", attendance_status)
print("Examination Eligibility:", eligibility)