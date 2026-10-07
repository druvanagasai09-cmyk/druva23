passsing_marks = 40

def check_result(marks) :
    status = ""

    if marks >= passsing_marks :
       status = "Pass"
    else :
        status = " fail"

    print ( "results :", status)

marks = float(input("enter student marks :"))
check_result(marks)

print("passing marks :", passsing_marks)  