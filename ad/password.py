import sys
sys.stdin = open('password.txt', 'r')


def make(e, result):
    if len(result) == leng:
        c = 0
        for u in mo:
            if u in result:
                c += 1
        if 0 < c <= leng-2:
            te = ''.join(result)
            print(te)
            return
    for k in range(e+1, nums):
        result.append(pass_list[k])
        make(k, result)
        result.pop()


leng, nums = map(int, input().split())
pass_list = list(map(str, input().split()))
pass_list.sort()
mo = ['a', 'e', 'i', 'o', 'u']
c = 0
result = []
for i in range(nums-(leng-1)):
    result.append(pass_list[i])
    make(i, result)
    result.pop()
