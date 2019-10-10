def fibo(n):
    global cnt
    cnt += 1
    if n >= 2 and memo[n] == -1:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]


N = 20
cnt = 0
memo = [-1] * (N+1)
memo[0] = 0
memo[1] = 1
print('피보나치 결과:', fibo(N))
print(cnt)


result = [0, 1]
for i in range(N):
    result.append(result[-1]+result[-2])
print(result)
