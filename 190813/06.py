import sys
sys.stdin = open('sample_input_06.txt', 'r')

N = int(input())
for i in range(1, N+1):
    num = int(input())
    print('#{} '.format(i))
    result_str = ''
    count = 0
    for nums in range(num):
        alpha = list(map(str, input().split()))
        for k in range(int(alpha[1])):
            result_str += alpha[0]
            count += 1
            if count % 10 == 0:
                print('{}'.format(result_str))
                result_str = ''
    print(result_str)


            


            
