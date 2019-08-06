import sys
sys.stdin  = open("sample_input_03.txt", "r")

N = int(input())

for i in range(1, N+1):
    a_list = list(map(int, input().split()))
    A = a_list[1]
    B = a_list[2]
    l = 1
    r = a_list[0]
    A_count = 0
    B_count = 0
    C = 0
    if A == B:
        print('#{} 0'.format(i))
        break
    while C != A:
        if int((l + r) / 2) > A:
            r = int((l + r) / 2)
            C = r
        else:
            l = int((l + r) / 2)
            C = l
        A_count += 1
        if abs(r-l) <= 1:
            break
    l = 1
    r = a_list[0]
    C = 0
    while C != B:
        if int((l + r) / 2) > B:
            r = int((l + r) / 2)
            C = r
        else:
            l = int((l + r) / 2)
            C = l
        B_count += 1
        if abs(r-l) <= 1:
            break
    if A_count > B_count:
        print('#{} B'.format(i))
    elif A_count == B_count:
        print('#{} 0'.format(i))
    else:
        print('#{} A'.format(i))
