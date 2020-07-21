#find the closeest number in the bst to target
#Given a binary search tree and a target node K. The task is to find the node with
#minimum absolute difference with given target value K.
#define class,
# Utility that allocates a new node with the
# given key and NULL left and right pointers.
class node:
    # Constructor to create a new node
    def __init__( self, data ):
        self.val = data
        self.left = None
        self.right = None

def findclosest(node, target):
    return recursefind(node, target, float("inf"))

def recursefind(node, target, close):
    if(node is None):
        return close
    #if the diff between the last closest and the current is greater, update close to the currenrt
    if(abs(target - close) > abs(target - node.val)):
        close = node.val #need to find the diffrence either way
    if(target < node.val):  # contuine looking
        return recursefind(node.left, target, close)
    elif(target > node.val):#contuine looking
        return recursefind(node.right, target, close)
    else:
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
    print(findclosest(root, 18))
