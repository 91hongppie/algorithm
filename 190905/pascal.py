import sys
sys.stdin = open('input_pascal.txt', 'r')

N = int(input())

for i in range(1, N+1):
    n = int(input())
    num_list = [[] for _ in range(n)]
    for k in range(1, n+1):
        for ho in range(k):
            if k == 1:
                num_list[k-1].append(1)
            elif k == 2:
                num_list[k-1].append(1)
            else:
                if ho == 0 or ho == k-1:
                    num_list[k-1].append(1)
                else:
                    num_list[k-1].append(num_list[k-2][ho-1]+num_list[k-2][ho])
    print('#{}'.format(i))
    for oi in range(len(num_list)-1):
        print(*num_list[oi])
    print(*num_list[-1])

