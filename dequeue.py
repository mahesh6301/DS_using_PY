#dequeue
import collections

class Dequeue:
    def __init__(self):
        self.source = collections.deque([])
        
    def add(self,data):
        self.source.append(data)
    def addleft(self,data):
        self.source.appendleft(data)
    def remove(self):
        self.source.pop()
    def removeleft(self):
        self.source.popleft()
    def display(self):
        print(self.source)
        
        
        
        
        
        
x = Dequeue()
x.add("Apple")
x.add("Ball")
x.add("Cat")
x.add("Dog")
x.display()
x.addleft("Elephant")
x.display()
x.remove()
x.display()
x.removeleft()
x.display()

