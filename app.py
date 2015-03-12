#! -*- coding: utf-8 -*-

"""Main Controller."""


def get_menu():
    text = "***Main Menu***\n1.Create a new canvas.\n2.Start Drawing.\n3.Quit"
    text += "\nEnter your choice (1, 2, 3): "
    return text


def get_option():
    return input(get_menu())


def main():
    option = -1
    while not option == 3:
        option = get_option()
        print 'option was {}'.format(option)

if __name__ == '__main__':
    main()