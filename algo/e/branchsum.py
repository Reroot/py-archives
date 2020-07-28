

def branchSums(n):
    sums = []
    return branchSumDfs(n, 0, sums)

def branchSumDfs(n, runningSum, sums):
    runningSum += n.val + runningSum
    if n.left and n.right:
        sums.append(runningSum)
        return
    branchSumDfs(n.left, runningSum, sums)
    branchSumDfs(n.right, runningSum, sums)

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
    print(branchSums(root))
