import sys
sys.stdin = open('input_fly.txt', 'r')

N = int(input())

for i in range(1, N+1):
    rc, box = map(int, input().split())
    table = []
    result_list = []
    for _ in range(rc):
        table.append(list(map(int, input().split())))
    for r in range(rc-box+1):
        for c in range(rc-box+1):
            result = 0
            for tr in range(r, r+box):
                for tc in range(c, c+box):
                    result += table[tr][tc]
            result_list.append(result)
    print('#{} {}'.format(i, max(result_list)))

