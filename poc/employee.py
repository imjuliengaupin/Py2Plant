
class Employee(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return str(f"""id: {self.id}\nemployee name: {self.name}""")
