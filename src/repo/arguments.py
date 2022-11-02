""" Input Arguments from command line Module"""

import argparse
import sys


def print_help(unknown, parser):
    """ print help if an unknown argument is passed
    unknown --> array
    parser --> argparser object
    """
    if any(unknown):
        parser.print_help()
        sys.exit(1)


def arguments():
    """ Define arguments from argparse """
    parser = argparse.ArgumentParser(description='Process data')
    parser.add_argument("--pipeline", type=str, choices=["netflix"],
                        help="Representa qual caso de uso"
                        "de processamento irá ser iniciado")

    args, unknown = parser.parse_known_args()
    print_help(unknown, parser)
    args = vars(args)
    return args
