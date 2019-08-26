import sys
sys.stdin = open('input_palindrome2.txt', 'r')

for i in range(1, 11):
    n = int(input())
    board = [list((input())) for _ in range(100)]
    result = 0
    for r in range(100):
        i = j = 0
        
            

            if row == row_reverse:
                if result < len(row):
                    result = len(row)
        for tc in range(100):
            col_reverse = col[99:tc-1:-1]
            if col == col_reverse:
                if result < len(col):
                    result = len()

    print(result)





