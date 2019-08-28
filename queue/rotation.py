import sys
from queue import Queue
sys.stdin = open('sample_rotation.txt', 'r')

N = int(input())

for i in range(1, N+1):
    length, num = map(int, input().split())
    a_list = list(map(int, input().split()))
    Q = Queue()
    for j in a_list:
        Q.put(j)
    for k in range(num):
        a = Q.get()
        Q.put(a)

    print('#{} {}'.format(i, Q.get()))
        