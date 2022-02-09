class Queue:
    def __init__(self):
        self.queue = []
        
    
    def addtoq(self, data):
        if data not in self.queue:
            
            self.queue.insert(0, data)
    def display(self):
        print(self.queue)
    def remove(self):
        self.queue.pop()

            
x = Queue()
x.addtoq("Apple")
x.addtoq("Ball")
x.addtoq("Cat")
x.addtoq("Dog")
x.display()
x.remove()
x.display()
x.remove()
x.display()
