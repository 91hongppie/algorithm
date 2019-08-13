import sys
sys.stdin = open('sample_input_07.txt', 'r')

N = int(input())

for i in range(1, N+1):
    word = input()
    word_reverse = word[::-1]
    if word == word_reverse:
        print('#{} Exist'.format(i))
        break
        