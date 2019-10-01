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
    result = [0]*(sum(scores)+1)
    result[0] = 1
    u = 0
    for i in range(len(scores)):
        for j in range(sum(scores), -1, -1):
            u += 1
            if result[j]:
                result[scores[i]+j] = 1
    a = result.count(1)
    print(u)
    print('#{} {}'.format(tc, a))
