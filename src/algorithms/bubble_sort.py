from .algorithm import Algorithm
from rectangle import Rectangle

class BubbleSort(Algorithm):
    def algorithm(self, rects: list[Rectangle]):
        num_rects = len(rects)
    
        for i in range(num_rects):
            for j in range(num_rects-i-1):
                rects[j].curr()
                rects[j+1].select()
                self.draw(rects)
                yield
                
                if rects[j].height > rects[j+1].height:
                    rects[j].x, rects[j+1].x  = rects[j+1].x, rects[j].x
                    rects[j], rects[j+1] = rects[j+1], rects[j]

                self.draw(rects)
                rects[j].unselect()
                yield

            rects[num_rects-i-1].set_sorted()
            self.draw(rects)    