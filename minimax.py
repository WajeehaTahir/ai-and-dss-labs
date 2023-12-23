import math
import time

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


def minimax(node, depth, maxDepth, maximizingPlayer):
    if depth == maxDepth or (node.left is None and node.right is None):
        return node.data

    if maximizingPlayer:
        bestValue = -math.inf
        children = [node.left, node.right]

        for child in children:
            if child is not None:
                v = minimax(child, depth+1, maxDepth, False)
                bestValue = max(bestValue, v)

        return bestValue

    else:
        bestValue = math.inf
        children = [node.left, node.right]

        for child in children:
            if child is not None:
                v = minimax(child, depth+1, maxDepth, True)
                bestValue = min(bestValue, v)

        return bestValue

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
print(minimax(root, 0, 4, True))
print("Time taken: ", time.clock() - start)
