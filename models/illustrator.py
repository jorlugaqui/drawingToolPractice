#! -*- coding: utf-8 -*-

""" Module for managing models."""


class Canvas():
    """Canvas Model."""

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.canvas = []
        self.create_canvas()

    def create_canvas(self):
        horizontal, vertical = self.w + 2, self.h
        self.canvas.append(self.__get_horizontal_lines(horizontal))
        for i in range(0, vertical):
            self.canvas.append(self.__get_vertical_line(horizontal))
        self.canvas.append(self.__get_horizontal_lines(horizontal))

    def get_canvas(self):
        return self.canvas

    def print_canvas(self):
        base = ''
        for i in range(0, self.h + 2):
            base += ''.join(self.canvas[i]) + '\n'
        return base

    @staticmethod
    def __get_horizontal_lines(horizontal):
        return ['-' for i in range(0, horizontal)]

    @staticmethod
    def __get_vertical_line(horizontal):
        major = horizontal - 2
        less = horizontal - (horizontal-1)

        base = [
            '|' if i == less or i == major else ' '
            for i in range(0, horizontal)]

        return base


class Illustrator():
    """Drawing operations."""

    def __init__(self):
        self.canvas = None

    def draw_canvas(self, command):
        try:
            c, w, h = command.split(' ')
            int_w = int(w)
            int_h = int(h)
            self.canvas = Canvas(int_w, int_h)
            return self.canvas.print_canvas()
        except (ValueError, IOError) as e:
            print 'Fatal Error'
            exit(0)

if __name__ == '__main__':
    can = Canvas(20, 4)
    tmp = can.get_canvas()
    print can.print_canvas()