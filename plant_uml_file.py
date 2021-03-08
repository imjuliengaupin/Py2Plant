
from constants import DEBUG_MODE


class PlantUmlFile(object):
    def __init__(self, py_files, package_name):
        self.py_files = py_files
        self.package_name = package_name
        self.classes = []

        # TEST define here or in pre_uml_content() ?
        self.class_name = None
        self.class_members = {}

    def __str__(self):
        pass

    def post_uml_content(self, uml_file):
        for class_name, class_members in self.class_members.items():
            for class_member in class_members:
                if DEBUG_MODE:
                    # TEST remove the '\n' ?
                    print(f"{class_name} : {class_member}\n")
                else:
                    uml_file.write(f"{class_name} : {class_member}\n")

        if DEBUG_MODE:
            print("}")
        else:
            uml_file.write("}\n")
