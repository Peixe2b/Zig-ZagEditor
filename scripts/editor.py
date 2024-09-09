from os import system
from typing import Any

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from enums.modes import Mode
from scripts.config import get_system_info, AUTOCOMPLETE_PYTHON
from scripts.event import TextInsertEvent, TextDeleteEvent, CommandEvent, CursorMoveEvent, FileSaveEvent
from interfaces.ievent import IEvent


class EventController(object):
    """
    A class for managing editor events.
    """

    def __init__(self, editor: Any) -> None:
        self.editor: Any = editor
        self.event_type: str = "" # Event Type
        self.event_data: str = "" # Event Data
        self.event_handler = None # Event handler

    def initialize(self) -> None:
        self.event: IEvent = TextInsertEvent(self.event_data)
        self.word_completor = WordCompleter(AUTOCOMPLETE_PYTHON, ignore_case=True)
        self.event_handler = self.event.handle_event()
    
    def get_user_input(self) -> str:
        user_key = prompt(f"{self.editor.get_lines()} ", completer=self.word_completor)
        self.editor.update_lines()
        self.set_event(
            self.event.get_event_type(),
            user_key
        )
        return self.event_data
    
    def save_and_exit(self) -> None:
        pass

    def force_exit(self) -> None:
        pass

    def set_event(self, event_type: str, event_data: str):
        self.event_data = event_data
        self.event_type = event_type


class TextEditor(object):
    """
    A class for managing text editor operations.
    """
    def __init__(self) -> None:
        # Private vars
        self.__modes: tuple = (Mode.VISUAL, Mode.COMMAND, Mode.EDIT)
        self.__lines: int = 1
        self.__cursor_x: int = 0
        self.__cursor_y: int = 0
        
        # Public vars
        self.mode: Mode = self.__modes[2]
        self.running: bool = True
        self.current_filename: str = ""
        self.system_info: tuple = get_system_info()
        self.text: list = []
        self.cols: int = 0
        self.rows: int = 0
        
        # Classes
        self.eventController: EventController = EventController(self)

        # Initialize
        self.eventController.initialize()

    def run(self) -> None: # Run program
        system("clear")
        while self.running and self.mode == Mode.EDIT:
            user_input_type: str = self.eventController.get_user_input()                   
            self.__cursor_x = self.__cursor_x + 1
        
    def update_lines(self) -> None:
        self.__lines += 1

    # ----- Getters and setters ----- #
    def get_modes(self) -> tuple:
        """
        Retrieves the available modes for the text editor.

        Returns:
            tuple: A tuple containing the available modes (Mode.VISUAL, Mode.COMMAND, Mode.EDIT).
        """
        return self.__modes

    def get_current_mode(self) -> Mode:
        return self.mode
    
    def get_cursor_y(self) -> int:
        """
        Get the current cursor y position.

        Returns:
            int: The current cursor y position.
        """
        return self.__cursor_y
    
    def get_cursor_x(self) -> int:
        """
        Get the current cursor x position.

        Returns:
            int: The current cursor x position.
        """
        return self.__cursor_x

    def get_lines(self) -> int:
        """
        Get the current number of lines in the text editor.

        Returns:
            int: The current number of lines.
        """
        return self.__lines
    
    def set_mode(self, mode: Mode):
        self.mode = mode
