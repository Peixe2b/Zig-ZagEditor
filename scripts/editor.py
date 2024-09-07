from enums.modes import Mode
from scripts.config import get_system_info

from rich.console import Console
from rich.text import Text


class EventController:
    def __init__(self) -> None:
        pass


class TextEditor:
    """
    A class for managing text editor operations.
    """
    def __init__(self) -> None:
        # Private vars
        self.__modes = (Mode.VISUAL, Mode.COMMAND, Mode.EDIT)
        self.__console = Console()
        self.__lines = 1
        self.__cols = 0
        self.__rows = 0
        
        # Public vars
        self.mode = self.__modes[0]
        self.running = True
        self.current_filename = ""
        self.system_info = get_system_info()

        # Classes
        self.eventController = EventController()

    def run_beta(self):
        print("Running Editor")
        self.__console.clear()

        while self.running:
            try:
                self.__console.input("{} ".format(self.__lines))
                self.__lines = self.__lines + 1
            except KeyboardInterrupt:
                print("Program ending...")
                self.running = False    
        # Discart function
        
    def save_and_exit(self):
        pass

    def force_exit(self):
        pass
    
    # Getters and setters
    def get_modes(self) -> tuple:
        return self.__modes
    
    def get_current_mode(self) -> Mode:
        return self.mode
    
    def set_mode(self, mode: Mode):
        self.mode = mode
