"""
This file is the main file for the Tidy OS file driver. To ensure system security, do not forcibly delete the file
For the security of the files and the system, we backed up the files


-- This is the translation of Youdao Dictionary
"""

import os
import pathlib
import shutil
import sys


def file_exist(*path: str):
    """
    说明:
    对提供的文件目录下的文件进行检查，检擦是否存在 文件 或 文件夹
    """
    i = 0
    exist_list = []
    if len(path) == 1:
        if os.path.exists(path[0]):
            return True
        else:
            return False
    else:
        for i in range(len(path)):

            if os.path.exists(path[i]):
                exist_list.append(True)

            else:
                exist_list.append(False)
        return tuple(exist_list)


def isfile(*filename):
    i = 0
    is_file_list = []
    if len(filename) == 1:

        if os.path.isfile(filename[0]):
            return True
        else:
            return False
    else:
        for i in range(len(filename)):
            if os.path.isfile(filename[i]):
                is_file_list.append(True)
            else:
                is_file_list.append(False)
        return tuple(is_file_list)


def mkdir(path: str):
    """
    在提供的路径下创建指定文件夹

    调用方法:

    mkdir(filename)


    :param path: 路径+创建文件夹的名称
    :return:状态码
    """

    if not file_exist(path):
        # noinspection PyBroadException
        try:
            os.makedirs(path)
        except:
            return 402
    elif file_exist(path):
        return 401
    else:
        return


def touch(path: str):
    """
    在提供的路径下创建文件

    调用方法:

    touch(filename)

    :param path: 路径+创建文件的名称
    :return:状态码
    """

    old_filename = path
    filename_list_len = path.split('/')
    path = path[0:len(path) - len(filename_list_len[len(filename_list_len) - 1])]

    if not file_exist(path):
        mkdir(path)
        with open(old_filename, 'w') as touch_file_not_exist:
            touch_file_not_exist.write('')
            touch_file_not_exist.close()
    elif file_exist(path):
        if file_exist(old_filename):
            return 401
        elif not file_exist(old_filename):
            with open(old_filename, 'w') as touch_file_exist:
                touch_file_exist.write('')
                touch_file_exist.close()
    else:
        return 402


def read(path: str, mode='r'):
    """
    在提供的路径下入读取指定文件


    调用方法:


    FileDrive.read(filename,mode)

    :param path: 路径+读取文件的名称
    :param mode: 模式(可选参数) 默认为 r ,传入 r 或 rb
    :return: 读取成功时返回读取的文件的内容，报错时返回状态码
    """
    if isfile(path):
        if mode == 'r':
            if file_exist(path):
                with open(file=path, mode='r', encoding='utf-8') as read_file:
                    return_content = read_file.read()
                    read_file.close()
                return return_content
            else:
                return 402
        elif mode == 'rb':
            if file_exist(path):
                with open(file=path, mode='rb') as read_file:
                    return_content = read_file.read()
                    read_file.close()
                return return_content
            else:
                return 402

        else:
            return 404
    else:
        return 404


def write(path: str, content: str, mode='o'):
    """
    对指定的文件进行写入操作


    调用方法:


    FileDrive.write(filename,mode) :param path: 路径+写入文件的名称 :param content: 写入的内容 :param mode: 模式(可选参数) 默认为 o (
    overwrite) ,传入 o (overwrite) a (add write)

    """
    if mode == 'o':
        if file_exist(path):
            with open(path, 'w') as write_overwrite:
                write_overwrite.write(content)
                write_overwrite.close()
        else:
            touch(path)
            with open(path, 'w') as write_overwrite:
                write_overwrite.write(content)
                write_overwrite.close()
    elif mode == 'a':
        if file_exist(path):
            with open(path, 'a') as write_add_write:
                write_add_write.write(content)
                write_add_write.close()
        else:
            touch(path)
            with open(path, 'a') as write_add_write:
                write_add_write.write(content)
                write_add_write.close()
    else:
        pass


def remove(mode, path):
    status = 0
    if mode == 'f':
        try:
            pathlib.Path.unlink(path)
            status = 1
        except:
            status = 2

    elif mode == 't':
        shutil.rmtree(path)



if __name__ == '__main__':
    pass
