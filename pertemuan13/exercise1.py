class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def isEmpty(self):
        if len(self.stack) == 0:
            return 'Stack Kosong'
        else:
            return 'Stack Tidak Kosong'