from interfaces.ievent import IEvent


class TextInsertEvent(IEvent):
    def __init__(self, text: str):
        self.text = text

    def get_event_type(self) -> str:
        super().get_event_type()
        return "TextInsertEvent"
    
    def get_event_data(self):
        super().get_event_data()
        return {"text": self.text}
    
    def handle_event(self) -> None:
        return super().handle_event()

class TextDeleteEvent(IEvent):
    pass


class CommandEvent(IEvent):
    pass


class CursorMoveEvent(IEvent):
    pass


class FileSaveEvent(IEvent):
    pass
