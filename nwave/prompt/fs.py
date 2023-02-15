import uuid
import os
import sys

def get_application_directory():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def make_unique_filename(pre, extension):
    return pre + "_" + str(uuid.uuid4()) + extension

def get_unique_image_fullpath(self, image_extension):
    return os.path.join(get_application_directory(), make_unique_filename("nwave", image_extension))
