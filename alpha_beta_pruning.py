import math
import time

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

def alphabeta(node, depth, maxDepth, alpha, beta, maximizingPlayer):
    if depth == maxDepth:
        return node.data

    if maximizingPlayer:
        v = -math.inf
        children = [node.left, node.right]

        for child in children:
            if child:
                v = max(v, alphabeta(child, depth+1, maxDepth, alpha, beta, False))
                alpha = max(alpha, v)

                if beta <= alpha:
                    break
        return v

    else:
        v = math.inf
        children = [node.left, node.right]

        for child in children:
            if child:
                v = min(v, alphabeta(child, depth+1, maxDepth, alpha, beta, True))
                beta = min(beta, v)

                if beta <= alpha:
                    break
        return v

root = Node(0)
root.left = Node(0)
root.right = Node(0)

root.left.left = Node(0)
root.left.right = Node(0)

root.left.left.left = Node(0)
root.left.left.right = Node(0)

root.left.right.left = Node(0)

root.left.left.left.left = Node(10)
root.left.left.left.left = Node(math.inf)

root.left.right.left.left = Node(5)

root.left.right.left.left = Node(-10)

root.right.left = Node(0)
root.right.right = Node(0)

root.right.left.left = Node(0)
root.right.left.right = Node(0)

root.right.left.left.left = Node(7)
root.right.left.left.right = Node(5)

root.right.left.right.left = Node(-math.inf)

root.right.right.left = Node(0)

root.right.right.left.left = Node(-7)
root.right.right.left.right = Node(-5)

start = time.clock()
print(alphabeta(root, 0, 4, -math.inf, math.inf, True))
print("Time taken: ", time.clock() - start)
