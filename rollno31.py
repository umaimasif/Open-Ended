class Node:
    #create a node that store data and the add of next term
    def __init__(self, data):
        self.data = data
        self.next = None
#in this the list is point to head and the head is none
class List:
    def __init__(self):
        self.head = None
#in this store the data in new node and then in head the while loop runs till the last node
    def add(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newnode
#print the value
    def show(self):
        current = self.head
        while current:
            print(current.data, end=" , " if current.next else "\n")
            current = current.next
#it del n after m
    def deletenafterm(self, m, n):
        current = self.head
        while current:
            # Skip m nodes
            for _ in range(m - 1):
                if current is None:
                    return
                current = current.next
            if current is None:
                return

            # Delete the next n nodes, if they exist
            a = current.next
            for _ in range(n):
                if a is None:
                    break
                a = a.next

            # Connect the current node to the next valid node
            current.next = a
            current = a


llist = List()
nodes = [4,5,7,9,3,2,4,1]
for node in nodes:
    llist.add(node)

print("Original Linked List:")
llist.show()

m, n = 2, 1  
llist.deletenafterm(m, n)

print("list after deleting", n, "after skipping", m, "nodes:")
llist.show()
