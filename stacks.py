class stack_actions():
    def __init__(self):
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if len(self.stack)==0:
            print('Stack is empty')
        else:
            self.stack.pop()
    def top(self):
        if len(self.stack)==0:
            print('Stack is empty')
        else:
            return self.stack[-1]
    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    def size(self):
        return len(self.stack)
    def display(self):
        print(self.stack)

stack1=stack_actions()
stack1.top()
stack1.push(6)
stack1.top()
print(stack1.isEmpty())
print(stack1.size())
stack1.display()