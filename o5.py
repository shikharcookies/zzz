class InvalidCGPAException(Exception):
    pass


def promote_student(cgpa):
    try:
        cgpa = float(cgpa)
        if cgpa < 4.5:
            raise InvalidCGPAException("CGPA is below the required threshold (4.5). Promotion denied.")
        else:
            print("Promotion granted!")
    except ValueError:
        print("Invalid input. Please enter a valid CGPA.")
    except InvalidCGPAException as e:
        print(str(e))


cgpa_input = input("Enter the CGPA: ")
promote_student(cgpa_input)
