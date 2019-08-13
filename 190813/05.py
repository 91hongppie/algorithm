import sys
sys.stbdin = open('sample_input_05.txt', 'r')

N = 10

for i in range(1, N+1):
    num = int(input())
    test_words = [[] for i in range(100)]
    count = 0
    for j in range(100):
        test_words[j] = list(map(str, input()))
    for num in range(100):
        j = l = 0
        text_list3 = []
        test_words_list = []
        test_words_list1 = []
        while j != len(test_words[num]):
            if test_words[num][j] != test_words[num][-1-l]:
                text_list3 = []
                j = j-l+1
                l = 0
            elif test_words[num][j] == test_words[num][-1-l]:
                text_list3.append(test_words[num][j])
                j += 1
                l += 1
            if len(result) < len(text_list3):
                result = ''.join(text_list3)
        
            
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
            if len(result) < len(text_list3):
                result = ''.join(text_list3)
        print('#{} {}'.format(i, result))
