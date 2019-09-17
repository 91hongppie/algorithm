import sys
sys.stdin = open('input_work.txt', 'r')


def perm(n, k):


N = int(input())

for tc in range(1, N+1):
    rc = int(input())
    board = [list(map(int, input().split())) for _ in range(rc)]
    visit = [False for _ in range(rc)]
    for j in range(rc):
        for k in range(rc):
            board[j][k] /= 100
