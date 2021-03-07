
from constants import DEBUG_MODE, UML_PREFIX, UML_SUFFIX


class PlantUmlFile(object):
    def __init__(self, py_files, file_name, index):
        self.py_files = py_files
        self.file_name = file_name
        self.index = index

        self.generate_uml_file()

    def __str__(self):
        pass

    def generate_uml_file(self):
        with open(f"plantuml/{self.file_name}.txt", "w") as uml_file:
            if DEBUG_MODE:
                print("hit")
            else:
                uml_file.write(f"{UML_PREFIX}\n")

                # TODO uml content generation

                uml_file.write(f"{UML_SUFFIX}")
                uml_file.close()
