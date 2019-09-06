import sys
sys.stdin = open('input_harvest.txt', 'r')

N = int(input())

for tc in range(1, N+1):
    rc = int(input())
    result = []
    if rc == 1:
        n = int(input())
        print('#{} {}'.format(tc, n))
        continue
    else:
        for j in range(rc):
            a = list(str(input()))
            result.append(a)
        i = 0
        y = rc - 1
        num = 0

        while i < len(result):
            if i < len(result)//2:
                for k in range(rc//2-i, rc//2+i+1):
                    num += int(result[i][k])
                i += 1
                y -= 1
            elif i == rc//2:
                for k in range(rc//2-i, rc//2+i+1):
                    num += int(result[i][k])
                i += 1
                y -= 1
            else:
                for k in range(rc//2-y, rc//2+y+1):
                    num += int(result[i][k])
                i += 1
                y -= 1
        print('#{} {}'.format(tc, num))







