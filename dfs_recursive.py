class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def preorder(node):
    if node is None:
        return

    print(node.data, end=', ')
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.data, end=', ')
    inorder(node.right)


def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.data, end=', ')


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

root1.left.left = Node(4)
root1.left.right = Node(5)

root1.left.left.left = Node(6)

root1.left.right.left = Node(7)
root1.left.right.right = Node(8)


root2 = Node(50)
root2.left = Node(17)
root2.right = Node(76)

root2.left.left = Node(9)
root2.left.right = Node(23)

root2.left.left.right = Node(14)

root2.left.right.left = Node(19)

root2.left.left.right.left = Node(12)

root2.right.left = Node(54)

root2.right.left.right = Node(72)

root2.right.left.right.left = Node(67)

print('\nPre-order')
print('Tree 1:')
preorder(root1)
print('\nTree 2: ')
preorder(root2)

print('\n\nIn-order')
print('Tree 1:')
inorder(root1)
print('\nTree 2: ')
inorder(root2)

print('\n\nPost-order')
print('Tree 1:')
postorder(root1)
print('\nTree 2: ')
postorder(root2)
