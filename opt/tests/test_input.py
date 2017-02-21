import unittest
import input
from unittest.mock import patch
from concourse_common import test_common
import json

class TestInput(unittest.TestCase):

    @patch("input.file_io")
    def test_call_to_fileIO(self, mock_io):
        test = "test/test"
        test_common.put_stdin(json.dumps({"source": {"prefix": "test"}, "version": {"version": "1.1.0"}}))
        input.execute(test)
        mock_io.write_to_file.assert_any_call(test + "/default", "test_1_1_0")
        mock_io.write_to_file.assert_any_call(test + "/heroku", "test-1-1-0")

    def test_invalid_prefix(self):
        test = "test/test"
        test_common.put_stdin(json.dumps({"source": {"prefix": "tes2234"}, "version": {"version": "1.1.0"}}))
        self.assertEquals(input.execute(test), -1)

    @patch("input.file_io")
    @patch("input.json")
    def test_call_to_json(self, mock_io, mock_io2):
        test = "test/test"
        test_common.put_stdin(json.dumps({"source": {"prefix": "test"}, "version": {"version": "1.1.0"}}))
        input.execute(test)
        mock_io.dumps.assert_any_call({"version": {"version": "1.1.0"}})
