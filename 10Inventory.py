class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def display_details(self):
        print(f'Name: {self.name}')
        print(f'Position: {self.position}')
        print(f'Salary: {self.salary}')
newEmployee = Employee('Henry', 'Manager', '10k')
newEmployee.display_details()