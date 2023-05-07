import unittest
import random
from tyre.octoprime_tyre import OctoprimeTyre


class TestOctoprimeTyre(unittest.TestCase):
    def test_needs_service_true(self):
        tyre_array=[]
        for i in range(4):
            tyre_array.append(random.random())
        tyre= OctoprimeTyre(tyre_array)
        self.assertTrue(tyre.needs_service())

    def test_needs_service_false(self):
        tyre_array=[]
        for i in range(4):
            tyre_array.append(random.random())
        tyre=OctoprimeTyre(tyre_array)
        self.assertFalse(tyre.needs_service())