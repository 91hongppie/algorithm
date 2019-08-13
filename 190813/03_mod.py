import sys
sys.stdin = open('sample_input_03.txt', 'r')

N = int(input())

for i in range(1, N+1):
    play = list(map(int, input().split())) 
    test_words = [[] for i in range(play[0])]
    for j in range(play[0]):
        test_words[j] = list(map(str, input()))
    for m in range(play[0]):
        for n in range(play[0]):
            mo_list = test_words[m][n:play[0]:]