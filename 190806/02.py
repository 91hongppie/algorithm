import sys
sys.stdin  = open("sample_input_02.txt", "r")


numbers = [1+i for i in range(12)]
num_list = []
n = len(numbers) # n 원소의 개수
for i in range(1<<n): # 1<<n 부분집합의 개수
    mo_list = []
    for j in range(n): # 원소의 수만큼 비트를 비교함
        if i & (1<<j): # i 의 j 번째 비트가 1이면 j번째 원소 출력
            mo_list.append(numbers[j])
    num_list.append(mo_list)
print(num_list)

N = int(input())
for i in range(1, N+1):
    result = list(map(int, input().split()))
    count = 0
    for k in num_list:
        sum = 0
        if len(k) == result[0]:
            for n in range(result[0]):
                sum += int(k[n])
            if sum == result[1]:
                count += 1
    print('#{} {}'.format(i, count))

