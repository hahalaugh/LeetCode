class Solution(object):
    """
    Solution 1. Two Pointer Greedy. ��������ұ�==limit�������һ��������ҵ������ͻ��Ǵ���LIMIT��ֻȡ�ұߣ������һ��������Һ�С��limit�������һͬʱ�ƽ���ע�����ָ��ָ��ͬһ�������
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