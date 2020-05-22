# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):

        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')

        vals = []
        doit(root)
        s = ' '.join(vals)
        print s
        return s

    def deserialize(self, data):

        def doit():
            val = next(vals)
            print(val)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node

        vals = iter(data.split())
        return doit()


# Your Codec object will be instantiated and called as such:
codec = Codec()
root = codec.deserialize('1 2 3 # # 4 5 # # # #')
print(root.val, root.left.val, root.left.left.val, root.left.right.val, root.left.right.left.val)
# codec.serialize(root)
