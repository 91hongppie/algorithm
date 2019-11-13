import sys
sys.stdin = open('sevendwarf.txt', 'r')

def DFS(num, D_list):
    global dwarf_list
    if len(D_list) == 7 or num == 9:
        if len(D_list)==7 and sum(D_list) == 100:
            a = D_list[::]
            dwarf_list.append(a)
        return 
    D_list.append(nums[num])
    DFS(num+1, D_list)
    D_list.pop()
    DFS(num+1, D_list)
    

nums = []
for _ in range(9):
    nums.append(int(input()))
nums.sort()
result = []
dwarf_list = []
DFS(0, result)
for k in dwarf_list[0]:
    print(k)