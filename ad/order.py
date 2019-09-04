def DFS(s):
    global num, visit
    visit[s] = True
    stack.append(s)
    for w in G[s]:
        if visit[w] == False and num[w] == 1:
            DFS(w)
        elif num[w] > 1:
            num[w] -= 1


import sys
sys.stdin = open('input_order.txt', 'r')

for i in range(1, 11):
    point, line = map(int, input().split())
    visit = [False for _ in range(point+1)]
    G = [[] for _ in range(point+1)]
    num = [0 for _ in range(point+1)]
    stack = []
    result = list(map(int, input().split()))
    
    for j in range(0, len(result)-1, 2):
        G[result[j]].append(result[j+1])
        num[result[j+1]] += 1
    for r in range(1, len(num)):
        if num[r] == 0:
            DFS(r)
    print('#{}'.format(i), *stack)


