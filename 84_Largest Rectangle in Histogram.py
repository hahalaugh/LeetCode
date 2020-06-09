class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        #����ջ
        #13 11 9 11 12 4
        #append 0 ��stack��ʼ��Ϊ-1 �൱����ԭ����ͷ��β�ֱ����߶�Ϊ0�ķ��� - 0 13 11 9 11 12 4 0
        #ջ[13]����11,��Ϊ�ǵ��������Բ�����11������13������13��ջ���㡣��13Ϊ�ߵ�building�������1
        #[9 11 12] ����4��������ѹ��,�ֱ����12(12 * 1), 11, 12 (11 * 2), 9 11 12(9 * 3 (9����11��12���²���)�Լ�9֮ǰ������building(13, 11)( ��ջ�˲�����֮ǰ��building�������ˣ���Ϊ�ǵ������У�������9֮ǰ��building����ʹ����ջ�ˣ�Ҳ������9)�� ������9 * 5 (i - stack[-1](��ʱΪ-1)-1))
        
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