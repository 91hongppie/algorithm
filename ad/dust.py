import sys; sys.stdin = open('dust.txt', 'r')

row, col, T = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(row)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
while count != T:
    dust_list= []
    filter_list = []
    for r in range(row):
        for c in range(col):
            if room[r][c] == -1:
                filter_list.append([r, c])
            elif room[r][c] != 0:
                dust_list.append([r, c, room[r][c]])
                room[r][c] = 0
    for k in dust_list:
        a = k[2]
        for i in range(4):
            if 0 <= k[0]+dx[i] < row and 0 <= k[1]+dy[i] < col:
                if room[k[0]+dx[i]][k[1]+dy[i]] != -1:
                    room[k[0]+dx[i]][k[1]+dy[i]] += int(k[2]/5)
                    a -= int(k[2]/5)
        room[k[0]][k[1]] += a
    top = filter_list[0]
    bottom = filter_list[1]

    i = [top[0]-1, top[1]]
    room[top[0]-1][top[1]] = 0
    while i != top:
        if i[0] == top[0]:
            if top[1]+1 < i[1]: 
                room[i[0]][i[1]] = room[i[0]][i[1]-1]
            i[1] -= 1
        elif i[1] == col-1:
            room[i[0]][i[1]] = room[i[0]+1][i[1]]
            i[0] += 1
        elif 0 < i[0]:
            room[i[0]][i[1]] = room[i[0]-1][i[1]]
            i[0] -= 1
        elif i[1] < col-1:
            room[i[0]][i[1]] = room[i[0]][i[1]+1]
            i[1] += 1
    room[top[0]][top[1]+1] = 0
    

    j = [bottom[0]+1, bottom[1]]
    room[bottom[0]+1][bottom[1]] = 0
    while j != bottom:
        if j[0] == bottom[0]:
            if bottom[1]+1 < j[1]: 
                room[j[0]][j[1]] = room[j[0]][j[1]-1]
            j[1] -= 1
        elif j[1] == col-1:
            room[j[0]][j[1]] = room[j[0]-1][j[1]]
            j[0] -= 1
        elif j[0] < row - 1:
            room[j[0]][j[1]] = room[j[0]+1][j[1]]
            j[0] += 1
        elif j[1] < col-1:
            room[j[0]][j[1]] = room[j[0]][j[1]+1]
            j[1] += 1
    room[bottom[0]][bottom[1]+1] = 0
    count += 1
sum = 0
for k in range(row):
    print(room[k])
    for y in range(0, col):
        sum += room[k][y]
print(sum+2)





            