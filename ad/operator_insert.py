import sys
sys.stdin = open('operator_insert.txt', 'r')
from itertools import permutations

nums = int(input())
result = list(map(str, input().split()))
operator = list(map(int, input().split()))
operator_list = []
for idx,k in enumerate(operator):
    if idx == 0:
        for y in range(k):
            operator_list.append('+')
    elif idx == 1:
        for y in range(k):
            operator_list.append('-')
    elif idx == 2:
        for y in range(k):
            operator_list.append('*')
    elif idx == 3:
        for y in range(k):
            operator_list.append('/')
calc = ''
operator_set = set()
i = 0
if len(operator_list) == 1:
    calc += str(result[0])
    calc += str(operator_list[0])
    calc += str(result[1])
    print(eval(calc))
    print(eval(calc))
else:
    max_num = -1e10
    min_num = 1e10
    for j in permutations(operator_list, len(operator_list)):
        operator_set.add(j)
        i += 1
    for u in range(len(operator_set)):
        result_operator = ''
        j = operator_set.pop()
        for ho in range(len(result)):
            result_operator += result[ho]
            if ho != 0:
                result_operator = str(int(eval(result_operator)))
            if ho < len(j):
                result_operator += j[ho] 
        max_num = max(max_num, int(result_operator))
        min_num = min(min_num, int(result_operator))
    print(max_num)
    print(min_num)




        
