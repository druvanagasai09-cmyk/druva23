def student_details (name, course, marks) :
    print("Name:", name)
    print("Course:", course)
    print("Marks:", marks)

# Positional arguments 
student_details("Ramcharan", "CSE", 89)

print()


#keyword arguments
student_details(marks=89 ,name="Ramcharan" ,course="CSE")