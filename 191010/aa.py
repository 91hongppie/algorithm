import sys
sys.stdin = open('aa.txt', 'r')


def preorder(n):
    if n != 0:
        print(n, end=" ")
        preorder(child[n][0])
        preorder(child[n][1])


def inorder(n):
    if n != 0:
        inorder(child[n][0])
        print(n, end=" ")
        inorder(child[n][1])


def postorder(n):
    if n != 0:
        postorder(child[n][0])
        postorder(child[n][1])
        print(n, end=" ")


N = int(input())
nums = list(map(int, input().split()))
child = [[0, 0] for _ in range(N+1)]
for k in range(0, len(nums), 2):
    if child[nums[k]][0] == 0:
        child[nums[k]][0] = nums[k+1]
    else:
        child[nums[k]][1] = nums[k+1]
print(child)
print()
preorder(1)
print()
inorder(1)
print()
postorder(1)
