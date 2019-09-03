import sys
sys.stdin = open('sample_password.txt', 'r')

N = int(input())

for y in range(1, N+1):
    start_num, step, times = map(int, input().split())

    first_list = list(map(int, input().split()))
    j= 0
    i = 0
    while j != times:
        j += 1
        i += step
        if i < len(first_list):
            first_list.insert(i, first_list[i-1]+first_list[i])
        elif i == len(first_list):
            first_list.insert(i, first_list[-1]+first_list[0])
        else:
            i -= len(first_list)
            if i == 0:
                first_list.insert(i, first_list[0]+first_list[-1])
            else:
                first_list.insert(i, first_list[i-1]+first_list[i])
    result = list(first_list[-1:-11:-1])
    print('#{}'.format(y), end=' ')
    print(*result)



