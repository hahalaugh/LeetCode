class Solution(object):

    def twoSum(self, numbers, target):
        # Tow Pointer
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers: return [-1, -1]
        
        i, j = 0, len(numbers) - 1
        
        while i < j: 
            t = numbers[i] + numbers[j]
            if t == target:
                return [i + 1, j + 1]
            elif t < target:
                i += 1
            else:
                j -= 1
        
