import sys
sys.stdin = open('lunch.txt', 'r')

def lunch(stair1, stair2, nums):
    if len(stair1) + len(stair2) == len(people):
        time(stair1, stair2) 
        return
    leng1 = abs(stairs[0][0] - people[nums][0]) + abs(stairs[0][1] - people[nums][1])
    leng2 = abs(stairs[1][0] - people[nums][0]) + abs(stairs[1][1] - people[nums][1])
    stair1.append([leng1, *people[nums]])
    lunch(stair1, stair2, nums+1)
    stair1.pop()
    stair2.append([leng2, *people[nums]])
    lunch(stair1, stair2, nums+1)
    stair2.pop()

def time(list1, list2):
    global answer
    list_1 = sorted(list1)
    list_2 = sorted(list2)

    a = b = result_a = result_b = 0
    if len(list_1) > 3:
        if list_1[-1][0] - list_1[-4][0] < stairs[0][2]:
            a = (stairs[0][2] + list_1[-4][0] + 1) - list_1[-1][0]
        
    if len(list_2) > 3:
        if list_2[-1][0] - list_2[-4][0] < stairs[1][2]:
            b = (stairs[1][2] + list_2[-4][0] + 1) - list_2[-1][0]
    if len(list_1) > 0:
        if a == 0:
            result_a = list_1[-1][0] + 1 + stairs[0][2]
        else:
            result_a = list_1[-1][0] + a + stairs[0][2]
    if len(list_2) > 0:
        if b == 0:
            result_b = list_2[-1][0] + 1 + stairs[1][2]
        else:
            result_b = list_2[-1][0] + b + stairs[1][2]
    result_len = max(result_a, result_b)
    if result_len < answer:
        answer = result_len
    

N = int(input())

for tc in range(1, N+1):
    rc = int(input())
    room = []
    stairs = []
    people = []
    stair1 = []
    stair2 = []
    answer = 1e9
    for i in range(rc):
        room.append(list(map(int, input().split())))
        for j in range(rc):
            if room[i][j] > 1:
                stairs.append([i, j, room[i][j]])
            elif room[i][j] == 1:
                people.append([i, j])
    lunch(stair1, stair2, 0)
    print('#{} {}'.format(tc, answer))
    