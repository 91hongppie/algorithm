# arr = [[9, 20, 2, 18, 11],
#        [19, 1, 25, 3, 21],
#        [8, 24, 10, 17, 7],
#        [15, 4, 16, 5, 6],
#        [12, 13, 22, 23, 14]]

# N, M = len(arr), len(arr[0])

# # dx, dy 각각 리스트로 저장
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# sum = 0
# for x in range(N):
#     for y in range(M):
        

# arr = 'ABC'
# bits = [0] * 3

# def print_set(bits):
#     for i in range(len(bits)):
#         if bits[i]:
#             print(arr[i], end=' ')
#     print()
# for i in range(2):
#     bits[0] = i
#     for i in range(2):
#         bits[1] = i
#         for i in range(2):
#             bits[2] = i
#             print_set(bits)


# 비트 연산자가 좋은 이유
# n =10

# if n % 2 ==0:
#     print('짝수')
# else:
#     print('홀수')

# # 누적되면 차이가있다.
# if n & 1:
#     print('홀수')
# else:
#     print('짝수')


# num = 10
# num2 = 0b1010
# num16 = 0xa
# print(num, num2, num16)

# a =  0b1010
# b = 0b10011
# c = a | b
# print(bin(c))

# # a 짝수이면 0 출력, 홀수이면 1출력
# a = 10

# b = a & 1

# print(b) 


# a 의 모든 수를 왼쪽으로 n칸
# print(a<<1)
# a 의 모든 수를 오

# arr = [3, 6, 7, 1, 5, 4]
# N = len(arr)
# subset = 10

# for subset in range(1 << N):
#     print(subset, end = '>')
#     for j in range(N):
#         if subset & (1 << j):
#             print(arr[j], end=' ')
#     print()
#  연습문제
# arr = [3, 6, -2, 7, -3, 1, -5, -1, 5, 4]
# N = len(arr)
# count = 0

# for subset in range(1<<N):
#     list_arr = []
#     sum = 0
    
#     for j in range(N):
#         if subset & (1 << j):
#             sum += arr[j]
#             list_arr.append(arr[j])
#     if sum == 0:
#         print(subset, end = '>')
#         print(list_arr, end = '\n')
#         count += 1
# print(count)

# arr = []
# key = 123
# lo, hi = 0, len(arr) - 1

# def binarySearch(arr, key):
#     lo, hi = 0, len(arr) - 1

#     while lo <= hi:
#         mid = (lo + hi) >> 1
#         if arr[mid] == key:
#             return mid
#         if arr[mid] > key:
#             hi = mid - 1
#         else:
#             lo = mid + 1
#     return -1


# def binarySearch(arr, lo, hi, key):

#     if lo > hi: return False

#     mid = (lo + hi) >> 1
#     if arr[mid] == key:
#         return True
#     if arr[mid] > key:
#         return binarySearch(arr, lo, mid - 1, key)
#     else:
#         return binarySearch(arr, mid+1, hi, key)

# arr = [64, 25, 10, 22, 11]
# N = len(arr)
# # [0, n-1] 최소값의 위치를 찾는다.

# for i in range(N-1):
#     minIdx = i
#     for j in range(i +1, N):
#         if arr[minIdx] > arr[j]:
#             minIdx = j
#     arr[i], arr[minIdx] = arr[minIdx], arr[i]

# print(arr)

arr = [ [9, 20, 2, 18, 11],
        [19, 1, 25, 3, 21],
        [8, 24, 10, 17, 7],
        [15, 4, 16, 5, 6],
        [12, 13, 22, 23, 14]]

x, y = len(arr), len(arr[0])
print(x, y)