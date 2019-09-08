import sys
sys.stdin = open('operator_insert.txt', 'r')
def ya(u, e):
    global max_num, min_num
    if u == len(result)-1:
        max_num = max(max_num, e)
        min_num = min(min_num, e)
    else:
        for i in range(4):
            if operator[i] > 0:
                if i == 0:
                    operator[i] -= 1
                    ya(u+1, e+result[u+1])
                elif i == 1:
                    operator[i] -= 1
                    ya(u+1, e-result[u+1])
                elif i == 2:
                    operator[i] -= 1
                    ya(u+1, e*result[u+1])
                elif i == 3:
                    operator[i] -= 1
                    ya(u+1, int(e/result[u+1]))
                operator[i] += 1


nums = int(input())
result = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_num = -1e10
min_num = 1e10
ya(0, result[0])
print(max_num, min_num)





        
