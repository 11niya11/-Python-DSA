# doublylinkedlist.py

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            last = temp
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

    def delete(self, key):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if temp is None:
            return
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        if temp == self.head:
            self.head = temp.next

# Demo
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_end(10)
    dll.insert_end(20)
    dll.insert_end(30)

    print("Forward traversal:")
    dll.display_forward()

    print("Backward traversal:")
    dll.display_backward()

    dll.delete(20)
    print("After deleting 20:")
    dll.display_forward()


▶️ Expected OutputForward traversal:
10 <-> 20 <-> 30 <-> None
Backward traversal:
30 <-> 20 <-> 10 <-> None
After deleting 20:
10 <-> 30 <-> None
Forward traversal:
10 <-> 20 <-> 30 <-> None
Backward traversal:
30 <-> 20 <-> 10 <-> None
After deleting 20:
10 <-> 30 <-> None
