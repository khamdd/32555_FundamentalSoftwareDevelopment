import re
import json
import os
import random

# Regular expressions for email and password validation
EMAIL_REGEX = r"^[a-zA-Z]+\.[a-zA-Z]+@university\.com$"
PASSWORD_REGEX = r"^[A-Z][a-zA-Z]{4,}\d{3,}$"

# Subject class
class Subject:
    def __init__(self, name):
        self.id = f"{random.randint(1, 999):03d}"  # 3-digit subject ID
        self.name = name
        self.mark = random.randint(25, 100)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.mark >= 85:
            return 'HD'
        elif self.mark >= 75:
            return 'D'
        elif self.mark >= 65:
            return 'C'
        elif self.mark >= 50:
            return 'P'
        else:
            return 'F'

# Student class
class Student:
    def __init__(self, name, email, password):
        self.id = f"{random.randint(1, 999999):06d}"  # Generate a 6-digit student ID
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []  # A list of enrolled subjects (max 4 subjects)

# Database class
class Database:
    def __init__(self, filename='students.data'):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Warning: students.data is empty or invalid. Initializing empty data.")
                return []
        else:
            return []

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump([student.__dict__ for student in self.students], file)

    def add_student(self, student):
        if any(s['email'] == student.email for s in self.students):
            print(f"Student {student.name} already exists.")
        else:
            self.students.append(student)
            self.save_data()
            print(f"Enrolling Student {student.name}")

    def find_student(self, email, password):
        for student in self.students:
            if student['email'] == email and student['password'] == password:
                return student
        return None

    def email_exists(self, email):
        return any(s['email'] == email for s in self.students)

# Controllers
class StudentController:
    def __init__(self, db):
        self.db = db

    def generate_email(self, full_name):
        try:
            first_name, last_name = full_name.lower().split()
            email = f"{first_name}.{last_name}@university.com"
            return email
        except ValueError:
            print("Error: Please enter both first and last name.")
            return None

    def register(self):
        print("\nStudent Sign Up")
        while True:
            print("Enter full name (firstname and secondname): ", end="")
            full_name = input()
            email = self.generate_email(full_name)
            if email:  # Proceed only if a valid email is generated
                print(f"Email: {email}")
                break
        
        while True:
            print("Password: ", end="")
            password = input()
            if not re.match(PASSWORD_REGEX, password):
                print("Incorrect email or password format")
                print(f"Email: {email}")
            else:
                print("email and password formats acceptable")
                break

        if self.db.email_exists(email):
            print(f"Student {full_name} already exists.")
            return

        new_student = Student(full_name, email, password)
        self.db.add_student(new_student)

    def login(self):
        print("\nStudent Sign In")
        
        while True:
            print("Email: ", end="")
            email = input()
            
            print("Password: ", end="")
            password = input()
            
            student = self.db.find_student(email, password)
            
            if student:
                print("email and password formats acceptable")
                # Proceed to the course menu or other actions
                break
            else:
                print("Incorrect email or password format. Please try again.")


# Main function for Student System
def main():
    db = Database()
    controller = StudentController(db)

    while True:
        print("\nUniversity System: (A)dmin, (S)tudent, or (X) Exit: ", end="")
        choice = input().lower()

        if choice == 's':
            print("\nStudent System (1/r/x): ", end="")
            choice = input().lower()
            if choice == 'r':
                controller.register()
            elif choice == '1':
                controller.login()
            elif choice == 'x':
                break
        elif choice == 'x':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
