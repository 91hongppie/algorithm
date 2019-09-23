# 순열 생성
arr = 'ABC'
N = len(arr)
order = [0] * N     # 순서를 저장
visit = [False] * N     # 함수 호출마다 매번 부른다...(전역변수로 빼자..)


def perm(a, k, n):  # 배열, k, input
    if k == n:
        print(a)
        # for idx in a:
        #     print(arr[idx], end='')
        # print()
        # process_solution()
    else:
        for i in range(n):
            if not visit[i]:
                continue
            visit[i] = True
            a[k] = i
            perm(a, k + 1, n)
            visit[i] = False


perm(order, 0, N)

# ----------- 비트연산자 이용 ---------------
arr = 'ABC'
N = len(arr)
order = [0] * N


def perm(a, k, n, visit):  # 배열, k, input
    if k == n:
        print(a)
        # for idx in a:
        #     print(arr[idx], end='')
        # print()
        # process_solution()
    else:
        for i in range(n):
            if visit & (1 << i):
                continue
            a[k] = i
            perm(a, k + 1, n, visit | (1 << i))


perm(order, 0, N, 0)
