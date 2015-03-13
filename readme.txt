* Pre-requisites

0. Install python 2.7.9 in a new virtualenv
1. Go to the root folder (drawing_tool)
2. Install the dependencies (pip install -Ur requirements.txt)
3. Run all tests: python -m unittest2 discover


* How to run the app?

$ python app.py

* How to use?

Follow next example:

$ python app.py

1.

***Main Menu***
    Create a new canvas (C).
    Create a new Line (L).
    Create a new Rectangle (R).
    Fill Area (B).
    Quit (Q).
    Enter your choice (C, L, R, B, Q): c


2. Enter command: c 20 4

3.

------------------------
 |                    |
 |                    |
 |                    |
 |                    |
------------------------

***Main Menu***
    Create a new canvas (C).
    Create a new Line (L).
    Create a new Rectangle (R).
    Fill Area (B).
    Quit (Q).
    Enter your choice (C, L, R, B, Q): l

4. Enter command: l 6 3 6 4

5.

------------------------
 |                    |
 |                    |
 |     x              |
 |     x              |
------------------------

***Main Menu***
    Create a new canvas (C).
    Create a new Line (L).
    Create a new Rectangle (R).
    Fill Area (B).
    Quit (Q).
    Enter your choice (C, L, R, B, Q): q

