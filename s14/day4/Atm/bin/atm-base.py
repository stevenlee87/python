import os
import sys
__author__ = "Steven Lee"

print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
# import conf
# import core

from conf import settings
from core import main

main.login()
