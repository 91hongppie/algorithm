import sys
sys.stdin = open('sample_bank.txt', 'r')

N = int(input())

for i in range(1, N+1):
    bina = list(map(int, input()))
    tern = list(map(int, input()))
    for j in range(len(bina)):
        a = bina[::]
        if a[j] == 0:
            a[j] = 1
        else: 
            a[j] = 0
        for k in range(len(tern)):
            for yo in range(2):
                b = tern[::]
                if b[k] == 0:
                    b[k] = 1 + yo
                elif b[k] == 1:
                    b[k] = 0 + yo*2
                elif b[k] == 2:
                    b[k] = b[k] - yo - 1
                result = result1 = 0
                for he in range(len(a)):
                    result = result * 2 + a[he]
                for ye in range(len(b)):
                    result1 = result1 * 3 + b[ye]
                if result == result1:
                    break
            if result == result1:
                break
        if result == result1:
            break
    print('#{} {}'.format(i, result))



    