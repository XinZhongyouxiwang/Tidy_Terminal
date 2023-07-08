import os
import platform
import sys
import git

from . import *

on_system = platform.system()
work_directory = os.getcwd()
work_file = __file__
index_path = work_directory[0:len(work_directory) - (len(work_directory.split('\\')[-1]) + 1)]

if not file.file_exist(index_path):


__all__ = ['file',]
