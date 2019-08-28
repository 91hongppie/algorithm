import sys
sys.stdin = open('sample_card.txt', 'r')

tc = int(input())
for tc in range(1, tc+1):
    cards = input()
    card_list = []
    card_dict = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    for i in range(0, len(cards), 3):
        card_list.append(cards[i:i+3])
    card_set = set(card_list)
    if len(card_set) != len(card_list):
        print('#{} ERROR'.format(tc))
    else:
        for k in card_list:
            card_dict[k[0]] -= 1
        print('#{} {} {} {} {}'.format(tc, card_dict['S'], card_dict['D'], card_dict['H'], card_dict['C']))

