import sys
from concourse_common import common
import json
import json_output
import os
from model import Model


def execute(filepath):

    try:
        model = Model()
    except:
        return -1

    if model.get_prefix() is (None or ""):
        common.log("invalid Prefix", file=sys.stderr)
        return -1

    common.log("returned version:" + json_output.inout_output(model.get_version(), model.get_prefix()))
    with open(os.path.join(filepath, "name"), "w+") as file:
        file.write(json_output.inout_output(model.get_version(), model.get_prefix()))
    print(json.dumps({"version" : {"version" : model.get_version()}}))
    

    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        common.log("Wrong number of arguments!")
        exit(-1)
    exit(execute(sys.argv[1]))