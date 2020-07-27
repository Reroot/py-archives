def dfsRecursive(n):
    if n is None:
        return Node
    # #preorder
    # print(n.val)
    # dfsRecursive(n.left)
    # dfsRecursive(n.right)
    # #inorder
    # dfsRecursive(n.left)
    # print(n.val)
    # dfsRecursive(n.right)
    # #postorder
    dfsRecursive(n.left)
    dfsRecursive(n.right)
    print(n.val)

def dfsIterative(n):
    if n is None:
        return None
    stack = []
    stack.append(n)
    while stack:
        curr = stack.pop()
        if curr.left:
            curr = curr.left
            stack.append(curr)
        print(curr.val)
        if curr.right:
            curr = curr.right
            stack.append(curr)

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
# def dfs(root, val):
#     stack = [root]
#     while stack:
#         node = stack.pop()
#         if node.val == val:
#             return node
#         if node.left:
#             stack.append(node.left)
#         if node.right:
#             stack.append(node.right)

class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

# Driver Code
if __name__ == '__main__':
    root = Node(9)
    root.left = Node(4)
    root.right = Node(17)
    root.left.left = Node(3)
    root.left.right = Node(6)
    root.left.right.left = Node(5)
    root.left.right.right = Node(7)
    root.right.right = Node(22)
    root.right.right.left = Node(20)
    k = 18
    print(dfsIterative(root))
