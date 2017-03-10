import sys
from concourse_common import common
from concourse_common import jsonutil
from concourse_common import request
import json
import os
import name_generator
import file_io
import schemas


def execute(filepath):

    valid, payload = jsonutil.load_and_validate_payload(schemas, request.Request.IN)

    if valid is False:
        return -1

    prefix = jsonutil.get_source_value(payload, "prefix")
    version = jsonutil.get_version(payload, "version")

    if prefix is (None or "") or not prefix.isalpha():
        common.log("invalid Prefix")
        return -1

    file_io.write_to_file(os.path.join(filepath, "default"),
                          name_generator.generate_default(version, prefix))

    file_io.write_to_file(os.path.join(filepath, "heroku"),
                          name_generator.generate_heroku(version, prefix))

    print(json.dumps({"version": {"version": version}}))

    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        common.log("Wrong number of arguments!")
        exit(-1)
    exit(execute(sys.argv[1]))