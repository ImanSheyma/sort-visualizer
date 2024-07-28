#colors
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (125, 0, 125)
LIGHT_BLUE = (64, 225, 200)


class Rectangle:
    def __init__(self, x, width, height) -> None:
        self.color = PURPLE
        self.x = x
        self.width = width
        self.height = height
        
        
    def select(self):
        self.color = BLUE
        
        
    def unselect(self):
        self.color = PURPLE
        
    
    def set_smallest(self):
        self.color = LIGHT_BLUE
        
    
    def set_sorted(self):
        self.color = GREEN