import unittest
import random
from tyre.carigan_tyre import CariganTyre


class TestCariganTyre(unittest.TestCase):
    def test_needs_service_true(self):
        tyre_array=[]
        for i in range(4):
            tyre_array.append(random.random())
        tyre= CariganTyre(tyre_array)
        self.assertTrue(tyre.needs_service())

    def test_needs_service_false(self):
        tyre_array=[]
        for i in range(4):
            tyre_array.append(random.random())
        tyre= CariganTyre(tyre_array)
        self.assertFalse(tyre.needs_service())