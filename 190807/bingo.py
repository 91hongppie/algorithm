import sys
sys.stdin  = open("input.txt", "r")
board=[]
count = 0
for i in range(5):
    board.append(list(map(int, input().split())))
print(board)

for i in range(5):
    call = list(map(int, input().split()))
    print(call)
    for n in range(5):
        for j in board:
            x = 0
            y = 0
            z = 0
            if call[n] in j:
                    j.index(call[n])=0
                    count+=1
                    # x += board[i][n]
                    # y += board[n][i]
                    # z += board[n][n]
                    print(board)
                # if x == 0 or y == 0 or z == 0:
                #     print(count)
                #     break

            

