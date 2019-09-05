import sys
sys.stdin = open('sample_2048.txt', 'r')

N = int(input())

for oioi in range(1, N+1):
    rc, direction = map(str, input().split())
    board = []
    for _ in range(int(rc)):
        board.append(list(map(int, input().split())))
    if direction == 'up':
        for j in range(len(board)):
            result = []
            for k in range(len(board)):
                result.append(board[k][j])
            i = oi = 0
            while oi < len(result):
                if result[i] == 0:
                    result.pop(i)
                    result.append(0)
                else:
                    i+=1
                oi += 1
            for h in range(len(result)-1):
                if result[h] == result[h+1]:
                    result[h] += result[h+1]
                    result.pop(h+1)
                    result.append(0)
            i = oi = 0
            while oi < len(result):
                if result[i] == 0:
                    result.pop(i)
                    result.append(0)
                else:
                    i+=1
                oi += 1
            for u in range(len(board)):
                board[u][j] = result[u]
    elif direction == 'down':
        for j in range(len(board)):
            result = []
            for k in range(len(board)):
                result.append(board[-1-k][j])
            i = oi = 0
            while oi < len(result):
                if result[i] == 0:
                    result.pop(i)
                    result.append(0)
                else:
                    i+=1
                oi += 1
            for h in range(len(result)-1):
                if result[h] == result[h+1]:
                    result[h] += result[h+1]
                    result.pop(h+1)
                    result.append(0)
            i = oi = 0
            while oi < len(result):
                if result[i] == 0:
                    result.pop(i)
                    result.append(0)
                else:
                    i+=1
                oi += 1
            for u in range(len(board)):
                board[-1-u][j] = result[u]
    elif direction == 'left':
        for j in range(len(board)):
            result = []
            for k in range(len(board)):
                result.append(board[j][k])
            i = oi = 0
            while oi < len(result):
                if result[i] == 0:
                    result.pop(i)
                    result.append(0)
                else:
                    i+=1
                oi += 1
            for h in range(len(result)-1):
                if result[h] == result[h+1]:
                    result[h] += result[h+1]
                    result.pop(h+1)
                    result.append(0)
            i = oi = 0
            while oi < len(result):
                if result[i] == 0:
                    result.pop(i)
                    result.append(0)
                else:
                    i+=1
                oi += 1
            for u in range(len(board)):
                board[j][u] = result[u]
    elif direction == 'right':
        for j in range(len(board)):
            result = []
            for k in range(len(board)):
                result.append(board[j][k])
            i = oi = 0
            while oi < len(result):
                if result[i] == 0:
                    result.pop(i)
                    result.insert(0, 0)
                    i += 1
                else:
                    i+=1
                oi += 1
            for h in range(len(result)-1, 0, -1):
                if result[h] == result[h-1]:
                    result[h] += result[h-1]
                    result.pop(h-1)
                    result.insert(0, 0)
            i = oi = 0
            while oi < len(result):
                if result[i] == 0:
                    result.pop(i)
                    result.insert(0, 0)
                    i += 1
                else:
                    i+=1
                oi += 1
            for u in range(len(board)):
                board[j][u] = result[u]
    print('#{}'.format(oioi))
    for yo in board:
        for ho in yo:
            print(ho, end=' ')
        print()