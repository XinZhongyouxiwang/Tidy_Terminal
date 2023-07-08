import os
import sys
 
from setuptools import find_packages, setup
 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
 
setup(
  name='Tterminal',
  version='0.1',
  packages=find_packages(),
)
