marks = float(input("Enter marks obtained (0-100): "))

if marks >= 90:
    performance = "Excellent"
elif marks >= 75:
    performance = "Very Good"
elif marks >= 60:
    performance = "Good"
elif marks >= 40:
    performance = "Average"
else:
    performance = "Poor"

print("Student's performance:", performance)