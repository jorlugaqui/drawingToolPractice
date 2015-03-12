#! -*- coding: utf-8 -*-

""" Module for managing models."""


class Illustrator():
    """Drawing operations."""

    def __init__(self):
        pass


class Canvas():
    """Canvas Model."""

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.canvas = []

    def get_canvas(self):
        horizontal, vertical = self.w + 2, self.h
        self.canvas.append(self.__get_horizontal_lines(horizontal))
        for i in range(0, vertical):
            self.canvas.append(self.__get_vertical_line(horizontal, vertical))
        self.canvas.append(self.__get_horizontal_lines(horizontal))
        return self.canvas

    @staticmethod
    def __get_horizontal_lines(horizontal):
        return ['-' for i in range(0, horizontal)]

    @staticmethod
    def __get_vertical_line(horizontal, vertical):
        major = horizontal - 2
        less = horizontal - (horizontal-1)

        base = [
            '|' if i == less or i == major else ' '
            for i in range(0, horizontal)]

        return base

if __name__ == '__main__':
    can = Canvas(3, 4)
    print can.get_canvas()