class Solution(object):
    """
    Solution 1. 使用combination模板，到长度了开始构建数组并返回，慢。
    Solution 2. 使用递归，C(n, k) = C(n-1, k-1) * n + C(n-1, k).出口有两个- 当k = 1的时候返回小于n的每个元素，当n=k的时候返回一个数组包含所有元素1-n
    C(3,2) = C(2,1)*3 + C(2,2) 
    - C(2,1) = [[1],[2]]
    - C(2,1) * 3 = [[1,3],[2,3]]
    - C(2,2) = [[1,2]]
    结果就是[[1,2],[1,3],[2,3]]
    """
    def combine(self, n, k):
        #递归
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
        #Backtracking 模板
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
    
                    
                