"""--------------- Zig/Zag ---------------
usage:
    zigzag.py start
    zigzag.py create <filename>
    zigzag.py open <filename>
    zigzag.py (--help | -h)
    zigzag.py --version
use examples:
    1.
        #   for start application   #
        input in cmd$ python zigzag.py --start
        >> Welcome to ZigZag Text Editor!
    2.
        #   for create a new file   #
        input in cmd$ python zigzag.py --create my_file.txt
        >> File my_file.txt created successfully!
    3.
        #   for open an existing file   #
        input in cmd$ python zigzag.py --open my_file.txt
        >> File my_file.txt opened successfully!
"""

from docopt import docopt
from scripts.editor import TextEditor
from scripts.config import VERSION


def start_program() -> None:
    print('Welcome to ZigZag Text Editor!')
    print("Preparing the application for use. Please wait...")
    editor = TextEditor()
    editor.run()


def create_file(filename) -> None:
    with open(filename, "w") as file:
        file.write("")
        print("File created successfully!")
        file.close()


def open_file(filename) -> None:
    if filename:
        with open(filename, 'r') as file:
            print(file.read())
            file.close()
    else:
        print("Please provide a filename.")


def init(version) -> None:
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

    if args['create']:
        print(f'Creating new file at {args["<filename>"]}')
        create_file(args["<filename>"])
    elif args["start"]:
        start_program()
    elif args["open"]:
        print(f'Opening file... {args["<filename>"]}')
        open_file(args["<filename>"])

# Main function
if __name__ == "__main__":
    init(VERSION) # Initialize terminal
    