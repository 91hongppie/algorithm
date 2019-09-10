import sys
sys.stdin = open('sample_bin.txt', 'r')

N = int(input())
for i in range(1, N+1):
    length, words = map(str, input().split())



    a = []
    fi = ''
    for k in range(int(length)):
        result = bin(int(words[k], 16))[2::]
        if len(words[k]) != 4:
            result = '0'*(4-len(result)) + result
        fi += result
    print('#{} {}'.format(i, fi))