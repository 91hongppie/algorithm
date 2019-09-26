import sys
sys.stdin = open('bishop.txt', 'r')


def bishop(s, cnt, arr, word):
    global result, result1
    if s == len(arr):
        if word == 'b':
            result = max(result, len(cnt))
            return
        else:
            result1 = max(result1, len(cnt))
            return
    kt = 0
    for k in cnt:
        if abs(k[0]-arr[s][0]) == abs(k[1]-arr[s][1]):
            kt += 1
    if kt == 0:
        cnt.append(arr[s])
        bishop(s+1, cnt, arr, word)
        cnt.pop()
        bishop(s+1, cnt, arr, word)
    else:
        bishop(s+1, cnt, arr, word)


N = int(input())
board = []
black = []
white = []
result = 0
for _ in range(N):
    board.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            if i % 2 == 0 and j % 2 == 0:
                black.append([i, j])
            elif i % 2 != 0 and j % 2 != 0:
                black.append([i, j])
            elif i % 2 == 0 and j % 2 != 0:
                white.append([i, j])
            elif i % 2 != 0 and j % 2 == 0:
                white.append([i, j])

w = []
b = []
result1 = 0
bishop(0, w, black, 'b')
bishop(0, b, white, 'w')
print(result+result1)

# for y in range(len(white)):
