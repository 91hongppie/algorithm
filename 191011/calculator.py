import sys
sys.stdin = open('calculator.txt', 'r')


def inorder(n):
    global cal
    if n != 0:
        inorder(child[n][0])

        inorder(child[n][1])
        cal.append(result[n])


for tc in range(1, 11):
    nums = int(input())
    child = [[0, 0] for _ in range(nums+1)]
    result = [0 for _ in range(nums+1)]
    for _ in range(nums):
        arr = list(map(str, input().split()))
        if len(arr) == 3:
            result[int(arr[0])] = arr[1]
            child[int(arr[0])][0] = int(arr[2])
        if len(arr) == 4:
            result[int(arr[0])] = arr[1]
            child[int(arr[0])][0] = int(arr[2])
            child[int(arr[0])][1] = int(arr[3])
        else:
            result[int(arr[0])] = arr[1]
    cal = []
    inorder(1)
    a = []
    for k in range(len(cal)):
        if cal[k] == '+':
            b = a.pop()
            c = a.pop()
            a.append(int(c)+int(b))
        elif cal[k] == '-':
            b = a.pop()
            c = a.pop()
            a.append(int(c)-int(b))
        elif cal[k] == '*':
            b = a.pop()
            c = a.pop()
            a.append(int(c)*int(b))
        elif cal[k] == '/':
            b = a.pop()
            c = a.pop()
            a.append(int(c)/int(b))
        else:
            a.append(cal[k])
    print('#{} {}'.format(tc, int(a[0])))
