import sys
sys.stdin = open('bishop.txt', 'r')
<<<<<<< HEAD


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
=======
sys.setrecursionlimit(10**8)

def bishop(yo, cnt):
    global po, result
    if yo == len(po):
        result = max(result, cnt)
    else:
        r, c = po[yo][0], po[yo][1]
        i = r + 1
        j = c + 1
        v = 0
        while 0 <= i and i < N and 0 <= j and j < N:
            if board[i][j] == 2:
                v += 1
                break
            i += 1
            j += 1
        if v == 0:
            i = r - 1
            j = c - 1
            while 0 <= i and i < N and 0 <= j and j < N:
                if board[i][j] == 2:
                    v += 1
                    break
                i -= 1
                j -= 1
        if v == 0:
            i = r + 1
            j = c - 1
            while 0 <= i and i < N and 0 <= j and j < N:
                if board[i][j] == 2:
                    v += 1
                    break
                i += 1
                j -= 1
        if v == 0: 
            i = r - 1 
            j = c + 1
            while 0 <= i and i < N and 0 <= j and j < N:
                if board[i][j] == 2:
                    v += 1
                    break
                i -= 1
                j += 1
        if v == 0:
            board[r][c] = 2
            bishop(yo+1, cnt+1)
            board[r][c] = 1
            bishop(yo+1, cnt)
        else:
            bishop(yo+1, cnt)




>>>>>>> 47100aadb6a277e6a5d07e499219b556e9f1bc35


N = int(input())
board = []
<<<<<<< HEAD
black = []
white = []
=======
po = []
>>>>>>> 47100aadb6a277e6a5d07e499219b556e9f1bc35
result = 0
for _ in range(N):
    board.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
<<<<<<< HEAD
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
=======
            po.append([i, j, 0])

bishop(0, 0)
print(result)
>>>>>>> 47100aadb6a277e6a5d07e499219b556e9f1bc35
