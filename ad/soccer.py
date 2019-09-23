import sys
sys.stdin = open('soccer.txt', 'r')
def soccer(c, result):
    global a
    if c == 11:
        a = max(a, result)
        return
    for i in range(11):
        if player_list[i][c]:
            if not visit[i]:
                visit[i] = True
                soccer(c+1, result+player_list[i][c])
                visit[i] = False

N = int(input())
for tc in range(1, N+1):
    a = 0
    player_list = []
    for _ in range(11):
        player_list.append(list(map(int, input().split())))
    visit = [False]*11
    soccer(0, 0)
    print(a)