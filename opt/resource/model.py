from concourse_common import common
import schemas
from enum import Enum

VERSION_JSON_NAME = 'version'


class Model:

    def __init__(self):
        self.payload = common.get_payload()

    def get_version_file(self):
        version = self.payload['params']['version']
        return version

    def get_version(self):
        version = self.payload['version']['version']
        return version

    def get_prefix(self):
        prefix = self.payload['source']['prefix']
        if prefix.isalpha():
            return prefix
        return ""


class Request(Enum):
    CHECK = 1
    IN = 2
    OUT = 3