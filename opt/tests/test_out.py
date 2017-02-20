
import unittest
from unittest.mock import patch
import json

import out
from concourse_common import test_common


class TestInput(unittest.TestCase):

    @patch("out.file_io")
    @patch("out.json")
    def test_json_output(self, mock_io, mock):
        test_common.put_stdin(json.dumps({"source": {"prefix": "test"}, "params": {"version": "1.1.0"}}))
        mock.read.return_value = "1.1.0"
        out.execute("")
        mock_io.dumps.assert_any_call({"version": {"version": "1.1.0"}})


if __name__ == '__main__':
    unittest.main()