#! -*- coding: utf-8 -*-

""" Module for managing models."""


class Canvas():
    """Canvas Model."""

    def __init__(self, w, h):
        """
        :param w: The width
        :param h: The height
        """
        self.w = w
        self.h = h
        self.canvas = []
        self.create_canvas()

    def create_canvas(self):
        """ Create a new canvas with the w and h given"""

        horizontal, vertical = self.w + 4, self.h
        self.canvas.append(self.__get_horizontal_lines(horizontal))
        for i in range(0, vertical):
            self.canvas.append(self.__get_vertical_lines(horizontal))
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
        """
        :param horizontal: Number of horizontal positions
        :return: A list with the '-' character per each position
        """
        return ['-' for i in range(0, horizontal)]

    @staticmethod
    def __get_vertical_lines(horizontal):
        """
        :param horizontal: Number of horizontal positions
        :return: A nested list with '|' character according to the size
        """
        major = horizontal - 2
        less = horizontal - (horizontal-1)

        base = [
            '|' if i == less or i == major else ' '
            for i in range(0, horizontal)]

        return base

    def draw_line(self, x1, y1, x2, y2):
        """
        Fill with 'x' all points calculated for a line
        :param x1: First coordinate in x axis
        :param y1: First coordinate in y axis
        :param x2: Second coordinate in x axis
        :param y2: Second coordinate in y axis
        """

        if len(self.canvas) == 0:
            return False

        if y1 != y2 and x1 != x2:
            return False

        points = self.__calculate_line_points(x1, y1, x2, y2)

        if not self.__line_in_boundaries(
                points[0][0],
                points[0][1],
                points[len(points)-1][0],
                points[len(points)-1][1]):
            return False

        return self.draw(points)

    def __line_in_boundaries(self, x1, y1, x2, y2):
        boundaries = self.__get_canvas_boundaries()

        if x1 <= boundaries[0][0] or x1 >= boundaries[1][0]:
            return False

        if y1 <= boundaries[0][1] or y1 >= boundaries[2][1]:
            return False

        if x2 >= boundaries[1][0] or x2 <= boundaries[0][0]:
            return False

        if y2 >= boundaries[2][1] or y2 <= boundaries[0][1]:
            return False

        return True

    def __point_in_boundaries(self, x, y):
        boundaries = self.__get_canvas_boundaries()

        if x <= boundaries[0][0] or x >= boundaries[1][0]:
            return False

        if y <= boundaries[0][1] or y >= boundaries[2][1]:
            return False

        return True

    def __get_canvas_boundaries(self):
        """
        Calculate the boundaries of the canvas
        :return: A list with 4 points, which are the boundaries of the canvas
        """
        boundaries = list()
        boundaries.append((1, 0))
        boundaries.append((len(self.canvas[0])-1, 0))
        boundaries.append((1, len(self.canvas)-1))
        boundaries.append((len(self.canvas[0])-1, len(self.canvas)-1))
        return boundaries

    def draw_rectangle(self, x1, y1, x2, y2):
        """
        Fill with 'x' all points calculated for a rectangle
        :param x1: First coordinate in x axis
        :param y1: First coordinate in y axis
        :param x2: Second coordinate in x axis
        :param y2: Second coordinate in y axis
        """

        if len(self.canvas) == 0:
            return False

        if x1 >= x2 or y1 >= y2:
            return False

        points = self.__calculate_rectangle_points(x1, y1, x2, y2)

        if not self.__line_in_boundaries(
                x1+1,
                y1,
                x2+1,
                y2):
            return False

        return self.draw(points)

    def draw(self, points):
        """
        Fill points with 'x' character
        :param points: The set of coordinates
        :return: True if the process was ok, False in another case
        """
        try:
            rows = len(self.canvas)
            columns = len(self.canvas[0])
            for column in range(0, columns):
                for row in range(0, rows):
                    if (column, row) in points:
                        self.canvas[row][column] = 'x'
        except (ValueError, KeyError, Exception):
            return False

        return True

    @staticmethod
    def __calculate_line_points(x1, y1, x2, y2):
        """
        Calculate all point on which the line will be drawn
        :param x1: First coordinate in x axis
        :param y1: First coordinate in y axis
        :param x2: Second coordinate in x axis
        :param y2: Second coordinate in y axis
        :return: A list of coordinate pairs
        """
        points = list()
        if x1 == x2:
            # Vertical lines, x is static
            for i in range(y1, y2+1):
                points.append((x1+1, i))
        else:
            # Horizontal lines, y is static
            for i in range(x1, x2+1):
                # Sum 1 column because the canvas start in 3 (0, 1, 2) column
                points.append((i+1, y1))
        return points

    @staticmethod
    def __calculate_rectangle_points(x1, y1, x2, y2):
        """
        Calculate all point on which the rectangle will be drawn
        :param x1: First coordinate in x axis
        :param y1: First coordinate in y axis
        :param x2: Second coordinate in x axis
        :param y2: Second coordinate in y axis
        :return: A list of coordinate pairs
        """
        points = set()

        points.add((x1+1, y1))
        points.add((x2+1, y2))

        x = x1 + 1
        y = y1

        # Get horizontal lines
        for i in range(0, (x2+1)-(x1+1)):
            x += 1
            points.add((x, y1))
            points.add((x, y2))

        # Get vertical lines
        for i in range(0, y2-y1):
            y += 1
            points.add((x1+1, y))
            points.add((x2+1, y))

        return list(points)

    def fill_area(self, x, y, char):

        if not self.__point_in_boundaries(x, y) or \
                self.__already_filled(x, y, char):
            return False

        self.canvas[y][x] = char

        self.fill_area(x+1, y, char)
        self.fill_area(x-1, y, char)
        self.fill_area(x, y+1, char)
        self.fill_area(x, y-1, char)
        return True

    def __already_filled(self, x, y, char):
        return self.canvas[y][x] == 'x' \
            or self.canvas[y][x] == '-' \
            or self.canvas[y][x] == '|' \
            or self.canvas[y][x] == char


class Illustrator():
    """Drawing operations."""

    def __init__(self):
        self.canvas = None

    def draw_canvas(self, command):
        """
        :param command: The command
        :return: The Canvas with the command applied
        """
        try:
            c = command.split(' ')
            if c[0].upper() == 'C':

                if self.__validate_number_options(c, 3):
                    raise(Exception('Incorrect format'))

                # Get size
                int_w, int_h = int(c[1]), int(c[2])
                if not self.__validate_format((int_w, int_w)):
                    raise(Exception('Incorrect format'))

                # Create canvas
                self.canvas = Canvas(int_w, int_h)

            elif c[0].upper() == 'L':

                if self.__validate_number_options(c, 5):
                    raise(Exception('Incorrect format'))

                # Get points
                x1, y1, x2, y2 = int(c[1]), int(c[2]), int(c[3]), int(c[4])
                if not self.__validate_format((x1, y1, x2, y2)):
                    raise(Exception('Incorrect format'))

                if not self.canvas:
                    raise(Exception('First create a canvas'))
                if not self.canvas.draw_line(x1, y1, x2, y2):
                    print 'Incorrect points or there is not canvas'

            elif c[0].upper() == 'R':
                if self.__validate_number_options(c, 5):
                    raise(Exception('Incorrect format'))

                # Get points
                x1, y1, x2, y2 = int(c[1]), int(c[2]), int(c[3]), int(c[4])
                if not self.__validate_format((x1, y1, x2, y2)):
                    raise(Exception('Incorrect format'))

                if not self.canvas:
                    raise(Exception('First create a canvas'))
                if not self.canvas.draw_rectangle(x1, y1, x2, y2):
                    print 'Incorrect points or there is not canvas'

            elif c[0].upper() == 'B':
                if self.__validate_number_options(c, 4):
                    raise(Exception('Incorrect format'))

                # Get point and fill character
                x, y = int(c[1]), int(c[2])
                char = c[3]
                if not self.__validate_format((x, y)):
                    raise(Exception('Incorrect format'))

                if not self.canvas:
                    raise(Exception('First create a canvas'))

                x += 1
                if not self.canvas.fill_area(x, y, char):
                    print 'Incorrect point or there is not canvas'

            else:
                raise(ValueError('Incorrect format'))

            return self.canvas.print_canvas()

        except (ValueError, IOError, Exception) as e:
            print 'Fatal Error {}:'.format(e)
            exit(0)

    @staticmethod
    def __validate_number_options(c, n):
        return len(c) != n

    @staticmethod
    def __validate_format(numbers):
        for n in numbers:
            if n < 0:
                return False
        return True


if __name__ == '__main__':
    can = Canvas(20, 4)
    tmp = can.get_canvas()
    print can.print_canvas()
    can.draw_line(1, 2, 6, 2)
    print can.print_canvas()
    can.draw_line(6, 3, 6, 4)
    print can.print_canvas()