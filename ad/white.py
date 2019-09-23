import sys
sys.stdin = open('white.txt', 'r')


def hun(s, he, pe):
    global result, result_list
    if s < len(hu):
        if len(pe) == 7:
            if he == 100:
                for i in range(7):
                    print(pe[i])
        else:
            pe.append(hu[s])
            hun(s+1, he+hu[s], pe)
            pe.pop()
            hun(s+1, he, pe)


hu = []
pe = []
result_list = []
result = 0
for _ in range(9):
    hu.append(int(input()))
hu.sort()
hun(0, 0, pe)
