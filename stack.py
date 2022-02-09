class Stack:
    def __init__(self):
        self.stack = []
    def add(self, data):
        if data not in self.stack:
            
            self.stack.append(data)
    def display(self):
        print(self.stack)
    def remove(self):
        if(len(self.stack)<=0):
            print("stack is empty")
        else:
            self.stack.pop()

x = Stack()
x.add("Apple")
x.add("Ball")
x.display()
x.remove()
x.display()
