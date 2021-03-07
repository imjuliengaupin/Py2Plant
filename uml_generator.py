
from constants import DEBUG_MODE, MIN_ARGS_REQUIRED
from imports import os, sys
from individual_files import IndividualFiles


class UmlGenerator(object):
    def __init__(self, argvs):
        self.run(argvs)

    def __str__(self):
        pass

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
                file_name = os.path.basename(argv.split(".")[0])
                index = argvs.index(argv)

                if DEBUG_MODE:
                    print("hit")
                else:
                    IndividualFiles(argvs, file_name, index)
