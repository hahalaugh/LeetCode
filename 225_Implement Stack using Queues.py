class MyStack(object):

    '''
    三种方法
    Push O(1), Pop O(N), 2 queues
    Push O(N), Pop O(1), 2 queues
    Push O(n), Pop O(1), 1 queue
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []
        
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1.append(x)
        
        while self.q2:
            self.q1.append(self.q2.pop(0))    

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q1.pop(0) if self.q1 else -1

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q1[0] if self.q1 else -1

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return False if self.q1 else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()