#! -*- coding: utf-8 -*-

""" Unit tests."""

import unittest2


from models.illustrator import Canvas


class TestCanvasModel(unittest2.TestCase):
    can = None

    def setUp(self):
        self.can = Canvas(2, 3)

    def tearDown(self):
        del self.can

    def test_create_canvas(self):
        self.assertEqual(self.can.w, 2)
        self.assertEqual(self.can.h, 3)

    def test_get_canvas(self):
        base_canvas = [
            ['-', '-', '-', '-', '-'],
            [' ', '|', ' ', '|', ' '],
            [' ', '|', ' ', '|', ' '],
            [' ', '|', ' ', '|', ' '],
            [' ', '|', ' ', '|', ' '],
            ['-', '-', '-', '-', '-']
        ]
        self.assertItemsEqual(self.can.get_canvas(), base_canvas)

    def test_print_canvas(self):
        pass


if __name__ == '__main__':
    unittest2.main()