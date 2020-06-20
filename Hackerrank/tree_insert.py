class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root=Node(val)
        else:
            root=self.root
            if root.info>=val:
                root=root.left
                self.insert(val)
            else:
                root=root.right
                self.insert(val)

tree = BinarySearchTree()
print(tree.root)
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])
    print(tree.root)
print(tree.root)
preOrder(tree.root)
