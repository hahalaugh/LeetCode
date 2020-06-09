# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(self, root, sum):
        self.result = 0
        d = collections.defaultdict(int)
        d[0] = 1

        def dfs(root, total):
            if not root: return 
            
            curTotal = root.val + total
            # print(root.val, curTotal, curTotal-sum, d)
            if curTotal - sum in d and d[curTotal - sum] > 0:
                self.result += d[curTotal - sum]
            
            d[curTotal] += 1
            dfs(root.left, curTotal)
            dfs(root.right, curTotal)
            d[curTotal] -= 1
        
        dfs(root, 0)
        return self.result
            
    def pathSumDualRecursion(self, root, sum: int) -> int:

        def toLeaf(root, remain):
            # �ӵ�ǰ�ڵ㵽Ҷ�ڵ���ɵ������У���Ϊremain��·������
            if not root: return 0
            
            result = 1 if root.val == remain else 0
            
            return result + toLeaf(root.left, remain - root.val) + toLeaf(root.right, remain - root.val)
            
        if not root: return 0
        
        return toLeaf(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        
