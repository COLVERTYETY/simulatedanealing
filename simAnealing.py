import numpy as np

class searcher2D():
    def __init__(self,xmax,ymax):
        self.xmax = xmax
        self.ymax = ymax
        self.s = self.randomneighbour()
        self.snew = self.randomneighbour()
        self.es=0.6
        self.esnew=0.7

    def randomneighbour(self):
        temp = np.random.rand(2)
        temp[0]=int(temp[0]*self.xmax)
        temp[1]=int(temp[1]*self.ymax)
        return temp
    
    def evaluate(self,T):
        value = np.exp(-1*(self.esnew/255-self.es/255)/T)
        if value>=np.random.randint(10000)/10000:
            self.s = self.snew
            self.snew = self.randomneighbour()