def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Student's name
student_name = input("Enter the student name: ")

grade_list = []

grade = float(input("Enter a grade: "))
grade_list.append(grade)

grade = float(input("Enter a grade: "))
grade_list.append(grade)

grade = float(input("Enter a grade: "))
grade_list.append(grade)

grade = float(input("Enter a grade: "))
grade_list.append(grade)

grade = float(input("Enter a grade: "))
grade_list.append(grade)

# Average
average = sum(grade_list) / len(grade_list)

letter_grade = get_letter_grade(average)

print(student_name)
print("Average:", f"{average:g}")
print("Letter Grade:", letter_grade)