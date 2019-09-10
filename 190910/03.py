import sys
sys.stdin = open('03.txt', 'r')

N = int(input())

for i in range(1, N+1):
    num_list = ['211', '221', '122', '411', '132', '231', '114', '312', '213', '112']
    row, length = map(int, input().split())
    passwords = [str(input()) for _ in range(row)]
    kk = '0'*length
    result_list = b = []
    for k in range(row):
        a = ''
        if passwords[k] == kk:
            continue
        if passwords[k] == b:
            continue
        for y in range(length):
            if passwords[k][y] != '0' and passwords[k-1][y] != '0':
                continue
            b = passwords[k]
            result = bin(int(passwords[k][y], 16))[2::]
            if len(passwords[k][y]) != 4:
                result = '0'*(4-len(result)) + result
            a += result
        result_list.append(a)
    
    hohoho = []
    for yo in range(len(result_list)):
        one = zero = 0
        mo_list = []
        mo = []
        count = 0
        for ho in range(len(result_list[yo])):
            if count != 0 and not count % 3:
                for idx, uo in enumerate(num_list):
                    t = 0
                    if int(mo[0])%int(uo[0])==0 and int(mo[1])%int(uo[1])==0 and int(mo[2])%int(uo[2])==0:
                        if int(mo[0]) // int(uo[0]) == int(mo[1]) // int(uo[1]) and int(mo[2]) // int(uo[2]) == int(mo[1]) // int(uo[1]) and int(mo[0]) // int(uo[0]) == int(mo[2]) // int(uo[2]):
                            mo_list.append(idx)
                            if len(mo_list) == 8:
                                if mo_list not in hohoho:
                                    hohoho.append(mo_list)
                                    mo_list = []
                one = zero = count = 0
                mo = []
            if result_list[yo][ho] == '1':
                one += 1
                if result_list[yo][ho+1] == '0':
                    mo.append(str(one))
                    zero = 0
                    count += 1
            elif result_list[yo][ho] == '0' and one != 0:
                zero += 1
                if result_list[yo][ho+1] == '1':
                    mo.append(str(zero))
                    one = 0
                    count += 1

    kkk = fire = 0
    for result_num in hohoho:
        first = last = 0 
        for yo in range(0, len(result_num), 2):
            first += result_num[yo]
            last += result_num[yo+1]
        kkk = first+last
        first = first * 3
        first += last
        if not first % 10:
            fire += kkk
        else:
            continue
    if kkk:
        print('#{} {}'.format(i, fire))
    else:
        print('#{} 0'.format(i))

