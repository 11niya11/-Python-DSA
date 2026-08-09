"""Topic: Stack Implementation using Linked List in Python""""
"""Steps
Create a new file in your repo: stack_using_linkedlist.py.

Write a program that:

Defines a Node class (data, next).

Implements a Stack class with methods:

push() → add element to top.

pop() → remove element from top.

peek() → view top element.

is_empty() → check if stack is empty.

display() → print stack contents.

Demonstrates usage in main."""
# stack_using_linkedlist.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack Underflow!")
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.top.data

    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Demo
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack after pushes:")
    stack.display()

    print("Top element:", stack.peek())

    print("Popped element:", stack.pop())
    print("Stack after pop:")
    stack.display()


"""▶️ Expected Output
Code
Stack after pushes:
30 -> 20 -> 10 -> None
Top element: 30
Popped element: 30
Stack after pop:
20 -> 10 -> None""""
