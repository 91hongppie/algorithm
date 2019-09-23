N = 8
visit = [0] * N
cnt = 0
cols = [0] * N  # 퀸의 열값을 저장
# 행 고정시키고 열값 체크! (대각은 따로 체크해줘야한데..)
# 대각 체크하는 방법 => 행값의 차이 == 열값의 차이 이면 대각에 있음.


def Possible(k, c):  # k번 퀸의 열 c가 답이 되는 선택인지 조사
    for i in range(k):  # 0 ~ k-1 번 퀸과 대각에 있는지 조사
        if k - i == abs(c - cols[i]):
            return False
    return True


def nQueen(k):
    if k == N:
        global cnt
        cnt += 1
    else:
        for i in range(N):
            if visit[i] or not Possible(k, i):
                continue
            visit[i] = 1
            cols[k] = i     # k 번 퀸의 열값을 i로 결정
            nQueen(k + 1)
            visit[i] = 0


nQueen(0)
print(cnt)
