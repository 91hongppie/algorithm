import sys
sys.stdin = open('alpha.txt', 'r')


def inorder(n):
    if n != 0:
        inorder(child[n][0])
        print(alpha[n], end="")
        inorder(child[n][1])


for tc in range(1, 11):
    nums = int(input())
    alpha = [0] * (nums+1)
    child = [[0, 0] for _ in range(nums+1)]
    for i in range(nums):
        mo = list(map(str, input().split()))
        alpha[int(mo[0])] = mo[1]
        if len(mo) == 3:
            child[int(mo[0])][0] = int(mo[2])
        if len(mo) == 4:
            child[int(mo[0])][0] = int(mo[2])
            child[int(mo[0])][1] = int(mo[3])
    print('#{}'.format(tc), end=" ")
    inorder(1)
    print()
