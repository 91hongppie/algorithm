import sys
sys.stdin = open('03.txt', 'r')

N = int(input())

for i in range(1, N+1):
    row, lenth = map(int, input().split())
    passwords = [list(map(str, input().split())) for _ in range(row)]
    a = format(int('1DB176C588D26EC', 16), 'b')
    a = '0' + a
    print(a)

    
