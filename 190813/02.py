import sys
sys.stdin = open('sample_input_02.txt', 'r')

N = int(input())

for i in range(1, N+1):
    result = 0
    my_dict = {}
    words = input()
    test_words = input()
    for j in test_words:
        if j not in my_dict.keys() and j in words:
            my_dict[j] = 1
        elif j in my_dict.keys():
            my_dict[j] += 1
    for val in my_dict.values():
        if val > result:
            result = val

    print('#{} {}'.format(i, result))