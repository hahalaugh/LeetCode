class Solution(object):
    def generateParenthesisBC(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def bc(r, left, right):
            if len(r) == 2 * n:
                result.append(r)
            else:
                if left < n:
                    bc(r + '(', left + 1, right)
                
                if right < left:
                    bc(r + ')', left, right + 1)
        
        bc('', 0, 0)
        
        return result
    
    def generateParenthesisBF(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def isValid(r):
            bal = 0
            for c in r:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            
            return bal == 0
        
        def bc(r):
            if len(r) == 2 * n:
                if isValid(r):
                    result.append(r)
            else:
                bc(r + '(')
                bc(r + ')')
        
        bc('')
        
        return result
    