N = int(input())

for i in range(1, N+1):
    count = 0
    words = input()
    for j in range(len(words)//2):
        if words[j] == words[-1-j]:
            count+=1
        elif words[j] == '*' or words[-1-j] == '*':
            print('#{} Exist'.format(i))
            break
        else:
            print('#{} Not exist'.format(i))
            break
    else:
        print('#{} Exist'.format(i))