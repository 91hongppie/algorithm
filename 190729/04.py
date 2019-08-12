import sys
sys.stdin = open("sample_input_4.txt", "r")

N = int(input())

for i in range(N):
    sum_max = 0
    sum_min = 0
    all_part = list(map(int, input().split()))
    num_list = list(map(int, input().split()))

    for j in range(all_part[0] - all_part[1] + 1):
        sum_mo = 0
        for k in range(all_part[1]):
            sum_mo += num_list[j+k]
        if j == 0:
            sum_max = sum_mo
            sum_min = sum_mo
        else:
            if sum_mo > sum_max:
                sum_max = sum_mo
            elif sum_mo < sum_min:
                sum_min = sum_mo
    print('#{} {}'.format(i+1, sum_max-sum_min))
