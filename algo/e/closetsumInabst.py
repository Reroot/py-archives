#find the closeest number in the bst to target
#define class,
def findclosest(node, target):
    return recursefind(node, target, 'inf')

def recursefind(node, target, close = 0):
    if(node is None):
        return None
    if(target - node.val == 0): return node.val
    if(target - node.val < close):#we know if we found a closer, we can ignore left side becuase it's all lower
        close = target - node.val
    if (target > close):  # contuine looking
        return recursefind(node.right, target, diff)
    if(target < close):#contuine looking
        return recursefind(node.left, target, close)
    return close #return out closest possible updated diff