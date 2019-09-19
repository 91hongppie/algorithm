import sys
sys.stdin = open('input_soccer.txt', 'r')

N = int(input())

for tc in range(1, N+1):
    players = []
    visit = [False for _ in range(11)]
    print(visit)

    for _ in range(11):
        players.append(list(map(int, input().split())))
    for k in range(11):
        visit[k] = True
        foot()
        visit[k] = False