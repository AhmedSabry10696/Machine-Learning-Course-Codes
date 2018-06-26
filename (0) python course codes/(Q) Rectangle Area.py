class rectangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w
        
    def area(self):
        return(self.length*self.width)

r1 = rectangle(10,5)
print(r1.area())        
        