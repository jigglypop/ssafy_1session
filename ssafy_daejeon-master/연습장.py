class Stack:
    def __init__(self,size):
        self.size = size
        self.arr = [0] * size
        self.top = -1
    
    def push(self,item):
        self.top += 1
        self.arr[self.top] = item

    def pop(self):
        ret  = self.arr[self.top]
        self.arr[self.top] = 0
        self.top -= 1        
        return ret

    def isEmpty(self):
        return self.top = -1

    

S = Stack(10)

for i in range(5):
    S.push(i)

print(S.arr)
print(S.pop())  
print(S.arr)