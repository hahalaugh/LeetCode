from __builtin__ import None


def postorderRecursive(root):
    if not root: return []
    return postorder(root.left) + postorder(root.right) + [root.val]


def postorder(root):
    stack = []
    r = []
    visited = None
    
    while root:
        stack.append(root)
        root = root.left
        
    while stack:
        root = stack.pop()
        if not root.right or root.right != visited:
            r.append(root.val)
            visited = root
        else:
            stack.append(root)
            root = stack[-1].right
            while root:
                stack.append(root)
                root = root.left
    
    return r
