class bst_node:
    def __init__(self, key, pos):
        self.left = None
        self.right = None
        self.val = key
        self.pos = pos

def insert(root,key, p):
    if root is None:
        print(p)
        root = bst_node(key,p)
    else:
        if root.val < key:
            root.right = insert(root.right,key, 2*p+1)
        else:
            root.left = insert(root.left,key, 2*p)
    return root

def delete(root, key):
    if root is None:
        return root
    elif root.val > key:
        root.left = delete(root.left, key)
    elif root.val < key:
        root.right = delete(root.right, key)
    else:
        print(root.pos)
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = root.right
        while(temp.left is not None):
            temp = temp.left
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root
    

t = int(input())
r = None
for _ in range(t):
    op, val = map(str, input().split())
    val = int(val)
    if op == 'i':
        r = insert(r, val, 1)
    else:
        r = delete(r, val)


