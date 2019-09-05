import sys
sys.stdin = open('input_nums.txt', 'r')

N = int(input())

for tc in range(1, N+1):
    num_1, num_2 = map(int, input().split())
    j = 1
    result = 0
    a = b = c = d = 0
    for row in range(1, 150):
        if row != 1:
            j = j + row
        result = j
        for col in range(1, 150):
            if col != 1:
                result = result + row + col - 2
            if result == num_1:
                a, b = row, col
            if result == num_2:
                c, d = row, col
    result_x = int(a + c)
    result_y = int(b + d)
    result1 = 0
    j = 1
    for row1 in range(1, 300):
        if row1 != 1:
            j = j + row1
        result1 = j
        for col1 in range(1, 300):
            if col1 != 1:
                result1 = result1 + row1 + col1 - 2
            if row1 == result_x and col1 == result_y:
                print('#{} {}'.format(tc, result1))
                break
        if row1 == result_x and col1 == result_y:
            break





