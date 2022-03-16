import queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)
            
    def _insert(self, cur, val):
        if val < cur.data:
            if cur.left == None:
                cur.left = Node(val)
            else:
                self._insert(cur.left, val)
        elif val > cur.data:
            if cur.right == None:
                cur.right = Node(val)
            else:
                self._insert(cur.right, val)
                
    def inorder(self):
        arr = []
        self._inorder(self.root, arr)
        return arr
        
    def _inorder(self, root, key):
        if root:
            self._inorder(root.left, key)
            key.append(root.data)
            self._inorder(root.right, key)
            
    def preorder(self):
        arr = []
        self._preorder(self.root, arr)
        return arr
    
    def _preorder(self, root, key):
        if root:
            key.append(root.data)
            self._preorder(root.left, key)
            self._preorder(root.right, key)
    
    def postorder(self):
        arr = []
        self._postorder(self.root, arr)
        return arr
        
    def _postorder(self, root, key):
        if root:
            self._postorder(root.left, key)
            self._postorder(root.right, key)
            key.append(root.data)
    
    def search(self, root, key):
        if root is None:
            return None
        elif root.data == key:
            return True
        elif root.data > key:
            return self.search(root.left, key)
        elif root.data < key:
            return self.search(root.right, key)
        
    def height(self, root):
        if root == None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def sum(self, root):
        if root is None:
            return 0
        return root.data + self.sum(root.left) + self.sum(root.right)
    
    def levelorder(self, root):
        pass
        
bst = BinarySearchTree()

arr = [3,5,1,6,2,0,8,7,4]
for i in arr:
    bst.insert(i)

# print(bst.height(bst.root))
# print(bst.search(bst.root, 6))
# print(bst.height(bst.root))
# print("inorder:", bst.inorder())
# print("preorder:", bst.preorder())
# print("postorder:", bst.postorder())
print(bst.levelorder(bst.root))