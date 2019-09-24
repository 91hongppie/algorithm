import sys
sys.stdin = open('NnM1.txt', 'r')


def comb(e, n):
    global pr, result
    if n == nums-1:
        print(*result)
    else:
        if e == 1:
            q = -1
            for i in range(num):
                if e == i:
                    continue
                if q == num_list[i]:
                    continue
                else:
                    q = num_list[i]
                    result.append(num_list[i])
                    comb(i, n+1)
                    result.pop()
        else:
            q = -1
            for i in range(num):
                if e == i:
                    continue
                if q == num_list[i]:
                    continue
                else:
                    q = num_list[i]
                    result.append(num_list[i])
                    comb(i, n+1)
                    result.pop()


num, nums = map(int, input().split())
num_list = list(map(int, input().split()))
result = []
pr = []
num_list.sort()
q = -1
for j in range(num):
    if q == num_list[j]:
        continue
    else:
        q = num_list[j]
        result.append(num_list[j])
        comb(j, 0)
        result.pop()
for k in pr:
    print(*k)
