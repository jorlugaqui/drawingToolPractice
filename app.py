#! -*- coding: utf-8 -*-

"""Main Controller."""

from models.illustrator import Illustrator


def get_menu():
    text = "***Main Menu***\n1.Create a new canvas.\n2.Start Drawing.\n3.Quit"
    text += "\nEnter your choice (1, 2, 3): "
    return text


def get_option(option='menu'):
    txt = ''
    if option == 'menu':
        txt = get_menu()
    elif option == 'command':
        txt = 'Enter command: '
    return input(txt)


def get_canvas(illustrator, command):
    return illustrator.draw_canvas(command)


def main():
    illustrator = Illustrator()
    option = -1
    while not option == 3:
        option = get_option()
        if option == 1:
            command = get_option(option='command')
            print get_canvas(illustrator, command)
        if option == 2:
            pass

if __name__ == '__main__':
    main()