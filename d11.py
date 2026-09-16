def get_valid_value(prompt):
    while True:
        try:
            value = float(input(prompt))

            if 0 <= value <= 100:
                return value

            print("Value must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


marks = get_valid_value("Enter marks obtained (0-100): ")
attendance = get_valid_value("Enter attendance percentage (0-100): ")

# Assign grade and performance category based on marks
if marks >= 90:
    grade = "A"
    category = "Excellent"
elif marks >= 75:
    grade = "B"
    category = "Very Good"
elif marks >= 60:
    grade = "C"
    category = "Good"
elif marks >= 40:
    grade = "D"
    category = "Average"
else:
    grade = "F"
    category = "Poor"

# Determine pass/fail status
if marks >= 40 and attendance >= 75:
    result = "Passed"
else:
    result = "Failed"

print("\n--- Student Evaluation ---")
print("Marks:", marks)
print("Attendance:", attendance, "%")
print("Result:", result)
print("Grade:", grade)
print("Performance Category:", category)