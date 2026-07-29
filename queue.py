# queue.py
# Basic queue operations in Python

from collections import deque

# 1. Create a queue
queue = deque([10, 20, 30])
print("Initial queue:", queue)

# 2. Enqueue (insert at end)
queue.append(40)
print("After enqueue:", queue)

# 3. Dequeue (remove from front)
queue.popleft()
print("After dequeue:", queue)

# 4. Peek (front element)
print("Front element:", queue[0])

# 5. Traversal
print("Traversal:")
for item in queue:
    print(item, end=" ")


#output
"""Initial queue: deque([10, 20, 30])
After enqueue: deque([10, 20, 30, 40])
After dequeue: deque([20, 30, 40])
Front element: 20
Traversal:
20 30 40"""
