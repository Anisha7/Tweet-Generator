from linkedlist import LinkedList

class Queue(object):
    def __init__(self, items = None):
        self.items = LinkedList(items)

    def enqueue(self, item):
        # print(self.size())
        (self.items).append(item)

    def dequeue(self):
        value = self.items.head.data
        self.items.delete(value)
        
        # return the item
        return value

    def peek(self):
        value = self.items.head.data
        
        # use linkedlist find function
        return value
        
    def size(self):
        (self.items).length()

    def isEmpty(self):
        return (self.items).length() <= 0

