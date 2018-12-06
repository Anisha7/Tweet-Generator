from linkedlist import LinkedList

class Queue(object):
    def init(self, items = None):
        self.data = LinkedList(items)

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        value = self.data.head.data
        self.data.delete(value)
        
        # return the item
        return value

    def peek(self):
        value = self.data.head.data
        
        # use linkedlist find function
        return value
        
    def size(self):
        self.data.length()

    def isEmpty(self):
        return self.data.length() <= 0

