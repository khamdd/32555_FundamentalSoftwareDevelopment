import random

class Subject:
    def __init__(self):
        self.subjectid = random.randint(1, 999)
        self.mark = random.randint(25, 100)
        if self.mark < 50:
            self.grade = 'F'
        elif self.mark >= 50 and self.mark < 65:
            self.grade = 'P'
        elif self.mark >= 65 and self.mark < 75:
            self.grade = 'CR'
        elif self.mark >= 75 and self.mark < 85:
            self.grade = 'D'
        elif self.mark >= 85:
            self.grade = 'HD'
