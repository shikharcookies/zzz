class InvalidMarkException(Exception):
    pass


def enter_marks():
    marks = []
    for i in range(5):
        try:
            mark = float(input(f"Enter the mark for student {i+1}: "))
            if mark == 0:
                raise InvalidMarkException("Zero mark is not allowed!")
            marks.append(mark)
        except ValueError:
            print("Invalid input. Please enter a valid mark.")
            marks.append(0.0)
        except InvalidMarkException as e:
            print(str(e))
            marks.append(0.0)
    return marks


student_marks = enter_marks()
print("Student Marks:", student_marks)
