def bfs(s, c):
    global result
    k.append([s, c])
    visit[s] = True
    while k:
        h, a = k.pop(0)
        for i in G[h]:
            if not visit[i]:
                visit[i] = True
                k.append([i ,a+1])
        result.append([h, a])
            


import sys
sys.stdin = open('input_contact.txt', 'r')

for i in range(1, 11):
    length, s_point = map(int, input().split())
    a_list = list(map(int, input().split()))
    line_list = []
    for j in range(0, len(a_list)-1, 2):
        line_list.append([a_list[j], a_list[j+1]])
    G = [[] for _ in range(length)]
    visit = [False for _ in range(length)]
    for j in line_list:
        G[j[0]].append(j[1])
    k = []
    result = []
    a_result = []
    bfs(s_point, 0)
    for u in result:
        if u[1] == result[-1][1]:
            a_result.append(u[0])
    print('#{} {}'.format(i, max(a_result)))