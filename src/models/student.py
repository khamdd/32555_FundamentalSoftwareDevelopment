from src.models import subject
from src.models.subject import Subject


class Student:
    def __init__(self, id, name, email, password, subjects):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects

    def change(self):
        print("Changing Password")

    def enrol(self):
        if len(self.subjects) >= 4:
            print("Error: Students are only allowed to enrol in 4 subjects")
            return
        print("Enrolling in Subject")
        subject = Subject()
        print("Enrolling in Subject-" + str(subject.subjectid))
        self.subjects.append(subject)

    def remove(self):
        print("Removing Subject")
        option = int(input("Remove Subject by ID: "))
        for subject in self.subjects:
            if subject.subjectid == option:
                self.subjects.remove(subject)
                print("Dropping Subject-" + str(subject.subjectid))
                return
        print("Invalid Subject ID")

    def show(self):
        print("Showing " + str(len(self.subjects)) + "Subjects:")
        for subject in self.subjects:
            print(" Subjects::" + str(subject.subjectid) + " -- Mark = " + str(subject.mark) + " -- grade = " + str(subject.grade))

    def exit(self):
        print("Exiting")