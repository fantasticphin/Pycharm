import queue

#선형큐의 예씨
# def isFull(quque):
#     return rear == len(quque) - 1
# def isEmpty(quque):
#     global front, rear
#     return front == rear
# def enQueue(item):
#     global rear
#     if isFull(): print('Queue is full')
#     else:
#         rear += 1
#         Q[rear] = item
#
# def deQueue():
#     global front
#     if isEmpty(): print('Queue is empty')
#     else:
#         front += 1
#         return Q[front]
#
# def Qpeek():
#     if isEmpty(quque): print('Q is empty')
#     else: return Q[front+1]
#
#
# front = rear = -1
# SIZE = 100
# size = [0] * SIZE
# enQueue(1)
# enQueue(2)
# enQueue(3)
# print(Qpeek())
# print(deQueue())
# print(deQueue())
# print(deQueue())

#원형 큐의 예씨
def enQueueRound(item):
    global rear
    if isFull(): print('Queue is full')
    else:
        rear += (rear + 1) mod n

def deQueueRound():
    global front
    if isEmpty(): print('Queue is empty')
    else:
        front = (front + 1) mod n

front = rear = 0
SIZE = 100
size = [0] * SIZE
enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
# Q = []
# Q.append(1)
# Q.append(2)
# Q.append(3)
# print(Q.pop(0))
# print(Q.pop(0))
# print(Q.pop(0))

q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())