import sys
sys.stdin = open('sample_input.txt', 'r')

N = int(input())

for i in range(1, N+1):
    fuel, distance, charger = map(int, input().split())
    charge = list(map(int, input().split()))
    for k in range(len(charge)):
        if 



