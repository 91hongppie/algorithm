import sys
sys.stdin = open('input_paper.txt', 'r')

row, col = map(int, input().split())
num = int(input())
cut_list = []
row_list = [0, row]
col_list = [0, col]
for i in range(num):
    cut_list.append(list(map(int, input().split())))
for i in cut_list:
    if i[0] == 1:
        row_list.append(i[1])
    else:
        col_list.append(i[1])
row_list = sorted(row_list)
col_list = sorted(col_list)
row = 0
col = 0
for k in range(len(row_list)-1):
    if row < row_list[k+1] - row_list[k]:
        row = row_list[k+1] - row_list[k]
for j in range(len(col_list)-1):
    if col < col_list[j+1] - col_list[j]:
        col = col_list[j+1] - col_list[j]
print(col*row)