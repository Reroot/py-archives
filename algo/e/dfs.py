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
    stack.append(n)]
    while stack is not None:
        curr = stack.pop()
        if(curr is not None):
            curr = curr.left
            stack.append(curr)
        curr = curr.right
        stack.append(curr)

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
