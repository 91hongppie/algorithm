import sys
sys.stdin = open('sample_sequence_sum.txt', 'r')

N = int(input())

for i in range(1, N+1):
    se_length, se_nums = map(int, input().split())
    first_sequence = list(map(int, input().split()))
    for j in range(se_nums-1):
        next_sequence = list(map(int, input().split()))
        for idx, k in enumerate(first_sequence):
            if next_sequence[0] < k:
                if idx == 0:
                    first_sequence = next_sequence + first_sequence
                else:
                    left = first_sequence[0:idx]
                    right = first_sequence[idx:]
                    first_sequence = left + next_sequence + right
                break
        else:
            first_sequence = first_sequence + next_sequence
    result_list = []
    print('#{}'.format(i), end=' ')
    for u in range(9):
           print(first_sequence[-1-u], end=' ')
    print(first_sequence[-10])