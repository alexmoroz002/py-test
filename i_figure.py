from abc import ABC, abstractmethod

class IFigure(ABC):
    @property
    @abstractmethod
    def square(self):
        pass