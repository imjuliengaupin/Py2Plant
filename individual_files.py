
from plant_uml_file import PlantUmlFile


class IndividualFiles(PlantUmlFile):
    def __init__(self, py_files, file_name, index):
        super().__init__(py_files, file_name, index)

    def __str__(self):
        return super().__str__()
