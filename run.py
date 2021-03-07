#!/usr/bin/env python

from imports import sys
from uml_generator import UmlGenerator


def run(argvs):
    UmlGenerator(argvs)


if __name__ == "__main__":
    run(sys.argv)
