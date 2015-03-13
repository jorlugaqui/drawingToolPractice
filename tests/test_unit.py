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

    def test_create_canvas(self):
        base_canvas = [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
        ]
        printed = self.can.get_canvas()
        self.assertEqual(len(base_canvas[0]), len(printed[0]))
        self.assertEqual(sorted(base_canvas), sorted(printed))

    def test_draw_line(self):
        # Horizontal line
        base_canvas = [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', '|', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
        ]
        r = self.can.draw_line(1, 2, 6, 2)
        printed = self.can.get_canvas()
        self.assertTrue(r)
        self.assertEqual(len(base_canvas[0]), len(printed[0]))
        self.assertEqual(sorted(base_canvas), sorted(printed))

        # Vertical line
        base_canvas = [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', '|', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
        ]
        r = self.can.draw_line(6, 3, 6, 4)
        printed = self.can.get_canvas()
        self.assertTrue(r)
        self.assertEqual(len(base_canvas[0]), len(printed[0]))
        self.assertEqual(sorted(base_canvas), sorted(printed))

    def test_draw_line_neither_vertical_nor_horizontal_line(self):
        # Neither horizontal nor vertical
        r = self.can.draw_line(1, 3, 3, 4)
        self.assertFalse(r)

    def test_draw_line_there_is_not_canvas(self):
        self.can.canvas = []
        r = self.can.draw_line(6, 3, 6, 4)
        printed = self.can.get_canvas()
        self.assertFalse(r)
        self.assertListEqual(printed, [])

    def test_draw_line_out_canvas(self):
        r = self.can.draw_line(1, 2, 25, 2)
        self.assertFalse(r)

    def test_draw_rectangle(self):
        base_canvas = [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
        ]
        r = self.can.draw_rectangle(16, 1, 20, 3)
        printed = self.can.get_canvas()
        self.assertTrue(r)
        self.assertEqual(len(base_canvas[0]), len(printed[0]))
        self.assertEqual(sorted(base_canvas), sorted(printed))

    def test_draw_rectangle_out_canvas(self):
        r = self.can.draw_rectangle(25, 1, 30, 3)
        self.assertFalse(r)

    def test_bucket_fill(self):
        base_canvas = [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            [' ', '|', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'x', 'x', 'x', 'x', 'x', '|', ' '],
            [' ', '|', 'x', 'x', 'x', 'x', 'x', 'x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'x', ' ', ' ', ' ', 'x', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', 'x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'x', 'x', 'x', 'x', 'x', '|', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', 'x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '|', ' '],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
        ]
        r = self.can.draw_line(1, 2, 6, 2)
        self.assertTrue(r)
        r = self.can.draw_line(6, 3, 6, 4)
        self.assertTrue(r)
        r = self.can.draw_rectangle(16, 1, 20, 3)
        self.assertTrue(r)
        r = self.can.fill_area(10+1, 3, 'o')
        self.assertTrue(r)
        printed = self.can.get_canvas()
        self.assertEqual(sorted(base_canvas), sorted(printed))


if __name__ == '__main__':
    unittest2.main()