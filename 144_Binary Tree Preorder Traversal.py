def preorder(root):
    stack = []
    r = []
    while stack or root:
        while root:
            r.append(root.val)
            stack.append(root)
            root = root.next
        
        if stack:
            root = stack.pop()
            root = root.right
    
    return r


def preorder(root):
    if not root: return []
    
    return [root.val] + preorder(root.left) + preorder(root.right)
