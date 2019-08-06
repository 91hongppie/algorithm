import sys
sys.stdin  = open("sample_input_04.txt", "r")

N = int(input())

for i in range(1, N+1):
    num = int(input())
    a_list = list(map(int, input().split()))
    result = []
    for j in range(0, len(a_list)):
        for k in range(j, len(a_list)):
            if a_list[j] > a_list[k]:
                a_list[j], a_list[k] = a_list[k], a_list[j]

    for n in range(0, 5):
        if a_list == []:
            break
        elif a_list != []:
            result.append(str(a_list.pop(-1)))
            result.append(str(a_list.pop(0)))
    result_str = ' '.join(result)


    print('#{} {}'.format(i, result_str))

