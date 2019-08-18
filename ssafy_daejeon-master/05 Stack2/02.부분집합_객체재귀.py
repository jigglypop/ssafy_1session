
class Subset:
    def __init__(self, n):
        self.n = n
        self.bits = [0] * n

    # getbits 내에 재귀가 있음. 0일 경우와 1일 경우 두가지 경우로 갈라짐
    def genbits(self, k):
        if k == self.n:
            print(self.bits)
            return
        self.bits[k] = 0
        self.genbits(k + 1)
        self.bits[k] = 1
        self.genbits(k + 1)

subset = Subset(3)
subset.genbits(0)
