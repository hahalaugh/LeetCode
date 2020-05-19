def inorder(root):
    r = []
    stack = []
    
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        
        if stack:
            root = stack.pop()
            r.append(root.val)
            root = root.right
    
    return r


def inorderRecursive(root):
    if not root: return []
    
    return inorder(root.left) + [root.val] + inorder(root.right)
            
