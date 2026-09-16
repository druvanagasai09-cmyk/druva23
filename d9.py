marks = float(input("Enter marks obtained (0-100): "))
attendance = float(input("Enter attendance percentage (0-100): "))

if 0 <= marks <= 100 and 0 <= attendance <= 100:
    if attendance >= 75:
        if marks >= 90:
            category = "Excellent"
        elif marks >= 75:
            category = "Very Good"
        elif marks >= 60:
            category = "Good"
        elif marks >= 40:
            category = "Average"
        else:
            category = "Poor"

        print("Academic performance:", category)
    else:
        print("Student is not eligible for a performance category.")
        print("Attendance must be at least 75%.")
else:
    print("Invalid input. Marks and attendance must be between 0 and 100.")