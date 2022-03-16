from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)
    
    def _insert(self, root, val):
        if val < root.data:
            if root.left == None:
                root.left = Node(val)
            else:
                self._insert(root.left, val)
        elif val > root.data:
            if root.right == None:
                root.right = Node(val)
            else:
                self._insert(root.right, val)
    
    def out(self, root):
        arr = []
        self.dfs(root, arr)
        return arr
        
    def dfs(self, root, key):
        if root:
            key.append(root.data)
            self.dfs(root.right, key)
            
        
bst = BinarySearchTree()
arr = [1,2]
for i in arr:
    bst.insert(i)
print(bst.out(bst.root))