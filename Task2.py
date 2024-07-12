# Function to input marks for a student
def input_student_data():
    name = input("Enter student's name: ")
    assignment = [int(x) for x in input("Enter assignment marks separated by space: ").split()]
    test = [int(x) for x in input("Enter test marks separated by space: ").split()]
    lab = [float(x) for x in input("Enter lab marks separated by space: ").split()]

    student_data = {
        "name": name,
        "assignment": assignment,
        "test": test,
        "lab": lab
    }

    return student_data

# Function calculates average
def get_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)

# Function calculates total average
def calculate_total_average(students):
    assignment = get_average(students["assignment"])
    test = get_average(students["test"])
    lab = get_average(students["lab"])

    # Return the result based on weightage supplied
    # 10 % from assignments, 70 % from test, 20 % from lab-works
    return (0.1 * assignment + 0.7 * test + 0.2 * lab)

# Calculate letter grade of each student
def assign_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"

# Function to calculate the total average marks of the whole class
def class_average_is(student_list):
    result_list = []

    for student in student_list:
        stud_avg = calculate_total_average(student)
        result_list.append(stud_avg)

    return get_average(result_list)

# Student list consisting the dictionary of all students
students = []

# Input data for each student
for _ in range(5):  # Assuming there are 5 students
    student_data = input_student_data()
    students.append(student_data)

# Iterate through the students list and calculate their respective
# average marks and letter grade
for student in students:
    print(student["name"])
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print("Average marks of %s is : %s " % (student["name"], calculate_total_average(student)))
    print("Letter Grade of %s is : %s" % (student["name"], assign_letter_grade(calculate_total_average(student))))
    print()

# Calculate the average of whole class
class_av = class_average_is(students)

print("Class Average is %s" % (class_av))
print("Letter Grade of the class is %s " % (assign_letter_grade(class_av)))
