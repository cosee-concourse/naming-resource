from concourse_common import jsonutil

VERSION_JSON_NAME = 'version'


class Model:

    def __init__(self):
        self.payload = jsonutil.load_payload()

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
