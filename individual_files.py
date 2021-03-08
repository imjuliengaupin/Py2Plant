
from constants import DEBUG_MODE, UML_PREFIX, UML_SUFFIX
from plant_uml_file import PlantUmlFile


class IndividualFiles(PlantUmlFile):
    def __init__(self, py_files, package_name, index):
        super().__init__(py_files, package_name)
        self.index = index

    def __str__(self):
        pass

    def generate_uml_files(self):
        with open(f"Py2Plant/plantuml/{self.package_name}.txt", "w") as uml_file:
            if DEBUG_MODE:
                print(f"{UML_PREFIX}")
                self.get_uml_content(uml_file)
                print(f"{UML_SUFFIX}")
            else:
                uml_file.write(f"{UML_PREFIX}\n")
                self.get_uml_content(uml_file)
                uml_file.write(f"{UML_SUFFIX}")
                uml_file.close()

    def get_uml_content(self, uml_file):
        self.pre_uml_content(uml_file)
        super().post_uml_content(uml_file)

    def pre_uml_content(self, uml_file):
        if DEBUG_MODE:
            print(f"package {self.package_name} {{")
        else:
            # TEST define here or in super().__init__() ?
            """self.class_name = None
            self.class_members = {}"""
            uml_file.write(f"package {self.package_name} {{\n")
