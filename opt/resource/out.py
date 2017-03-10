import sys
from concourse_common import common
from concourse_common import jsonutil
from concourse_common import request
import json
import file_io
import schemas


def execute(filepath):

    valid, payload = jsonutil.load_and_validate_payload(schemas, request.Request.OUT)

    if valid is False:
        return -1

    print(json.dumps({"version" : {"version":  file_io.read(filepath, jsonutil.get_params_value(payload, "version"))}}))

    return 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        common.log("Wrong number of arguments!")
        exit(-1)
    exit(execute(sys.argv[1]))