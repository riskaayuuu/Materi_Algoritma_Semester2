class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        self.queue.pop(0)
    def head(self):
        return self.queue[0]