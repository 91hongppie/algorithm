import sys
sys.stdin = open('sample_column.txt', 'r')

N = int(input())

for i in range(1, N+1):
    words_list = []
    max_length = 0
    for j in range(5):
        words = input()
        words_list.append(list(words))
        if j > 0 and len(words_list[j]) >= max_length:
            max_length = len(words_list[j])
        elif j == 0:
            max_length = len(words_list[j])

    result = ''
    for k in range(max_length):
        for h in range(5):
            if k >= len(words_list[h]):
                pass
            else:
                result += words_list[h][k]
    print('#{} {}'.format(i, result))








#1 Aa0FfBb1GgCc2HhDd3IiEe4Jj
#2 Aa0aPAf985Bz1EhCz2W3D1gkD6x