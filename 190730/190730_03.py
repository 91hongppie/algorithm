import sys
sys.stdin  = open("sample_input_03.txt", "r")
num = int(input())
for k in range(1, num+1):
    pages = int(input())
    numbers = input()
    max_num = 0
    card_num = 1



    result = [0]*10
    sum_result = 0
    for i in numbers:
        result[int(i)] += 1
        sum_result += 1
    

    for idx, val in enumerate(result):
        if val == card_num:
            max_num = idx
            card_num = val
        elif val > card_num:
            max_num = idx
            card_num = val
    print('#{} {} {}'.format(k, max_num, card_num)) 


        
            





