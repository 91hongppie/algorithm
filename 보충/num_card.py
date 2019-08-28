import sys
sys.stdin = open('input_num_card.txt', 'r')

s_card = int(input())
s_cards = list(map(int, input().split()))
all_card = int(input())
all_cards = list(map(int, input().split()))
card_list = [str(0)]*len(all_cards)
for i in s_cards:
    if i in all_cards:
        card_list[all_cards.index(i)] = str(1)
    else:
        pass
a = ' '.join(card_list)
print(a)
