def dfs(n):
    if Node is None:
        return Node
    # #preorder
    # print(n.val)
    # dfs(n.left)
    # dfs(n.right)
    # #inorder
    # dfs(n.left)
    # print(n.val)
    # dfs(n.right)
    # #postorder
    dfs(n.left)
    dfs(n.right)
    print(n.val)

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
    print(dfs(root))
