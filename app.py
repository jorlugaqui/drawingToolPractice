#! -*- coding: utf-8 -*-

"""Main Controller."""

from models.illustrator import Illustrator


def get_menu():
    text = """***Main Menu***
    Create a new canvas (C).
    Create a new Line (L).
    Create a new Rectangle (R).
    Fill Area (B).
    Quit (Q).
    Enter your choice (C, L, R, B, Q): """
    return text


def get_option(option='menu'):
    txt = ''
    if option == 'menu':
        txt = get_menu()
    elif option == 'command':
        txt = 'Enter command: '
    return raw_input(txt)


def get_canvas(illustrator, command):
    return illustrator.draw_canvas(command)


def main():
    illustrator = Illustrator()
    option = -1
    while not option == 'Q':
        option = get_option()
        if option.upper() in ('C', 'L', 'R', 'B'):
            command = get_option(option='command')
            print get_canvas(illustrator, command)

if __name__ == '__main__':
    main()