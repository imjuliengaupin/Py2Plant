#!/usr/bin/env python

import sys

MIN_ARGS_REQUIRED = 2


def run(argvs):
    # if a sufficient number of arguments are not passed ...
    if len(argvs) < MIN_ARGS_REQUIRED:
        # exit the program and print out the requirements
        sys.exit(f"usage -> python3 {argvs[0]} [.py file] [.py file] ...")


if __name__ == "__main__":
    run(sys.argv)
