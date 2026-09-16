marks = float(input("Enter marks obtained (0-100): "))

if 0 <= marks <= 100:
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

    print("Performance category:", category)
else:
    print("Invalid marks. Please enter a value between 0 and 100.")