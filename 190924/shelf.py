import sys
sys.stdin = open('sample_shelf.txt', 'r')


def shelf(s, he):
    global fi
    if fi < he:
        return
    if he >= height:
        fi = min(fi, he)
        return
    for k in range(s+1, shelfs):
        shelf(k, he+shelf_list[k])


N = int(input())

for tc in range(1, N+1):
    fi = 1e9
    shelfs, height = map(int, input().split())
    shelf_list = list(map(int, input().split()))
    for i in range(shelfs):
        shelf(i, shelf_list[i])
    print('#{} {}'.format(tc, fi-height))
