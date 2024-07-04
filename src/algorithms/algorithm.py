from abc import abstractmethod
from random import sample
import time

class Algorithm:
    def __init__(self):
        self.array = sample(range(512), 512)
        
    
    def run(self):
        self.start_time = time.time()
        self.algorithm()
        time_end = time.time() - self.start_time
        return self.array, time_end
    
    def update_view(self, a, b):
        pass
    
    @abstractmethod
    def algorithm(self):
        raise TypeError(f"method algorithm has not been overwritten.")