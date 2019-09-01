import sys
sys.stdin = open('input_word.txt', 'r')

N = int(input())

for i in range(1, N+1):
    word_table = []
    rc, length = map(int, input().split())
    result = 0
    for j in range(rc):
        word_table.append(list(map(int, input().split())))
    for k in range(len(word_table)):
        count_r = 0
        for c in range(len(word_table)):
            if word_table[c][k] == 1:
                count_r += 1
            else:
                count_r = 0
            if count_r == 5:
                result += 1

        count = 0
        for u in word_table[k]:
            if u == 1:
                count += 1
            elif u == 0:
                count = 0
            if count == 5:
                result += 1
    print(result)