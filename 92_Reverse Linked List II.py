# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from __builtin__ import False
class Solution(object):

    def reverseBetweenRecur(self, head, m, n):

        # �ݹ�д���ر�����˼��python2��֧��nonlocal
        def reverse(right, m, n):
            #nonlocal left, stop
            if n > 1: 
                right = right.next
            else:
                return 
            
            if m > 1:
                left = left.next
            
            reverse(right, m - 1, n - 1)
            if left == right or right.next == left:
                stop = True
            
            if not stop:
                left.val, right.val = right.val, left.val
                left = left.next
        
        left = head
        stop = False
        reverse(head, m, n)
        return head
    
    def reverseBetweenABCD(self, head, m, n):
        # ��ͳ���Ľڵ�ABCD������ע�����ڱ�����Ҫ��ʼ�Ͱ�Aָ��ͷ�ڵ㣬���
        # 1 [2 3 4] 5
        # a  b   c  d
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        def reverse(head):
            if not head or not head.next: return None
            prev = None
            cur = head
            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            
            return prev
        
        s = ListNode()
        s.next = head
        a = s
        
        # ��Ѱ��Ҫ����������ͷ�ڵ��ǰһ���ڵ�
        for _ in range(m - 1):
            a = a.next
            
        # ��Ҫ��Aָ��ͷ�ڵ㣬��һ�����ܳ���
        b = a.next
        
        # ̽Ѱc��Ҫ��ת�������β��
        c = b
        for _ in range(n - m):
            c = c.next
        
        # ��ת����Ҫ��������β�ڵ�ָ��Ľڵ�
        d = c.next
        
        # ��Ҫ��c���ض��������ڷ�ת����
        c.next = None

        reverse(b)
        a.next = c
        b.next = d
        
        return s.next
