import unittest
from puncpy.classmodule import MyClass


class MyClassModuleTestCase(unittest.TestCase):
    """Tests for `classmodule.py`."""

    def test(self):
        my_object = MyClass('Mark')
        my_object.say_name()
        self.assertTrue(True)

