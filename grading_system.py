mathematics_marks = int(input("Enter the students mathematics marks: "))
english_marks = int(input("Enter the students english marks: "))
science_marks = int(input("Enter the students science marks: "))
socialstudies_marks = int(input("Enter the students socialstudies marks: "))

# average
average_mark = (mathematics_marks + english_marks + science_marks + socialstudies_marks)//4

def student_grading_system():
    if 84 < average_mark <= 100:
        print("The student grade is A")
    elif 74 < average_mark <= 85:
        print("The student grade is B")
    elif 64 < average_mark <= 75:
        print("The student grade is C")
    elif 54 < average_mark <= 65:
        print("The student grade is D")
    elif 49 < average_mark <= 55:
        print("The student grade is E")
    else:
        print("The student grade is F")

student_grading_system()