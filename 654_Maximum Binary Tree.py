class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution(object):

    def constructMaximumBinaryTree(self, nums):
        if not nums: return None
        
        stack = [(0, len(nums))]
        root = None
        while stack:
            (i, j) = stack.pop()
            mx = -float('inf')
            idx = -1
            
            for k in range(i, j):
                if nums[k] > mx:
                    mx = nums[k]
                    idx = k
            
            root = TreeNode(nums[idx])
            if idx + 1 < j:
                stack.append((idx + 1, j))
            stack.append((preRoot, idx + 1, j))
            stack.append((preRoot, i, idx))
        
        return preRoot
        
    def constructMaximumBinaryTreeRecursive(self, nums):
        # Recursive
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        
        mx = -float('inf')
        idx = -1
        
        for i in range(len(nums)):
            if nums[i] > mx:
                mx = nums[i]
                idx = i
        
        root = TreeNode(nums[idx])
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx + 1:])
        return root

    
s = Solution()
s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
