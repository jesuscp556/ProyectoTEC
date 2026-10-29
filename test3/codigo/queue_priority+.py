from queue import PriorityQueue
q = PriorityQueue()

q.put((2, "Smith"))
q.put((1, "Jones"))
q.put((4, "Wilson"))
q.put((1, "Aamirez"))

next = q.get()
print(next)

# print(q.empty())
# print(q.full())

q.put((3, "Collins"))
print(q.get())

while not q.empty():
     print(q.get())

print(q.empty())