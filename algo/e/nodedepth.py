#calculate the sum of the depth of each node in the tree
#root is 0, 2nd level will each have a deppth of 1, sum up all these

def sumOfEachNodeDepth(node):
    #level order, count, left, and right
    #dfs rec, count +1 on every rec call, each node will get called with
    #the last count it had, update the sum count
    if node is None:
        return 0
    currDepth = sumOfEachNodeDepth(node.left) + 1
    currDepth = currDepth + sumOfEachNodeDepth(node.right) + 1
    return currDepth

class Node:
    # Constructor to create a new Node
    def __init__( self, data ):
        self.val = data
        self.left = None
        self.right = None

if __name__ == '__main__':
    #NOT ORDERED
    root = Node(1)#0
    root.left = Node(2)#1
    root.right = Node(3)#1
    root.left.left = Node(4)#2
    root.left.right = Node(5) # 2

    root.left.left.left = Node(8)#3
    root.left.left.right = Node(9)#3

    root.right.left = Node(6)#2
    root.right.right = Node(7)#2

    root.right.right.left = Node(9)#3
    root.right.right.right = Node(19)#3

    print(sumOfEachNodeDepth(root))

