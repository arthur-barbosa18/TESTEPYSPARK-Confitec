""" Constants Module"""

import os
from src import __file__ as module_file

NETFLIX = "netflix"

MODULE_PARENT = os.path.abspath(os.path.join(module_file, os.pardir))

BASE_PATH = os.path.abspath(os.path.join(MODULE_PARENT, os.pardir))
MODULE_PATH = os.path.dirname(module_file)
