import sys
sys.stdin  = open("input.txt", "r")

board=[]
count = 0
ans = ['0', '0', '0', '0', '0']
for i in range(5):
    board.append(list(map(int, input().split())))
for i in range(5):
    call = list(map(int, input().split()))       
    for n in range(5):
        for j in board:
            if call[n] in j:
                j[j.index(call[n])] = '0'
                count+=1
        y_board = []
        for w in range(5):
            mo=[]
            for e in range(5):
                mo.append(board[e][w])
            y_board.append(mo)
        z = []
        back_z =[]
        bingo=0   
        for t in range(5):
            if board[t] == ans:
                bingo += 1
            if y_board[t] == ans:
                bingo += 1
            for k in range(5):
                z.append(board[k][k])
                back_z.append(board[k][4-k])
            if z == ans:
                bingo += 1
            if back_z == ans:
                bingo += 1
        if bingo >= 3:
            print(count)
            exit()

            

                    
        

            

