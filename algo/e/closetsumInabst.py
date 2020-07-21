#find the closeest number in the bst to target
#Given a binary search tree and a target node K. The task is to find the node with
#minimum absolute difference with given target value K.
#define class,
# Utility that allocates a new node with the
# given key and NULL left and right pointers.
class node:
    # Constructor to create a new node
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def findclosest(node, target):
    return recursefind(node, target, 100000000)

def recursefind(node, target, close = 0):
    if(node is None):
        return None
    close = target - node.val
    if (target > abs(close)):  # contuine looking
        return recursefind(node.right, target, close)
    if(target < abs(close)):#contuine looking
        return recursefind(node.left, target, close)
    if (close == 0): return node.val
    return close #return out closest possible updated diff


# Recursive Python program to find key
# closest to k in given Binary Search Tree.




# Driver Code
if __name__ == '__main__':
    root = node(9)
    root.left = node(4)
    root.right = node(17)
    root.left.left = node(3)
    root.left.right = node(6)
    root.left.right.left = node(5)
    root.left.right.right = node(7)
    root.right.right = node(22)
    root.right.right.left = node(20)
    k = 18
    print(findclosest(root, k))
