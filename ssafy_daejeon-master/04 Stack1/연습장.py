class Subset:
    def __init__(self,n):
        self.n = n
        self.bits = [0] * n

    def getbits(self,k):
        if k == self.n:
            return
        
