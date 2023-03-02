# Q3 - Base class Employee: display()
# Derive - EmployeeDetails with same fn named
class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def display(self):
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)


class EmployeeDetails(Employee):
    def __init__(self, name, basic_salary, allowance, deductions):
        super().__init__(name, basic_salary)
        self.allowance = allowance
        self.deductions = deductions

    def calculate_net_salary(self):
        net_salary = self.basic_salary + self.allowance - self.deductions
        return net_salary

    def display(self):
        super().display()
        print("Allowance:", self.allowance)
        print("Deductions:", self.deductions)
        net_salary = self.calculate_net_salary()
        print("Net Salary:", net_salary)


e = EmployeeDetails("Aniket Pathak", 50000, 10000, 5000)
e.display()