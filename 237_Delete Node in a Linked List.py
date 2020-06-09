class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        
    def deleteNodeComplete(self, head, node):
        if not node: return
        if node.next:
            node.val = node.next.val
            node.next = node.next.next
        elif head == node:
            del head
        else:
            n = head
            while n and n.next != node:
                n = n.next
            if not n:
                return
            else:
                n.next = None
                return 


def printLinkedList(head):
    r = []
    t = head
    while t:
        r.append(t.val)
        t = t.next
    print(r)


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

# a.next = b
# b.next = c
# c.next = d

s = Solution()
s.deleteNodeComplete(a, a)
# s.deleteNodeComplete(pre.next, a)
# s.deleteNodeComplete(a, a)
printLinkedList(a)
