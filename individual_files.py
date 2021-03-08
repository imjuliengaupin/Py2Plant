
from constants import DEBUG_MODE, UML_PREFIX, UML_SUFFIX, CHILD_CLASS, PARENT_CLASS, NO_PARENT_CLASS, CLASS_MEMBER, CLASS_METHOD, CLASS_INSTANCE
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
        super().pre_uml_content(uml_file)
        self.core_uml_content(uml_file)
        super().post_uml_content(uml_file)

    def core_uml_content(self, uml_file):
        # RESEARCH do i need to convert self to super ?
        for line_of_code in open(self.py_files[self.index], "r"):
            # for each line of code read, ignore the "\n" character escape sequence
            if self.is_newline_found.match(line_of_code):
                continue

            # if a class that has a parent is found ...
            class_found = self.is_class_found.match(line_of_code)
            if class_found:
                super().class_name_validation(class_found.group(
                    CHILD_CLASS), class_found.group(PARENT_CLASS), uml_file)
                continue

            # if a class that has no parents is found ...
            class_w_no_parent_found = self.is_no_parent_class_found.match(
                line_of_code)
            if class_w_no_parent_found:
                super().class_name_validation(
                    class_w_no_parent_found.group(NO_PARENT_CLASS), "", uml_file)
                continue

            # if a class member variable is found ...
            class_member_found = self.is_class_member_found.match(line_of_code)
            if class_member_found and self.class_name:
                super().class_member_validation(class_member_found.group(CLASS_MEMBER))

            # if a class method is found ...
            class_method_found = self.is_class_method_found.match(line_of_code)
            if class_method_found and self.class_name:
                super().class_method_validation(class_method_found.group(CLASS_METHOD), uml_file)
                continue

            # if any class object instantiation is found ...
            class_instantiation_found = self.is_class_instantiated.search(
                line_of_code)
            if class_instantiation_found and self.class_name:
                super().class_instance_validation(class_instantiation_found.group(CLASS_INSTANCE))
