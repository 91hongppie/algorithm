import sys
sys.stdin  = open("sample_input_01.txt", "r")

for h in range(10):
    num = int(input())
    result = []
    for i in range(100):
        nums = list(map(int, input().split())
        sum_x = 0
        sum_y = 0
    for i in range(100):
        for j in range(100):



# for tc in range(1, 11):
#     N = input()
#     arr = [list(map(int, input().split())) for _ in range(100)]
#
#     ans = 0     # 최대값 저장
#     # 행들의 합
#     for i in range(100):
#         S = 0
#         for j in range(100):
#             S += arr[i][j]
#         ans = max(ans, S) # 가장 큰 값만 저장
#     # 열들의 합
#     for i in range(100):
#         S = 0
#         for j in range(100):
#             S += arr[j][i]
#         ans = max(ans, S) # 가장 큰 값만 저장
#     # 좌상단 --> 우하단
#     S = 0
#     for i in range(100):
#         S += arr[i][i]
#     ans = max(ans, S)
#     # 우상단 --> 좌하단
#     S = 0
#     for i in range(100):
#         S += arr[i][99 - i]
#     ans = max(ans, S)
#
#     print(ans)