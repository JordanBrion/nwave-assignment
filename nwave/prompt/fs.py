import uuid
import os
import sys

def get_application_directory():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def make_unique_filename(pre, extension):
    return pre + "_" + str(uuid.uuid4()) + extension