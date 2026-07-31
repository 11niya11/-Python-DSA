# stack.py
# Basic stack operations in Python

stack = []

# 1. Push (insert at top)
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushes:", stack)

# 2. Pop (remove from top)
stack.pop()
print("Stack after pop:", stack)

# 3. Peek (top element)
print("Top element:", stack[-1])

# 4. Traversal
print("Traversal:")
for item in reversed(stack):   # top to bottom
    print(item, end=" ")

""""▶️ Expected Output
Stack after pushes: [10, 20, 30]
Stack after pop: [10, 20]
Top element: 20
Traversal:
20 10

Step‑by‑Step Execution
1.Create a queue
queue = deque([10, 20, 30])
print("Initial queue:", queue)
➡️ Output: deque([10, 20, 30])  
→ You start with a queue containing 10, 20, 30.



2.Enqueue (insert at end)
queue.append(40)
print("After enqueue:", queue)
➡️ Output: deque([10, 20, 30, 40])  
→ Adds 40 at the end of the queue.



3.Dequeue (remove from front)
queue.popleft()
print("After dequeue:", queue)
➡️ Output: deque([20, 30, 40])  
→ Removes 10 from the front (first element).



4.Peek (front element)
print("Front element:", queue[0])
➡️ Output: Front element: 20  
→ Shows the current front element (20).



5.Traversal (iterate through queue)
for item in queue:
    print(item, end=" ")
➡️ Output: 20 30 40  
→ Prints all elements from front to back.


BASIC  summary
Enqueue → adds at the end.

Dequeue → removes from the front.

Peek → shows the front element.

Traversal → prints the queue in order.""""
