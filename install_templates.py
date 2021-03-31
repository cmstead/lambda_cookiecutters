#!/usr/bin/env python3.8

import os
import sys
import shutil

run_command = os.system

user_directory = os.path.expanduser("~")
cookiecutters_directory = os.path.realpath(os.path.join(user_directory, ".cookiecutters"))

local_directory = os.path.dirname(os.path.realpath(__file__))

def join_path(path_base, *args):
    return os.path.realpath(os.path.join(local_directory, *args))

def copy_cookiecutter(name):
    source_path = join_path(local_directory, name)
    destination_path = join_path(cookiecutters_directory, name)

    try:
        shutil.rmtree(destination_path)
    except:
        # file probably doesn't exist
        pass

    shutil.copytree(source_path, destination_path)

def run_script():
    copy_cookiecutter("lambda")
    copy_cookiecutter("layer")

if __name__ == "__main__":
    run_script()