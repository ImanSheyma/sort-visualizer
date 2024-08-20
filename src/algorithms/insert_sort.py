from rectangle import Rectangle
from .algorithm import Algorithm

class InsertSort(Algorithm):
    def algorithm(self, rects: list[Rectangle]):
        num_rects = len(rects)
    
        if num_rects <= 1:
            return
 
        for i in range(1, num_rects):
            j = i-1
            
            while j >= 0 and rects[j+1].height < rects[j].height:
                #highlight rects as selected
                rects[j+1].select()
                rects[j].curr()
                self.draw(rects)
                yield
                
                #swap
                rects[j].x, rects[j+1].x  = rects[j+1].x, rects[j].x
                rects[j], rects[j+1] = rects[j+1], rects[j]
                self.draw(rects)
                yield
                
                #highlight selected rects as sorted
                rects[j].set_sorted()
                rects[j+1].set_sorted()
                j -= 1
            
            rects[i-1].set_sorted()  
            self.draw(rects)
            
        self.draw(rects)