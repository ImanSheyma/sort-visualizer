from algorithm import Algorithm

class BubbleSort(Algorithm):
    def algorithm(self):
        n = len(self.array)
        for i in range(n):
            for j in range(n-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
            self.update_view(self.array[j], self.array[j+1])    