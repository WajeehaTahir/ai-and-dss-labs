class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.mid = None
        self.data = data

def bfs(root):
    visited_nodes = []
    queue = [root]

    while len(queue):
        node = queue.pop(0)

        if node.data not in visited_nodes:
            visited_nodes.append(node.data)

            neighbors = [node.left, node.mid, node.right]

            for neighbor in neighbors:
                if neighbor:
                    queue.append(neighbor)

    print(visited_nodes)


root1 = Node(1)
root1.left = Node(2)
root1.mid = Node(3)
root1.right = Node(4)

root1.left.left = Node(5)
root1.left.mid = Node(6)

root1.right.mid = Node(7)
root1.right.right = Node(8)

root1.left.left.left = Node(9)
root1.left.left.mid = Node(10)

root1.right.mid.mid = Node(11)
root1.right.mid.right = Node(12)

bfs(root1)

root2 = Node('Frankfurt')
root2.left = Node('Mannheim')
root2.mid = Node('Würzburg')
root2.right = Node('Kassel')

root2.left.left = Node('Karlsruhe')

root2.mid.left = Node('Nürnberg')
root2.mid.right = Node('Erfurt')

root2.right.right = Node('München')

root2.left.left.mid = Node('Augsburg')

root2.mid.left.mid = Node('Stuttgart')

bfs(root2)
