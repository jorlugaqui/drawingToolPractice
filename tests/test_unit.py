#! -*- coding: utf-8 -*-

""" Unit tests."""

import unittest2


from models.illustrator import Canvas


class TestCanvasModel(unittest2.TestCase):
    can = None

    def setUp(self):
        self.can = Canvas(20, 4)

    def tearDown(self):
        del self.can

    def test_create_canvas(self):
        self.assertEqual(self.can.w, 20)
        self.assertEqual(self.can.h, 4)

    def test_get_canvas(self):
        base_canvas = [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
             '-', '-', '-', '-', '-', '-', '-', '-', '-'],

            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
             ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],

            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
             ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],

            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
             ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],

            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
             ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],

            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
             '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ]
        printed = self.can.get_canvas()
        self.assertEqual(len(base_canvas[0]), len(printed[0]))
        self.assertEqual(sorted(base_canvas), sorted(printed))


if __name__ == '__main__':
    unittest2.main()