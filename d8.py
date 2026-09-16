marks = float(input("Enter marks obtained (0-100): "))

if 0 <= marks <= 100:
    if marks >= 40:
        print("Student has passed the examination.")

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        else:
            grade = "D"

        print("Grade:", grade)
    else:
        print("Student has failed the examination.")
        print("Grade: F")
else:
    print("Invalid marks. Please enter a value between 0 and 100.")