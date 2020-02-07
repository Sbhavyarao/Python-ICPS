class Employee:
    EmployeeCount = 0
    avg_salary = 0

    def __init__(self, n, f, dept, sal):
        self.name = n
        self.family = f
        self.salary = sal
        self.department = dept
        Employee.EmployeeCount += 1
        Employee.avg_salary += sal

    def avgSalary(self):
        print('Total average salary is ', Employee.avg_salary/Employee.EmployeeCount)


class FullTimeEmployee(Employee):
    def __init__(self, n, f, dept, sal):
        super(FullTimeEmployee, self).__init__(n, f, dept, sal)


emp1 = FullTimeEmployee('Bhavya', 's', 'Acconting', 2000)
emp2 = FullTimeEmployee('Sri', 's', 'Acconting', 5000)
emp3 = FullTimeEmployee('mani', 's', 'Admin', 7000)

emp1.avgSalary()
