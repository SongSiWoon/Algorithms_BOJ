n = int(input())
tree = {}
for i in range(n):
    node, left, right = list(input().split())
    tree[node] = [left, right]
root = list(tree)[0]


def preorder(node):
    if node == '.':
        return
    left, right = tree[node]
    print(node, end='')
    preorder(left)
    preorder(right)


def inorder(node):
    if node == '.':
        return
    left, right = tree[node]
    inorder(left)
    print(node, end='')
    inorder(right)


def postorder(node):
    if node == '.':
        return
    left, right = tree[node]
    postorder(left)
    postorder(right)
    print(node, end='')


preorder(root)
print()
inorder(root)
print()
postorder(root)
