import sys
sys.stdin = open('sample_input_04.txt', 'r')

N = 10

for i in range(1, N+1):
    play = int(input())
    test_words = [[] for i in range(8)]
    count = 0
    for j in range(8):
        test_words[j] = list(map(str, input()))
    for num in range(8):
        j = l = 0
        text_list3 = []
        test_words_list = []
        test_words_list1 = []
        while j != len(test_words[num])-play+1:
            test_words_list = test_words[num][j:j+play]
            test_words_list1 = test_words_list[::-1]      
            j += 1
            if test_words_list == test_words_list1:
                count += 1
            
        j = l = 0       
        while j != len(test_words[num])-play+1:
            test_words_list = []
            test_words_list1 = []
            for k in range(play):
                test_words_list.append(test_words[j+k][num])
            test_words_list1 = test_words_list[::-1]
            if test_words_list == test_words_list1:
                count += 1
            j += 1
    print('#{} {}'.format(i, count))