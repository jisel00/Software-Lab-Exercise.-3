from collections import deque

q = deque()

q.append('x')
q.append('y')
q.append('z')

print("Initial queue:")
print(q)

print("\nElements dequeued from the queue:")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

