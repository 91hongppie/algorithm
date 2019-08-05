import sys
sys.stdin  = open("sample_input_05.txt", "r")
for i in range(1, 11):
    mod = int(input())
    build = list(map(int, input().split()))
    max_floor = 1
    min_floor = 100
    for n in range(1, mod+1):
        for j in range(0, len(build)):
            for k in range(j, len(build)):
                if build[j] > build[k]:
                    build[j], build[k] = build[k], build[j]
        build[0]+=1
        build[-1]-=1
    for j in range(0, len(build)):
            for k in range(j, len(build)):
                if build[j] > build[k]:
                    build[j], build[k] = build[k], build[j]
    
    print('#{} {}'.format(i, build[-1]-build[0]))