import sys
from concourse_common import common
import json
import os
from model import Model
import name_generator

def write_to_file(filepath, name):
    with open(filepath, "w+") as file:
        file.write(name)

def execute(filepath):

    try:
        model = Model()
    except:
        return -1

    if model.get_prefix() is (None or ""):
        common.log("invalid Prefix", file=sys.stderr)
        return -1

    write_to_file(os.path.join(filepath, "default"),
                  name_generator.generate_default(model.get_version(), model.get_prefix()))

    write_to_file(os.path.join(filepath, "heroku"),
                  name_generator.generate_heroku(model.get_version(), model.get_prefix()))

    print(json.dumps({"version" : {"version" : model.get_version()}}))

    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        common.log("Wrong number of arguments!")
        exit(-1)
    exit(execute(sys.argv[1]))