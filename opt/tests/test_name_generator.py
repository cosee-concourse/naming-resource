import name_generator
import unittest

class TestOutput(unittest.TestCase):


    def test_output_default(self):
        out = name_generator.generate_default("test", "1.1.2")
        self.assertEquals=(out, "test-1-1-2")

    def test_output_heroku(self):
        out = name_generator.generate_default("test", "1.1.2")
        self.assertEquals=(out, "test_1_1_2")

    def test_output_default_emptyversion(self):
        out = name_generator.generate_default("test", "")
        self.assertEquals=(out, "test-")

    def test_output_heroku_emptyversion(self):
        out = name_generator.generate_default("test", "")
        self.assertEquals=(out, "test_")
