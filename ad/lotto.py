import sys
sys.stdin = open('lotto.txt', 'r')


def lot(s, cnt, result):
    if cnt == 6:
        print(*result)
    else:
        if s < len(lotto)-1:
            result.append(lotto[s+1])
            lot(s+1, cnt+1, result)
            result.pop()
            lot(s+1, cnt, result)


lotto = []
while not lotto:
    lotto = list(map(int, input().split()))
    if lotto[0] == 0:
        break
    for i in range(1, len(lotto)-5):
        result = []
        result.append(lotto[i])
        lot(i, 1, result)
    lotto = []
    print()
