from abc import ABC, abstractmethod


class IEvent(ABC):
    @abstractmethod
    def get_event_type(self) -> str:
        """
        This method should be implemented to return a string representing the type of the event.
        The type should be a unique identifier for the event and should be used to differentiate
        between different types of events.
        
        Returns:
            str: A unique identifier for the event type.
        """
        pass

    @abstractmethod
    def get_event_data(self):
        pass

    @abstractmethod
    def handle_event(self):
        """
        Handle the event.
        This method should be implemented to define the specific actions
        that need to be taken when the event is handled.

        Returns:
            None
        """
        pass
