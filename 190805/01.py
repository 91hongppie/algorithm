import sys
sys.stdin  = open("sample_input_01.txt", "r")

result = []
x = []

for h in range(10):
    num = int(input())
    result = []
    x = []
    for i in range(100):
        num = input().split()
        sum_x = 0
        sum_y = 0
        for j in num:
            sum_x += int(j)
            sum_y += int(num[i][j])
        x.append(sum)
        print(x)






    #
    # sum = 0
    # for j in range(100):
    #     sum += int(result[i][j])
    # x.append(sum)
    #
    # for i in range(100):
    #     sum = 0
    #     for k in range(100):
    #         sum += int(result[k][i])
    #     x.append(sum)
    # sum = 0
    # for i in range(100):
    #     sum += int(result[i][i])
    # x.append(sum)
    # sum = 0
    # count = 0
    # for i in range(99, -1, -1):
    #     sum += int(result[count][i])
    #     count+=1
    # x.append(sum)
    # max_num = 0
    # for i in range(len(x)):
    #     if max_num < x[i]:
    #         max_num = x[i]
    # print('#{} {}'.format(h+1, max_num))