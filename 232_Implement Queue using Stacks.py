class MyQueue(object):
    '''
        有两种方法，这种就是PUSH O(1), POP O(N)
        还有一种办法是PUSH O(N), POP O(1)
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.s1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        return self.s2.pop() if self.s2 else -1
        
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.s2: 
            while self.s1: 
                self.s2.append(self.s1.pop())
        
        return self.s2[-1] if self.s2 else -1
    
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.s1 and not self.s2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
