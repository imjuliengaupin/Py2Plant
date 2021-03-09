
from constants import DEBUG_MODE
from imports import re


class PlantUmlFile(object):
    def __init__(self, py_files, package_name):
        self.py_files = py_files
        self.package_name = package_name
        self.class_name = None
        self.classes = []
        self.no_parent_classes = ["object", ""]
        self.class_members = {}
        self.class_relationships = {}
        self.parents = {}

        # regexp's
        self.is_newline_found = re.compile(r"^\s*(:?$|#|raise|print)")
        self.is_builtin_method = re.compile(r"^__[\w_]+__")
        self.is_private_class_member = re.compile(r"^_[\w\d_]+")
        self.is_class_found = re.compile(
            r"^class\s+([\w\d]+)\(\s*([\w\d\._]+)\s*\):")
        self.is_no_parent_class_found = re.compile(r"^class\s+([\w\d]+)\s*:")
        self.is_class_member_found = re.compile(r"^\s+self.([_\w]+)\s*=")
        self.is_class_method_found = re.compile(r"^\s+def (\w+)\(.*\):")
        self.is_class_instantiated = re.compile(
            r"((:?[A-Z]+[a-z0-9]+)+)\(.*\)")

    def __str__(self):
        return str(f"""file list: {self.py_files}\npackage name: {self.package_name}\nclass name: {self.class_name}\nclasses: {self.classes}\nclasses (no parent): {self.no_parent_classes}\nclass members: {self.class_members}\nclass relationships: {self.class_relationships}\nparents: {self.parents}""")

    def pre_uml_content(self, uml_file):
        # RESEARCH utilizing html/css for diagram components
        # https://plantuml.com/component-diagram
        # https://plantuml.com/style-evolution
        if DEBUG_MODE:
            print(f"package {self.package_name} {{")
        else:
            # TEST define here or in __init__() ? previously here by default
            # self.class_name = None
            # self.class_members = {}
            uml_file.write(f"package {self.package_name} {{\n")

    def post_uml_content(self, uml_file):
        for class_name, class_members in self.class_members.items():
            for class_member in class_members:
                if DEBUG_MODE:
                    print(f"{class_name} : {class_member}")
                else:
                    uml_file.write(f"{class_name} : {class_member}\n")

        if DEBUG_MODE:
            print("}")
        else:
            uml_file.write("}\n")

    def post_uml_relationship_content(self, uml_file):
        for child_class, parent_class in self.parents.items():
            if DEBUG_MODE:
                print(f"{parent_class} <|-- {child_class}")
            else:
                uml_file.write(f"{parent_class} <|-- {child_class}\n")

        # TEST create a test case scenario to understand how this works
        """for related_class, classes in self.class_relationships.items():
            for defined_class_in_file in classes:
                if defined_class_in_file in self.classes and related_class != defined_class_in_file:
                    if DEBUG_MODE:
                        print(f"{related_class} -- {defined_class_in_file}")
                    else:
                        uml_file.write(
                            f"{related_class} -- {defined_class_in_file}\n")"""

    def is_class_attribute_validation(self, class_attribute):
        if self.is_builtin_method.match(class_attribute):
            return f"+{class_attribute}"
        elif self.is_private_class_member.match(class_attribute):
            return f"-{class_attribute}"
        else:
            return f"+{class_attribute}"

    def class_name_validation(self, class_name, parent_class_name, uml_file):
        # TEST create a test case scenario to understand how this works
        # expecting a "package.class_name" format ?
        """if "." in parent_class_name:
            package_and_class_name = parent_class_name.split(".")
            package_name = package_and_class_name[0:-1]
            selected_parent_class_name = package_and_class_name[-1]
            parent_class_name = selected_parent_class_name"""

        # if there are multiple definitions of the same class ...
        if class_name in self.classes:
            return

        self.class_name = class_name
        self.classes.append(class_name)
        # FIXME defined as lists here, but dictionaries in __init__() ?
        self.class_relationships[class_name] = []
        self.class_members[class_name] = []

        if DEBUG_MODE:
            print(f"class {class_name}")
        else:
            uml_file.write(f"class {class_name}\n")

        if parent_class_name not in self.no_parent_classes:
            self.parents[class_name] = parent_class_name

    def class_member_validation(self, class_member_name):
        class_member_name = self.is_class_attribute_validation(
            class_member_name)
        if class_member_name not in self.class_members[self.class_name]:
            self.class_members[self.class_name].append(class_member_name)

    def class_method_validation(self, class_method_name, uml_file):
        class_method_name = self.is_class_attribute_validation(
            class_method_name)
        if DEBUG_MODE:
            print(f"{self.class_name} : {class_method_name}()")
        else:
            uml_file.write(f"{self.class_name} : {class_method_name}()\n")

    # FIXME graph visualization issue on multi-inheritance uml (individual files)
    # e.g. employee <- salary employee <- commission employee
    def class_instance_validation(self, instantiated_class):
        # if code scan identifies when a class object is instantiated ...
        # RESEARCH https://stackoverflow.com/questions/52203260/plantuml-class-diagram-with-multiple-children-any-way-to-bifurcate-the-arrow
        if instantiated_class not in self.class_relationships[self.class_name]:
            self.class_relationships[self.class_name].append(
                instantiated_class)
