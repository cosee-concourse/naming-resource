import sys
from concourse_common import common
import json
import os
from model import Model
import name_generator
import file_io


def execute(filepath):

    try:
        model = Model()
    except:
        return -1

    if model.get_prefix() is (None or "") or not model.get_prefix().isalpha():
        common.log("invalid Prefix")
        return -1

    file_io.write_to_file(os.path.join(filepath, "default"),
                  name_generator.generate_default(model.get_version(), model.get_prefix()))

    file_io.write_to_file(os.path.join(filepath, "heroku"),
                  name_generator.generate_heroku(model.get_version(), model.get_prefix()))

    print(json.dumps({"version" : {"version" : model.get_version()}}))

    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        common.log("Wrong number of arguments!")
        exit(-1)
    exit(execute(sys.argv[1]))