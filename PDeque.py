from dataclasses import dataclass

@dataclass
class Element:
    value:object
    priority:int

class BinaryHeap:
    def __init__(self) -> None:
        self.que = []
        self.indexque = []
    def push(self, Element):
        self.que.append(Element)
        self.sort(len(self.que)-1)
        
    def sort(self,i):        
        self.fatherindex = (i-1)//2
        if(self.que[i].priority < self.que[self.fatherindex].priority):
            self.que[i], self.que[self.fatherindex] = self.que[self.fatherindex], self.que[i]
            if (self.fatherindex!=0):
                self.sort(self.fatherindex)

    def pop(self, ):
        if not (self.indexque):
            self.indexque.append(0)
        self.min_index = 0
        for i in range(len(self.indexque)):
            if (self.que[self.indexque[i]].priority<self.que[self.indexque[self.min_index]].priority):
                self.min_index = i
        if (self.indexque[self.min_index]*2+2<len(self.que)):
            self.indexque.append(self.indexque[self.min_index]*2+2)
        if (self.indexque[self.min_index]*2+1<len(self.que)):
            self.indexque.append(self.indexque[self.min_index]*2+1)
        return self.que[self.indexque.pop(self.min_index)]
    
