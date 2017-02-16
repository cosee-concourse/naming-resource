import sys
from concourse_common import common
import json
from model import Model
import os


def execute(filepath):

    try:
        model = Model()
    except:
        return -1

    print(json.dumps({"version" : {"version":  open(os.path.join(filepath, model.get_version_file())).read()}}))

    return 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        common.log("Wrong number of arguments!")
        exit(-1)
    exit(execute(sys.argv[1]))