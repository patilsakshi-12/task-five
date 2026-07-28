# Student Grade Calculator
# This program takes marks for subjects and calculates grade

print("Welcome to Student Grade Calculator")
print("------------------------------------")

while True:
    student_name = input("Enter student name: ")

    while True:
        try:
            num_subjects = int(input("Enter number of subjects: "))
            break
        except:
            print("Please enter a valid whole number.")

    marks_list = []

    for i in range(num_subjects):
        while True:
            try:
                marks = int(input("Enter marks for subject " + str(i + 1) + ": "))
                break
            except:
                print("Please enter a valid number for marks.")
        marks_list.append(marks)

    total_marks = sum(marks_list)
    average = total_marks / num_subjects

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    print("")
    print("---------- REPORT CARD ----------")
    print("Student Name:", student_name)

    for i in range(num_subjects):
        print("Subject", i + 1, "Marks:", marks_list[i])

    print("Total Marks:", total_marks)
    print("Average:", average)
    print("Grade:", grade)
    print("----------------------------------")

    again = input("Do you want to calculate for another student? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for using Student Grade Calculator. Goodbye!")
        break
# Testing GitHub Actions workflows