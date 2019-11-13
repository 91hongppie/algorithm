import sys
sys.stdin = open('princess.txt', 'r')

def DFS(dis, num, ans):
    



board = [[] for _ in range(5)]
for i in range(5):
    board[i].extend(input())

visit = [[False]*5 for _ in range(5)]
result = []
answer = []
for j in range(5):
    for k in range(5):
        if board[j][k] == 'S':
            result.append([j, k])
for k in range(len(result)):
    answer.append(result[k])
    DFS(0, k, answer)
    answer.pop()