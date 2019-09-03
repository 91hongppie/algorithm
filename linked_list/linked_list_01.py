class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def addtoLast(data):    # 마지막에 데이터 삽입
    global Head
    if Head == None:    # 빈 리스트이면
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None:   # 마지막 노드 찾을때까지
            p = p.link
        p.link = Node(data, None)

def delete(pre):
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link

def deleteFirst():
    global Head
    if pre == None:
        print('error')
    else:
        Head = Head.link

def addtoFirst(data):
    global Head
    Head = Node(data, Head)


def add(pre, data):
    if pre == None:
        print('error')
    else:
        pre.link=Node(data, pre.link)
    
data = [1, 2, 3, 4]
Head = None

for i in range(len(data)):
    addtoLast(data[i])

# for i in range(len(data)):
#     addtoFirst(data[i])
    
# delete(Head)
add(Head, 8)

while Head.link != None:
    print(Head.data, end='->')
    Head = Head.link
print(Head.data)