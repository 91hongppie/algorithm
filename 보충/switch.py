import sys
sys.stdin = open('input_switch.txt', 'r')

tc = int(input())

room = list(map(int, input().split()))
students = int(input())
for j in range(students):
    student, num = map(int, input().split())
    if student == 1:
        for switch in range(num-1, len(room), num):
            if room[switch] == 1:
                room[switch] = 0
            else:
                room[switch] = 1
    else:
        i = num-1
        j = num-1
        while i < tc and j >= 0 and room[i] == room[j]:
            if room[i] == room[j]:
                if room[i] == 1:
                    room[i] = 0
                    room[j] = 0
                else:
                    room[i] = 1
                    room[j] = 1
            i += 1
            j -= 1

for k in range(len(room)):
    if k > 0 and k % 20 == 0: 
        print()
        print(room[k], end=' ')
    elif k == len(room)-1:
        print(room[k])
    else:
        print(room[k], end=' ')