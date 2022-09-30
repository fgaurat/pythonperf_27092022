

import unittest
import sys
sys.path.append('..')
from Rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def test_rectangle_is_created(self):
        r = Rectangle()
        self.assertIsInstance(r,Rectangle)


    def test_rectangle_longueur_gt_0(self):
        r = Rectangle()
        self.assertGreater(r.longueur,0)

    def test_rectangle_longueur_gt_init_0(self):

        self.assertRaises(AssertionError, Rectangle,1,1)

                

