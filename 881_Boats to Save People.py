class Solution(object):
    """
    Solution 1. Two Pointer Greedy. 排序，如果右边==limit，结果加一，如果左右的重量和还是大于LIMIT，只取右边，结果加一。如果左右和小于limit，结果加一同时逼近。注意最后指针指向同一个的情况
    """
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i, j = 0, len(people)-1
        
        count = 0
        while i < j:
            if people[j] == limit or people[i] + people[j] > limit:
                count += 1
                j -= 1
            else:
                count += 1
                i += 1
                j -= 1
        
        if i == j: count += 1
        
        return count