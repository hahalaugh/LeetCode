# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def getIntersection(self, headA, headB):
        # ����˫ѭ����A������ͷ�˾ͱ���B��B������ͷ�˱���A��A + C + B = B + C + A, ����н����һ����A+B+C��λ���Ͻ��档
        
        a = headA
        b = headB
        
        while a and b:
            if a == b: 
                return a
            else:
                a = a.next
                b = b.next
                if not a: a = headB
                if not b: b = headA
        return None
    
    def getIntersectionHash(self, headA, headB):
        # ��ϣ��
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next
        
        while headB:
            if headB in s: 
                return headB
            headB = headB.next
        
        return None
        
    def getIntersectionNode(self, headA, headB):
        # ��������ջ��ȫ����ջ��Ƚ�ջ���������ͬ�򷵻����һ����ͬ�Ľڵ�
        sa = []
        sb = []
        while headA:
            sa.append(headA)
            headA = headA.next
        
        while headB:
            sb.append(headB)
            headB = headB.next
        
        prev = None
        while sa and sb:
            if sa[-1] == sb[-1]:
                prev = sa.pop()
                sb.pop()
            else:
                return prev
        
        return prev
    
    def getIntersectionNodeIterate(self, headA, headB):
        # M + N, �ֱ�����õ����ȡ���Ľڵ����߳��ȲȻ��һ���ߣ�ֱ������λ��
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: 
            return None
        
        a = headA
        ca = 0
        b = headB
        cb = 0
        while a.next: 
            a = a.next
            ca += 1
        
        while b.next:
            b = b.next
            cb += 1
        
        for _ in range(abs(ca - cb)):
            if ca > cb:
                headA = headA.next
            else:
                headB = headB.next
        
        while headA and headB:
            if headA == headB: 
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None        
        
            
