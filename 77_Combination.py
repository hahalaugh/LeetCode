class Solution(object):
    """
    Solution 1. ʹ��combinationģ�壬�������˿�ʼ�������鲢���أ�����
    Solution 2. ʹ�õݹ飬C(n, k) = C(n-1, k-1) * n + C(n-1, k).����������- ��k = 1��ʱ�򷵻�С��n��ÿ��Ԫ�أ���n=k��ʱ�򷵻�һ�������������Ԫ��1-n
    C(3,2) = C(2,1)*3 + C(2,2) 
    - C(2,1) = [[1],[2]]
    - C(2,1) * 3 = [[1,3],[2,3]]
    - C(2,2) = [[1,2]]
    �������[[1,2],[1,3],[2,3]]
    """
    def combine(self, n, k):
        #�ݹ�
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
        #Backtracking ģ��
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
    
                    
                