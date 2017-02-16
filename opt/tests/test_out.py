
import unittest

import out
from concourse_common import test_common


class TestInput(unittest.TestCase):

    def test_invalid_json(self):
        test_common.put_stdin('{"sourcez":{'
                               '"prefix":"test"},'
                               '"version":{"version":"version-v1-dev"}}')

        self.assertEqual(out.execute(""), -1)


if __name__ == '__main__':
    unittest.main()