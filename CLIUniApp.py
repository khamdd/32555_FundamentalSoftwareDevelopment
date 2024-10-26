from src.models.student import Student


class User:
    def __init__(self, name):
        pass




if __name__ == "__main__":
    student = Student(123, "Tim", "tim.sun@university.com", "utspassword", [])
    exit = False
    while not exit:
        option = input("Student Course Menu c/e/r/s/x: ")
        print(option)
        if option == "c":
            student.change()
        elif option == "e":
            student.enrol()
        elif option == "r":
            student.remove()
        elif option == "s":
            student.show()
        elif option == "x":
            student.exit()
        else:
            print("Invalid option")






