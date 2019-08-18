import sys
sys.stdin = open('sample_input_01.txt', 'r')

N = int(input())

for i in range(1, N+1):
    num = int(input())
    synergy_list = []
    material_list = [[]*num for _ in range(num)]
    row = 0
    for j in range(num):
        material_list[j].extend((map(int, input().split())))
    print(material_list)
    
        




