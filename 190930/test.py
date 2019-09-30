import sys
sys.stdin = open('test.txt', 'r')


# def test(c, rc):
#     global result, nums
#     if rc not in result:
#         result.append(rc)
#     if c == nums:
#         return
#     test(c+1, rc+scores[c])
# test(c+1, rc)


N = int(input())

for tc in range(1, N+1):
    nums = int(input())
    scores = list(map(int, input().split()))
    result = [0]
    for i in range(len(scores)):
        for j in range(len(result)):
            if result[j]+scores[i] not in result:
                result.append(result[j]+scores[i])
    print(result)
    print('#{} {}'.format(tc, len(result)))
