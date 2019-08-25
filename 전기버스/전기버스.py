import sys
sys.stdin = open('sample_input.txt', 'r')

N = int(input())

for i in range(1, N+1):
    fuel, distance, charger = map(int, input().split())
    charge = list(map(int, input().split()))
    gas = fuel
    count = 0
    for k in range(distance + 1):
        if gas >= 0:
            if k in charge:
                if k == charge[-1]:
                    if distance-charge[charge.index(k)] > gas:
                        gas = fuel
                        count += 1
                else:
                    if charge[charge.index(k)+1]-charge[charge.index(k)] > gas:
                        gas = fuel
                        count += 1
        elif gas < 0:
            print('#{} 0'.format(i))
            break
        gas -= 1
    else:
        print('#{} {}'.format(i, count))
