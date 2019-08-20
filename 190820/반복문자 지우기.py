import sys
sys.stdin = open('sample_input_04.txt', 'r')

N = int(input())

for i in range(1, N+1):
    words = input()
    word_list = []
    for idx, word in enumerate(words):
        if idx == 0 or len(word_list) == 0:
            word_list.append(word)
        elif word_list[-1] == word:
            word_list.pop()
        else:
            word_list.append(word)
    print('#{} {}'.format(i, len(word_list)))