def collect_student_details(num_students):
    students = []
    for _ in range(num_students):
        student_details = {}
        name = input("Enter student name: ")
        usn = input("Enter USN number: ")
        marks = []
        for subject in ['Che', 'Physics', 'Maths', 'Bio', 'CSE']:
            mark = float(input(f"Enter marks for {subject}: "))
            marks.append(mark)
        student_details['Name'] = name
        student_details['USN'] = usn
        student_details['Marks'] = marks
        students.append(student_details)
        print()  # Print an empty line for separation
    return students

def display_student_details(students):
    for student in students:
        print("Name:", student['Name'])
        print("USN:", student['USN'])
        print("Marks:")
        for i, subject in enumerate(['Che', 'Physics', 'Maths', 'Bio', 'CSE']):
            print(f"{subject}: {student['Marks'][i]}")
        print()  # Print an empty line for separation
num_students = int(input("Enter the number of students: "))
student_details = collect_student_details(num_students)
print("Student Details:")
display_student_details(student_details)
