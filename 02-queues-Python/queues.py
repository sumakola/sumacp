"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

#reference from https://jmlb.github.io/coding/2016/12/16/queues/
class Queue:
    def __init__(self, head=None):
        self.storage = [head]
    #queues follow the FIFO principle
    #adding the element at the top 
    def enqueue(self, new_element):
        self.storage.append(new_element)
    #peek is used to return top element without deleting from the queue
    def peek(self):
        return self.storage[0]  
    #removes the element from the head of the queue
    def dequeue(self):
        return self.storage.pop(0)  
