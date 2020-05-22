# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from __builtin__ import False
class Solution(object):

    def reverseBetweenRecur(self, head, m, n):

        # 递归写法特别有意思，python2不支持nonlocal
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
        # 传统的四节点ABCD做法，注意用哨兵，不要开始就把A指向头节点，会错
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
        
        # 先寻找要逆序的链表的头节点的前一个节点
        for _ in range(m - 1):
            a = a.next
            
        # 不要把A指向头节点，这一步才能成立
        b = a.next
        
        # 探寻c到要逆转的链表的尾，
        c = b
        for _ in range(n - m):
            c = c.next
        
        # 翻转后需要被新链表尾节点指向的节点
        d = c.next
        
        # 需要用c来截断链表用于翻转链表。
        c.next = None

        reverse(b)
        a.next = c
        b.next = d
        
        return s.next
