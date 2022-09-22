from abc import abstractmethod

from serviceable import Serviceable


class Car(Serviceable):
    
    def __init__(self):
        self.engine: None
        self.battery: None
        self.tire = None

    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service():
            return True
        return False
