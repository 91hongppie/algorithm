def DFS(table, x, y, i, stack):
    global result
    if x < len(table) and y < len(table) and table[x][y] not in stack:
        stack.append(table[x][y])
        DFS(table, x+1, y, i+1, stack)
        DFS(table, x, y+1, i+1, stack)
    else:
        result.append(i)
        return

import sys
sys.stdin = open('alphabet.txt', 'r')

row, col = map(int, input().split())
table = []
result = []
stack = []
for _ in range(row):
    mo_list= []
    mo_list.extend(list(input()))
    table.append(mo_list)
DFS(table, 0, 0, 0, stack)
print(max(result))