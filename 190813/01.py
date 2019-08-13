import sys
sys.stdin = open('sample_input_01.txt', 'r')

N = int(input())

for i in range(N):
    words = input()
    test_words = input()

    if words in test_words:
        print('#{} 1'.format(i+1))
    else:
        print('#{} 0'.format(i+1))
