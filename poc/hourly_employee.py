
from poc.employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def __str__(self):
        return str(f"""id: {self.id}\nemployee name: {self.name}\nhours worked: {self.hours_worked}\nhour rate: {self.hour_rate}""")

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate
