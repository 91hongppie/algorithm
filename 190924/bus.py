import sys
sys.stdin = open('sample_bus.txt', 'r')


def bus(s, fuel, cnt):
    global result, gas
    if result < cnt:
        return
    if s == station-1:
        result = min(result, cnt)
    else:
        if fuel > 0:
            bus(s+1, fuel-1, cnt)
        if fuel >= 0:
            bus(s+1, gas[s]-1, cnt+1)


N = int(input())
for tc in range(1, N+1):
    station, *gas = map(int, input().split())
    result = 1e9
    bus(0, gas[0], 0)
    print('#{} {}'.format(tc, result))
