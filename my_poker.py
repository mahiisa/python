import random
from pprint import pprint as pp
from collections import defaultdict

def deal(num, n=5, deck=[r+s for r in "23456789TJQKA" for s in "HDSC"]):
    random.shuffle(deck)
    return [deck[i*n:(i+1)*n] for i in range(num)]

def hand_rank(hand):
    ranks = card_rank(hand)
    if flush(hand) and straight(ranks):
        return 8, max(ranks)
    if kind(4,ranks):
        return 7, kind(4,ranks), ranks
    if kind(3, ranks) and kind(2, ranks):
        return 6, kind(3, ranks), kind(2, ranks)
    if flush(hand):
        return 5, max(ranks)
    if straight(ranks):
        return 4, max(ranks)
    if kind(3, ranks):
        return 3, kind(3, ranks), ranks
    if two_pair(ranks):
        return 2 , two_pair(ranks), ranks
    if kind(2, ranks):
        return 1, kind(2, ranks), ranks
    return 0 , ranks


def poker(hands):
    if hands.count(max(hands, key=hand_rank)) ==2 :
        print("2 winner" , max(hands, key=hand_rank))
    else:
        return max(hands , key=hand_rank)


def card_rank(hand):
    return sorted(["__23456789TJQKA".index(r) for r,_ in hand], reverse=True)

def straight(rank):
    if 14 in rank:
        return (max(rank) - min(rank) == 4 or max(rank) - min(rank) == 12) and len(set(rank)) == 5
    else:
        return max(rank) - min(rank) == 4 and len(set(rank)) == 5

def flush(hand):
    return len(set([s for _,s in hand])) ==1

def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return r

def two_pair(ranks):
    high_pair = kind(2,ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if high_pair and high_pair != low_pair:
        return high_pair, low_pair


def test():
    h1 = ['7H', '8S', '7S', '8H', 'KC']
    cr1 = [13, 8, 8, 7, 7]
    h2 = ['7H', '8S', '6S', '9H', 'TC']
    cr2 = [6 , 7, 8, 9, 10]
    h3 = ['7H', '8H', '6H', '9H', 'TH']
    h4 = ['3H', '2H', 'AH', '5H', '4H']
    h5 = ['3H', '3S', '3D', '5C', '4H']
    h6 = ['5C', '5D', 'QH', 'QC', 'TC']
    assert card_rank(h1)== cr1
    assert straight(card_rank(h2)) is True
    assert straight(card_rank(h1)) is False
    assert straight(card_rank(h4)) is True
    assert flush(h3) is True
    assert kind(3, card_rank(h5)) == 3
    assert two_pair(card_rank(h6)) == 12, 5

    return "you are green!"


#print(test())





#hands = deal(4)
#pp(hands)
#print()
#print(poker(hands))

def hand_percentage(n=700*1000):
    d = defaultdict(int)
    for _ in range(n//10):
        for hand in deal(10):
            d[hand_rank(hand)[0]] += 1

    print(d)


hand_percentage(10)