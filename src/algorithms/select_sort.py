from rectangle import Rectangle
from .algorithm import Algorithm

class SelectSort(Algorithm):
    def algorithm(self, rects: list[Rectangle]):
        num_rects = len(rects)
    
        for i in range(num_rects):
            min_index = i
            rects[i].curr()
            
            for j in range(i+1, num_rects):
                rects[j].select()
                self.draw(rects)
                
                if rects[j].height < rects[min_index].height:
                    rects[min_index].unselect()
                    min_index = j
                    
                rects[min_index].curr()
                self.draw(rects)
                rects[j].unselect()
                
                yield
        
            rects[i].x, rects[min_index].x  = rects[min_index].x, rects[i].x
            rects[i], rects[min_index] = rects[min_index], rects[i]
            
            rects[min_index].unselect()
            rects[i].set_sorted()
            
            self.draw(rects)