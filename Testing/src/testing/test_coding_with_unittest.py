from __future__ import absolute_import

import sys
import unittest
from src.examples.coding import division

class TestCode(unittest.TestCase):

    def test_division_with_two_ints(self):
        self.assertEqual(division(2,4), .5)
        self.assertAlmostEqual(division(1,3), .3, places=1)

    @unittest.skip("demonstrating skipping")
    def test_division_wrong_type_string(self):
        self.assertRaises(TypeError, division, 4, "2")

        