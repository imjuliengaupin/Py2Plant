
from poc.salary_employee import SalaryEmployee


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self._commission = commission

    def __str__(self):
        return str(f"""id: {self.id}\nemployee name: {self.name}\nweekly salary: {self.weekly_salary}\ncommission: {self.commission}""")

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self._commission
