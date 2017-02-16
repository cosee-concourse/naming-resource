import unittest
import json_output
import json

class TestJsonOutput(unittest.TestCase):

    def test_outin_output(self):
        output = json_output.inout_output("1.0.0.-rc.1", "test")
        self.assertEqual(output, json.dumps({"default": "test1_0_0__rc_1", "heroku": "test1-0-0--rc-1"}, sort_keys = True))