from interfaces.ievent import IEvent


class TextInsertEvent(IEvent):
    pass


class TextDeleteEvent(IEvent):
    pass


class CommandEvent(IEvent):
    pass


class CursorMoveEvent(IEvent):
    pass


class FileSaveEvent(IEvent):
    pass
