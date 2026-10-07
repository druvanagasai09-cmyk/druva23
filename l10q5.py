def calculate_total(marks) :
    return sum(marks)

def calculate_average(marks) :
    return sum(marks) / len(marks)

def calculate_percentage(marks, total_marks) :
    return (sum(marks) / total_marks) * 100

marks = {}

for i in range (3) :
    marks = float(input(f"enter marks for subject {i + 1} :"))
    marks.append (mark)

total_marks = 300

total = calculate_total(marks)
average= calculate_average(marks)
percentage = calculate_percentage(marks , total_marks)

print("\n===== ACADEMIC SUMMARY =====")
print("total marks obtained :", total)
print("average marks :", average)
print("percentage :", percentage , "%")

 