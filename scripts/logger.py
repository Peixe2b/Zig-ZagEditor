from logging import Logger


class Log:
    def __init__(self) -> None:
        pass

    def log_error(self, msg):
        print("Problems in ZigZag ;-;")
        Logger.error(self, msg)

    def log_info(self, msg):
        Logger.info(self, msg)

    def log_debug(self, msg):
        Logger.debug(self, msg)
   