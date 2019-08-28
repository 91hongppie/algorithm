from queue import Queue

# q = Queue()
# q.put('A')
# q.put('B')
# q.put('C')
#
# while not q.empty():
#     print(q.get())


def isEmpty():
    return front == rear

def isFull():
    return (rear+1) % len(cQ) == front

def enQueue(item):
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear = (rear+1) % len(cQ)
        cQ[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front = (front + 1) % len(cQ)
        return cQ[front]



cQ_SIZE = 3
cQ = [0] * cQ_SIZE
front = rear = 0    # front 와 rear 를 0 으로 초기화

enQueue('A')
enQueue('B')
enQueue('C')
print(deQueue())
print(deQueue())
print(deQueue())
