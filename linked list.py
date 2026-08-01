# linkedlist.py
# Basic singly linked list operations in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # 2. Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 3. Delete a node
    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

# ▶️ Demo
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
print("Linked List after inserts:")
ll.display()

ll.delete(20)
print("Linked List after deleting 20:")
ll.display()
