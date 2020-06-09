from cgitb import small


class LessNumKey(str):

    def __lt__(x, y):
        return x + y < y + x

    
class LargerNumKey(str):

    def __lt__(x, y):
        return x + y > y + x

    
class Solution(object):

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        largest = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest[0] == '0' else largest
    
    def smallestNumber(self, nums):
        smallest = ''.join(sorted(map(str, nums), key=LessNumKey))
        
        i = 0
        while i < len(smallest) and smallest[i] == '0':
            i += 1
        
        if i == len(smallest):
            return '0'
        else:
            return smallest[i:]


s = Solution()
print(s.largestNumber([9, 8, 0, 4, 5, 7]))
print(s.smallestNumber([9, 8, 0, 4, 5, 7]))
print(s.smallestNumber([3, 32, 321, 0, 0]))
