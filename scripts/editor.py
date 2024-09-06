import colorama

from enums.modes import Mode


class TextEditor:
    """
    A class for managing text editor operations.
    """
    def __init__(self) -> None:
        # Private vars
        self.__modes = (Mode.VISUAL, Mode.COMMAND, Mode.EDIT)

        # Public vars
        self.mode = self.__modes[0]
        self.running = False
        self.current_filename = ""
        self.config = None # config = Config()
        
    def run(self):
        print("Running Editor")

    def open_file(self, filename: str) -> str:
        return ""
    
    def save_file(self, filename: str) -> bool:
        return False

    def enter_command(self, command):
        pass

    def exit(self):
        pass

    def get_modes(self) -> tuple:
        return self.__modes
    
    def change_mode(self, mode):
        self.mode = mode
