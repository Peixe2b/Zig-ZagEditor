import curses

from typing import Any

from enums.modes import Mode
from scripts.config import get_system_info
from scripts.event import TextInsertEvent, TextDeleteEvent, CommandEvent, CursorMoveEvent, FileSaveEvent
from interfaces.ievent import IEvent


class EventController(object):
    """
    A class for managing editor events.
    """

    def __init__(self, editor: Any) -> None:
        self.editor: Any = editor
        self.event_type: str = ""
        self.event_value: str = ""
        self.event_handler = None

        self.operations: dict = {
            ":[save-exit]": self.save_and_exit, 
        }

    def initialize(self) -> None:
        self.event: IEvent = TextInsertEvent(self.event_value)
        self.event_handler = self.event.get_event_data()

    def get_user_input(self) -> str:
        self.event_value = self.editor.get_console().getch(self.editor.get_cursor_y(),
                                                            self.editor.get_cursor_x())
        self.event.text = self.event_value
        self.event_handler = self.event.get_event_data()
        self.event_type = self.event.get_event_type()
        return self.event_type
    
    def save_and_exit(self) -> None:
        pass

    def force_exit(self) -> None:
        pass

    def check_keyboard_key(self, key):
        # 10 -> Enter
        # 263 -> BackScape
        pass


class TextEditor(object):
    """
    A class for managing text editor operations.
    """
    def __init__(self) -> None:
        # Private vars
        self.__modes: tuple = (Mode.VISUAL, Mode.COMMAND, Mode.EDIT)
        self.__console = curses.initscr()
        self.__lines: int = 1
        self.__cols: int = 0
        self.__rows: int = 0
        self.__cursor_x: int = 0
        self.__cursor_y: int = 0
        
        # Public vars
        self.mode: Mode = self.__modes[0]
        self.running: bool = True
        self.current_filename: str = ""
        self.system_info: tuple = get_system_info()
        self.text: list = []
        
        # Classes
        self.eventController: EventController = EventController(self)

        # Initialize
        self.eventController.initialize()
        self.__console.keypad(True)

    def run(self) -> None:
        self.__console.clear()

        while self.running:
            try:
                user_input_type: str = self.eventController.get_user_input()
                self.__cursor_x = self.__cursor_x + 1
                self.__console.refresh()
            except:
                self.__console.keypad(False)
                curses.endwin()
                self.running = False
                    
    # ----- Getters and setters ----- #
    def get_modes(self) -> tuple:
        return self.__modes

    def get_modes(self) -> tuple:#+
        """
        Retrieves the available modes for the text editor.

        Returns:
            tuple: A tuple containing the available modes (Mode.VISUAL, Mode.COMMAND, Mode.EDIT).
        """
        return self.__modes

    def get_current_mode(self) -> Mode:
        return self.mode

    def get_console(self) -> Any:
        return self.__console
    
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
    
    def set_mode(self, mode: Mode):
        self.mode = mode
