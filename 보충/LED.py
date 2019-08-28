import sys
sys.stdin = open('input_led.txt', 'r')

tc = int(input())

for i in range(1, tc+1):
    length = int(input())
    LED_list = list(map(int, input().split()))
    a_list = [0]*len(LED_list)
    count = 0
    for j in range(1, len(LED_list)+1):
        if LED_list[j-1] != a_list[j-1]:
            for k in range(j-1, len(a_list), j):
                if a_list[k] == 0:
                    a_list[k] = 1
                elif a_list[k] == 1:
                    a_list[k] = 0
            count += 1
        if LED_list == a_list:
            break
    print('#{} {}'.format(i, count))