name = input("Enter student's name: ")
roll_number = input("Enter roll number: ")

while True:
    try:
        marks = float(input("Enter marks obtained (0-100): "))
        if 0 <= marks <= 100:
            break
        print("Marks must be between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        attendance = float(input("Enter attendance percentage (0-100): "))
        if 0 <= attendance <= 100:
            break
        print("Attendance must be between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")

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

attendance_status = "Satisfactory" if attendance >= 75 else "Insufficient"
eligibility = (
    "Eligible for examination"
    if attendance >= 75 and marks >= 40
    else "Not eligible for examination"
)

print("\n--- Student Details ---")
print("Name:", name)
print("Roll Number:", roll_number)
print("Grade:", grade)
print("Attendance Status:", attendance_status)
print("Examination Eligibility:", eligibility)