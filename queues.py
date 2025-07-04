class queue_actions():
    def __init__(self):
        self.queue=[]
    def enqueue(self,value):
        self.queue.append(value)
        print(self.queue)
    def dequeue(self):
        if len(self.queue)>0:
            self.queue.pop(0)
        else:
            print('No items in list')
        print(self.queue)
    def isEmpty(self):
        if len(self.queue)==0:
            print('Yes it is empty')
        else:
            print('Not empty')
    def peek_head(self):
        if len(self.queue)>0:
            print(self.queue[0])
        else:
            print('No items in list')
    def peek_tail(self):
        if len(self.queue)>0:
            print(self.queue[-1])
        else:
            print('No items in list')
    def size(self):
        print(len(self.queue))
    def display(self):
        print(self.queue) 

queue1=queue_actions()
queue1.peek_head()
queue1.peek_tail()
queue1.dequeue()
queue1.enqueue(6)
queue1.enqueue(7)
queue1.peek_head()
queue1.size()
queue1.dequeue()