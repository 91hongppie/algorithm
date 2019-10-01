import sys
sys.stdin = open('test.txt', 'r')

# N = int(input())

# for tc in range(1, N+1):
#     nums = int(input())
#     scores = list(map(int, input().split()))
#     result = [0]*(sum(scores)+1)
#     result[0] = 1
#     for i in scores:
#         for j in range(sum(scores)-1, -1, -1):
#             if result[j]:
#                 result[j+i] = 1
#     a = result.count(1)
#     print('#{} {}'.format(tc, a))

N = int(input())

for tc in range(1, N+1):
    nums = int(input())
    scores = list(map(int, input().split()))
    result = [0]*(sum(scores)+1)
    result[0] = 1
    for i in scores:
        for j in range(len(result)-1, -1, -1):
            if result[j]:
                result[j+i] = 1
    dd = result.count(1)
    print('#{} {}'.format(tc, dd))