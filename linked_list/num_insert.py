import sys
sys.stdin = open('sample_num_insert.txt', 'r')

N = int(input())

for i in range(1, N+1):
    length, insert_num, result_num = map(int, input().split())
    num_list = list(map(int, input().split()))
    for j in range(insert_num):
        index, num = map(int, input().split())
        num_list.insert(index, num)
    print('#{} {}'.format(i, num_list[result_num]))