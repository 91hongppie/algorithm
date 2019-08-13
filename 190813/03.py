import sys
sys.stdin = open('sample_input_03.txt', 'r')

N = int(input())

for i in range(1, N+1):
    play = list(map(int, input().split())) 
    text_list = [[] for i in range(play[0])] 
    test_words = [[] for i in range(play[0])]
    for j in range(play[0]):
        test_words[j] = list(map(str, input()))
    for num in range(play[0]):
        j = l = 0
        text_list3 = []
        while j != len(test_words[num]):
            if test_words[num][j] != test_words[num][-1-l]:
                text_list3 = []
                j = j-l+1
                l = 0
            elif test_words[num][j] == test_words[num][-1-l]:
                text_list3.append(test_words[num][j])
                j += 1
                l += 1
            result = ''.join(text_list3)
            if len(result) == play[1]:
                print('#{} {}'.format(i, result))
        j = l = 0
        text_list3 = []
        while j != len(test_words[num]):
            if test_words[j][num] != test_words[-1-l][num]:
                text_list3 = []
                j = j-l+1
                l = 0
            elif test_words[j][num] == test_words[-1-l][num]:
                text_list3.append(test_words[j][num])
                j += 1
                l += 1
            result = ''.join(text_list3)
            if len(result) == play[1]:
                print('#{} {}'.format(i, result))

