import sys
sys.stdin = open('blackjack.txt', 'r')


cards, nums = map(int, input().split())
card_list = list(map(int, input().split()))
result = []
for i in range(len(card_list)-2):
    for j in range(i+1, len(card_list)-1):
        for k in range(j+1, len(card_list)):
            hu = card_list[i] + card_list[j] + card_list[k]
            if hu <= nums:
                result.append(card_list[i] + card_list[j] + card_list[k])

result.sort()
print(result[-1])
