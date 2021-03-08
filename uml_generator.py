
from constants import DEBUG_MODE, MIN_ARGS_REQUIRED
from imports import os, sys
from individual_files import IndividualFiles


class UmlGenerator(object):
    def __init__(self, argvs):
        self.run(argvs)

    def __str__(self):
        return super().__str__()

    def get_package_name(self, argv):
        return os.path.basename(argv.split(".")[0])

    def run(self, argvs):
        # if a sufficient number of arguments are not passed ...
        if len(argvs) < MIN_ARGS_REQUIRED:
            # exit the program and print out the requirements
            sys.exit(f"usage -> python3 {argvs[0]} [.py file] [.py file] ...")

        # removes the first argument (which is passed to the program by default)
        argvs.pop(0)

        for argv in argvs:
            if "." not in argv:
                sys.exit("passing a folder instead of a file to argvs list")
            else:
                package_name = self.get_package_name(argv)
                index = argvs.index(argv)

                if DEBUG_MODE:
                    IndividualFiles(argvs, package_name,
                                    index).generate_uml_files()
                else:
                    IndividualFiles(argvs, package_name,
                                    index).generate_uml_files()
