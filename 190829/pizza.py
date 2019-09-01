import sys
sys.stdin = open('sample_pizza.txt', 'r')
from queue import Queue

N = int(input())

for i in range(1, N+1):
    forge, pizza = map(int, input().split())
    pizza_list = list(map(int, input().split()))
    Q_size = 3
    Q = [] * Q_size
    for j in range(pizza):
        Q.append([j, pizza_list[j]])
        if len(Q) == forge:
            while len(Q) == forge:
                a = Q.pop(0)
                if a[1]//2 == 0:
                    pass
                else:
                    a[1] = a[1]//2
                    Q.append(a)
    while len(Q) != 1:
        a = Q.pop(0)
        if a[1]//2 == 0:
            pass
        else:
            a[1] = a[1]//2
            Q.append(a)
    a = Q.pop()
    print('#{} {}'.format(i, a[0]+1))





    

    