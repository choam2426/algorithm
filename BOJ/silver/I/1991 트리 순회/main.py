# https://www.acmicpc.net/problem/1991
n = int(input())
tree = {}
for _ in range(n):
    node, lc, rc = input().split()
    tree[node] = [lc, rc]


def preorder(node):
    print(node, end="")

    lc = tree[node][0]
    rc = tree[node][1]
    if lc != ".":
        preorder(lc)
    if rc != ".":
        preorder(rc)


def inorder(node):
    lc = tree[node][0]
    rc = tree[node][1]
    if lc != ".":
        inorder(lc)
    print(node, end="")
    if rc != ".":
        inorder(rc)


def postorder(node):
    lc = tree[node][0]
    rc = tree[node][1]
    if lc != ".":
        postorder(lc)
    if rc != ".":
        postorder(rc)
    print(node, end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")
