# Q2 - 2 base class - student details: input is roll number and student result : input is marksheet
# Derived class - StudentGradeSheet
class StudentDetails:
    def __init__(self, roll_number):
        self.roll_number = roll_number

    def display(self):
        print("Roll Number:", self.roll_number)


class StudentResult:
    def __init__(self, marks):
        self.marks = marks

    def display(self):
        print("Marks:", self.marks)


class StudentGradeSheet(StudentDetails, StudentResult):
    def __init__(self, roll_number, marks):
        StudentDetails.__init__(self, roll_number)
        StudentResult.__init__(self, marks)

    def calculate_grade(self):
        total_marks = sum(self.marks)
        percentage = total_marks / len(self.marks)
        if percentage >= 90:
            grade = 'A+'
        elif percentage >= 80:
            grade = 'A'
        elif percentage >= 70:
            grade = 'B'
        elif percentage >= 60:
            grade = 'C'
        elif percentage >= 50:
            grade = 'D'
        else:
            grade = 'F'
        return grade

    def display(self):
        super().display()
        super(StudentDetails, self).display()
        grade = self.calculate_grade()
        print("Grade:", grade)


s = StudentGradeSheet(123, [80, 85, 90, 95])
s.display()