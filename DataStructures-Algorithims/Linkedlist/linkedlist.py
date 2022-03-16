class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None
        
    def out(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        
    def append(self, val):
        node = Node(val)
        last = self.head
        while last.next:
            last = last.next        
        last.next = node
        
    def insert(self, pos, val):
        node = Node(val)
        if pos == 0:
            node.next = self.head
            self.head = node
            return
        temp = self.head
        while pos!=1:
            temp = temp.next
            pos-=1
        node.next = temp.next
        temp.next = node
        
    def delv(self, val):
        temp = self.head
        if temp.data == val:
            self.head = temp.next
            return
        prev = None
        while temp.data != val:
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp.next = prev
    
    def delp(self, pos):
        temp = self.head
        if pos == 0:
            self.head = temp.next
            return
        while pos!=1:
            temp = temp.next
            pos-=1
        temp.next = temp.next.next
    
    def search(self, val):
        temp = self.head
        while temp.data != val:
            temp = temp.next
            if temp is None:
                print("Not found")
                return
        print("Found")
        return
    
    def swap(self, node1, node2):

        if node1 == node2:
            return

        prev1 = None
        curr1 = self.head
        while curr1.data != node1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        while curr2.data != node2:
            prev2 = curr2
            curr2 = curr2.next

        if curr1 == None or curr2 == None:
            return
        
        if prev1 != None:
            prev1.next = curr2
        else:
            self.head = curr2
 
        if prev2 != None:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next
        
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev
        
    def last(self, target):    
        head = self.head
        prev = None
        while head != None:
            if head.data == target:
                prev = head
            head = head.next
        if prev != None and prev.next == None:
            head = self.head
            while head.next != prev:
                head = head.next
            head.next = None
            
        if prev != None and prev.next != None:
            prev.data = prev.next.data
            head = prev.next
            prev.next = prev.next.next
            
    def delo(self, target):
        temp = self.head
        while temp.next:
            if temp.next.data is target:
                temp.next = temp.next.next
            else:
                temp = temp.next
        if self.head.data is target:
            self.head = self.head.next
        
    def delD(self):
        myDict = {}
        temp = self.head
        while temp:
            if temp.data in myDict:
                myDict[temp.data] = None
                prev = temp
            else:
                prev.next = temp.next
            temp = temp.next

    def rotate(self, n):
        temp = self.head
        count = 1
        while count<n and temp:
            temp = temp.next
            count+=1
        new_node = temp
        while temp.next:
            temp = temp.next
        temp.next = self.head
        self.head = new_node.next
        new_node.next = None
        
    def delNthN(self, n):
        cur = final = self.head
        while n!=0:
            cur = cur.next
            n-=1
        print(cur.data)
        if n is None:
            return
        while cur.next != None: # 6 5 4 3 2 1 null
            cur = cur.next
            final = final.next
        final.next = final.next.next
        
def merge(head1, head2):
    if not head1 or not head2:
        return head1 or head2
    if head1.data >= head2.data:
        head1.next = merge(head1.next, head2)
        return head1
    else:
        head2.next = merge(head1, head2.next)
        return head2
    
ll = linkedlist()

ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.push(6)
ll.push(7)
# ll.swap(2,1)
# ll.append(5)
# ll.insert(1, 10)
# ll.delv(2)
# ll.delp(2)
# ll.search(5)
# ll.reverse()
# ll.delD()
# ll.rotate(3)
# ll.delo(6)
# ll.out()

ll2 = linkedlist()
ll2.push(10)
ll2.push(11)
ll2.push(12)
ll2.push(13)

ll3 = linkedlist()
ll3.head = merge(ll.head, ll2.head)
ll3.out()
