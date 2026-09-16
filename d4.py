attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter marks obtained: "))

if attendance >= 75 and marks >= 40:
    print("Student is eligible for the examination.")
else:
    print("Student is not eligible for the examination.")