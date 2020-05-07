class Solution(object):

    def intervalIntersection(self, A, B):
        # Two Pointer, 右边界较大的节点不变，右边界小的节点往前移动不断merge.
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        
        r = []
        
        while i < len(A) and j < len(B):
            pair = (max(A[i][0], B[j][0]), min(A[i][1], B[j][1]))
            
            if pair[1] >= pair[0]:
                r.append(pair)
            
            if A[i][1] > B[j][1]:
                j += 1
            else:
                i += 1
        return r
