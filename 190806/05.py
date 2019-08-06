import sys
sys.stdin  = open("sample_input_05.txt", "r")

N = int(input())

for i in range(1, N+1):
    num = int(input())
    num_list = list(map(int, input().split()))
    result = []
    mo_list = []
    for k in num_list:
        mo_list.append(k)
        if len(mo_list) == 2:
            result.append(mo_list)
            mo_list = []
    start = []
    back = []
    first = []

    for n in range(1, len(num_list), 2):
        start.append(num_list[n-1])
        back.append(num_list[n])

    for u in start:
        if u not in back:
            first.append(u)
    fi_list = []
    for m in range(0, len(result)):
        if str(first[0]) in str(result[m][0]):
            fi_list.append(result[m])
            break
    for m in range(0, len(result)):
        for v in range(0, len(result)):
            if fi_list[m][1] == result[v][0]:
                fi_list.append(result[v])
            else:
                pass
    print(fi_list)
    re_list = ''
    for l in range(0, len(fi_list)):
        for h in range(2):
            re_list += str(fi_list[l][h]) + ' '

    print('#{} {}'.format(i, re_list))


