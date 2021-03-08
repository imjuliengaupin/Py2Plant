
from poc.employee import Employee


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def __str__(self):
        return str(f"""id: {self.id}\nemployee name: {self.name}\nweekly salary: {self.weekly_salary}""")

    def calculate_payroll(self):
        return self.weekly_salary
