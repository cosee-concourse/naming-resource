#! /usr/bin/env python3
import json
from concourse_common import jsonutil
from concourse_common import request
import schemas


def execute():

    valid, payload = jsonutil.load_and_validate_payload(schemas, request.Request.OUT)

    if valid is False:
        return -1

    print(json.dumps([{}]))

    return 0

if __name__ == '__main__':
    exit(execute())