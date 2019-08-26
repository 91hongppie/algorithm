def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k) # 답이면 원하는 작업을 한다.
    else:
        k += 1
        ncandidates = construct_candidates(1, k ,input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)


def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def process_solution(a, k):
    result_sum = 0
    for i in range(k+1):
        if a[i]:
            result_sum += i
    if result_sum == 10:
        print("(", end="")
        for i in range(k+1):
            if a[i]:
                print(i, end="")
        print(")")

MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX
backtrack(a, 0, 10)

