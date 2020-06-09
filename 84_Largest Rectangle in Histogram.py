class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        #递增栈
        #13 11 9 11 12 4
        #append 0 和stack初始化为-1 相当于在原数组头和尾分别加入高度为0的房子 - 0 13 11 9 11 12 4 0
        #栈[13]遇到11,因为是递增，所以不允许11出现在13后，所以13出栈计算。以13为高的building，宽度是1
        #[9 11 12] 遇到4，不允许压入,分别计算12(12 * 1), 11, 12 (11 * 2), 9 11 12(9 * 3 (9本身，11和12的下部分)以及9之前的所有building(13, 11)( 出栈了不代表之前的building不存在了，因为是递增序列，出现在9之前的building，即使被出栈了，也都大于9)， 所以是9 * 5 (i - stack[-1](此时为-1)-1))
        
        if not heights: return 0

        heights.append(0)
        stack = [-1]
        mx = 0
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                w = i - stack[-1] - 1
                h = heights[idx]
                mx = max(mx, w * h)
            stack.append(i)
        
        return mx