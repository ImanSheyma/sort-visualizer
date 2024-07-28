from abc import abstractmethod
from rectangle import Rectangle

class Algorithm:
    def __init__(self, draw):
        self.draw = draw
    
    @abstractmethod
    def algorithm(self, rects: list[Rectangle]):
        raise TypeError(f"method algorithm has not been overwritten.")