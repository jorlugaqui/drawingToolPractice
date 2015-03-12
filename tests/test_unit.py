#! -*- coding: utf-8 -*-

""" Unit tests."""

import unittest2


from models.illustrator import Canvas


class TestCanvasModel(unittest2.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_canvas(self):
        can = Canvas(2, 3)
        self.assertEqual(can.w, 2)
        self.assertEqual(can.h, 3)
        del can


if __name__ == '__main__':
    unittest2.main()