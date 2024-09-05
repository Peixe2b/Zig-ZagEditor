"""--------------- Zig/Zag ---------------
usage:
    zigzag.py --start
    zigzag.py --create <filename>
    zigzag.py --open <filename>
    zigzag.py (-h | --help)
    zigzag.py --version
"""

from docopt import docopt
from scripts.editor import TextEditor
from setup import VERSION


def init(version):
    """
    Initialize the ZigZag application with the given version.

    This function parses command-line arguments using docopt and performs actions
    based on the provided arguments. Currently, it supports creating a new project.

    Parameters:
        version (str): The version of the ZigZag application.

    Returns:
        None
    """
    args = docopt(__doc__, version=version)

    if args['--create']:
        print(f'Creating new file at {args["<filename>"]}')


def start_program():
    print('Welcome to ZigZag Text Editor!')

# Main function
if __name__ == "__main__":
    init(VERSION) # Initialize terminal
    