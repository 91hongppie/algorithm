import sys
sys.stdin = open('sample_input_01.txt', 'r')

N = int(input())

for i in range(1, N+1):
    row = int(input())
    row_list = [10 for _ in range(row//10)]
    count = 1
    for j in range(row//20):
        mo = ja = 1
        row_list.pop()
        for k in range(j+1):
            row_list[k] = 20
        if row_list.count(10) == 0:
            count += 2**row_list.count(20)
        else:
            for u in range(1, row_list.count(20)+1):
                ja *= len(row_list)-(u-1)
                mo *= u
            count += (ja/mo)*2**row_list.count(20)
    print('#{} {}'.format(i, int(count)))





    

