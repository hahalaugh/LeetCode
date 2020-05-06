class Solution(object):
    def combine(self, n, k):
        #µÝ¹é
        if k == 1:
            r = []
            for i in range(1, n+1):
                r.append([i])
            return r
        elif n == k:
            return [range(1, n+1)]
        else:
            a = self.combine(n-1, k)
            b = self.combine(n-1, k-1)
            for i in b:
                i.append(n)
            a.extend(b)
            return a
            
    def combineBC(self, n, k):
        #Backtracking Ä£°å
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        def bc(r, idx):
            if len(r) == k:
                result.append(r[:])
            else:
                for i in range(idx, n+1):
                    r.append(i)
                    bc(r, i+1)
                    r.pop()
        
        bc([], 1)
        return result
    
                    
                