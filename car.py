from abc import abstractmethod

from serviceable import Serviceable


class Car(Serviceable):
    
    def __init__(self):
        self._engine: None
        self._battery: None

    def needs_service(self):
        if self._engine.needs_service() or self._battery.needs_service():
            return True
        return False
