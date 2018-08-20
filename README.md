
# Snakes Cafe



**Author**: Ben Hurst

**Version**: 1.0.1



## Overview

Snakes Cafe is a command line utility that mimics the functionality of a point of sale (POS) restaurant system using basic Python tools and libraries.

## Getting Started
To run the program, follow these steps:
 1. Clone this repo onto your local.
 2. Navigate into the appropriate directory.
 3. In the terminal, run ```python3 snakes_cafe.py```

## Testing
To run tests (after cloning repo), run ```pytest -vv``` in the terminal. Currently, 23 tests have been written, all of which are passing.

## Architecture

This program was written using Python 3.7 along with the ```textwrap```, ```sys```, and ```uuid``` libraries. Menu items are stored in nested objects within an array so they can easily be added/modified. Other than that, the architecture is very straightforward. Please have a look at the ```snakes_cafe.py``` in this repo for more info.


## Change Log

08-13-2018 4:40pm - Completed basic functionality

08-13-2013 8:25pm - Added entry by item number feature

08-14-2018 9:00pm - Added itemized order print out and remove item functionality

08-15-2018 10:12pm - New feature to load custom menu in .csv format. Also, user now has option to add a specified quantity to each item ordered, which will be checked against inventory.

08-16-2018 10:35pm - Created Class constructor for the Order class. Refactored code accordingly. This class has methods that do everything the code did before, but also a new one that can write a file containing the receipt text.

08-19-2018 11:02pm - Incorporated write functionality as option in UI. Added 23 tests.
