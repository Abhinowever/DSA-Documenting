class MyQueue(object):

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        self.peek() # validating output stack is filled ?
        return self.output.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.output : # if output is empty will fill it back using input
            while self.input :
                self.output.append(self.input.pop())
        
        return self.output[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.output and not self.input


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()