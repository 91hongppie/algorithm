import sys
sys.stdin = open('cut_paper.txt', 'r')

col, row = map(int, input().split())
nums = int(input())
for num in range(nums):
    v, u = map(int, input().split())
    if v == 0:
        max(u, row - u)
    else:
        max(u, col - u)

