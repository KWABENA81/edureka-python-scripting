import argparse
"""Greeter
Usage:
    command1.py hello
    command1.py goodby
    command1.py -h | --help
Option:
    -h --help   show this screen
"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
