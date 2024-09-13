from os import system
from typing import Any

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from scripts.config import AUTOCOMPLETE_PYTHON
from scripts.event import TextInsertEvent
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
        user_key = prompt(">>> ", completer=self.word_completor)
        self.set_event(
            self.event.get_event_type(),
            user_key
        )
        return user_key

    def set_event(self, event_type: str, event_data: str):
        self.event_data = event_data
        self.event_type = event_type


class TextEditor(object):
    """
    A class for managing text editor operations.
    """
    def __init__(self) -> None:
        # Private vars
        self.__cursor_x: int = 0
        self.__cursor_y: int = 0
        
        # Public vars
        self.running: bool = True
        
        # Classes
        self.eventController: EventController = EventController(self)

        # Initialize
        self.eventController.initialize()

    def run(self) -> None: # Run program
        system("clear")
        while self.running:
            try:
                user_input: str = self.eventController.get_user_input()
                exec(user_input)              
                self.__cursor_x = self.__cursor_x + 1
            except KeyboardInterrupt:
                print("Program end")
                self.running = False
            except:
                print("Error in command")

    # ----- Getters and setters ----- #
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
