import sys
sys.stdin  = open("GNS_test_input.txt", "r")

N=int(input())

for i in range(1, N+1):
    num_dict = {'ZRO':0, 'ONE':0, 'TWO':0, 'THR':0, 'FOR':0, 'FIV':0, 'SIX':0, 'SVN':0, 'EGT':0, 'NIN':0}
    result = ''
    n_list = list(map(str, input().split()))
    num_list = list(map(str, input().split()))
    for j in num_list:
        num_dict[j] += 1

    result += 'ZRO '*num_dict['ZRO']
    result += 'ONE '*num_dict['ONE']
    result += 'TWO '*num_dict['TWO']
    result += 'THR '*num_dict['THR']
    result += 'FOR '*num_dict['FOR']
    result += 'FIV '*num_dict['FIV']
    result += 'SIX '*num_dict['SIX']
    result += 'SVN '*num_dict['SVN']
    result += 'EGT '*num_dict['EGT']
    result += 'NIN '*num_dict['NIN']


    print('#{} {}'.format(i, result))