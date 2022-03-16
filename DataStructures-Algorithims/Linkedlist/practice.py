class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class linkedlist:
    def __init__(self):
        self.head = None
        
    def out(self):
        temp = self.head
        arr = []
        while temp:
            arr.append(temp.data)
            temp = temp.next
        return arr
    
    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        
    def test(self): #delete duplicates
        hash = {}
        temp = self.head
        prev = None
        while temp:
            if temp.data not in hash:
                hash[temp.data] = None
                prev = temp
            else:
                prev.next = temp.next
            temp = temp.next
        
ll = linkedlist()
arr = [3,2,0,-4]
for i in arr:
    ll.push(i)
    
print(ll.test(1))

print(ll.out())