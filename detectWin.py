"""
Thomas Bonatti
{river: [card, card, ....],
me: [card, card]
ops: [[card, card], [card, card], ...]
"""
from lib2to3.fixer_util import in_special_context


def checkWin(jsonDict):
    river = jsonDict["river"]
    myHand = jsonDict["me"]
    myScore = getHandRank(myHand + river)
    opponentHands = jsonDict["ops"]
    bestRank = -1
    bestOpponentHand = []

    for hand in opponentHands:
        if bestRank == -1:
            bestOpponentHand = hand
            bestRank = getHandRank(hand + river)
        else:
            current = getHandRank(hand + river)
            if current > bestRank:
                bestRank = current
                bestHand = hand
            elif current < bestRank:
                continue
            else:
                bestHand = compareHighCards(hand, bestHand)
    ####
    if myScore > bestRank:
        return True
    elif myScore == bestRank:
        winner = compareHighCards(myHand, hand)
        if winner == 2:
            return False
        else:
            return True
    else:
        return False


"""gets the best hand made from the cards"""
def getHandRank(cards):
    cards.sort()
    if isStraightFlush(cards):
        return 8
    if isFourOfAKind(cards):
        return 7
    if isFullHouse(cards):
        return 6
    if isFlush(cards):
        return 5
    if isStraight(cards):
        return 4
    if isThreeOfAKind(cards):
        return 3
    if isTwoPair(cards):
        return 2
    if isPair(cards):
        return 1
    else:
        return 0


def isStraightFlush(hand):
    return isFlush(hand) and isStraight(hand)


def isFourOfAKind(hand):
    count = countNumbers(hand)
    return countContainsGroup(count, 4)


def isFullHouse(hand):
    numbCount = countNumbers(hand)
    hasThree = countContainsGroup(numbCount, 3)
    hasTwo = countContainsGroup(numbCount, 2)
    return hasThree and hasTwo


def isFlush(hand):
    suitCount = countSuits(hand)
    for suit in suitCount:
        if suitCount[suit] >= 5:
            return True

    return False


def isStraight(sorted_hand):
    return False
    # TODO fix this
    # # hand must be sorted for this to work
    # sub_hand = sorted_hand.copy()
    # firstVal = int(sub_hand.pop()[0])
    # if straight_helper(sub_hand, firstVal, 1, 1):
    #     return True
    # sub_hand = sorted_hand.copy()
    # return straight_helper(sub_hand, firstVal, -1, 1)


def straight_helper(sub_hand, prev, increment, consecutive):
    if consecutive >= 5:
        return True
    if (len(sub_hand) + consecutive) > 5:
        return False

    currentVal = int(sub_hand.pop()[0])
    if currentVal + increment == prev:
        return straight_helper(sub_hand, currentVal, increment, consecutive+1)
    else:
        return straight_helper(sub_hand, currentVal, increment, 1)


def isThreeOfAKind(hand):
    count = countNumbers(hand)
    return countContainsGroup(count, 3)


def isTwoPair(hand):
    count = countNumbers(hand)
    firstPair = countContainsGroup(count, 2)
    secondPair = countContainsGroup(count, 2)
    return firstPair and secondPair


def isPair(hand):
    count = countNumbers(hand)
    return countContainsGroup(count, 2)


def countContainsGroup(dict, count):
    for key in dict:
        if dict[key] >= count:
            dict[key] = 0
            return True
    return False


def countNumbers(hand):
    numbCount = {}
    for card in hand:
        number = int(card[1:])
        if number in numbCount:
            numbCount[number] += 1
        else:
            numbCount[number] = 1
    return numbCount


def countSuits(hand):
    suitCount = {}
    for card in hand:
        suit = card[0]
        if suit in suitCount:
            suitCount[suit] += 1
        else:
            suitCount[suit] = 1
    return suitCount


def compareHighCards(hand1, hand2):
    if len(hand1) == 0:
        # base case: draw
        return -1
    high1 = findHighestCard(hand1)
    high2 = findHighestCard(hand2)
    if int(high1[1:]) > int(high2[1:]):
        return 1;
    if int(high1[1:]) < int(high2[1:]):
        return 2;
    else:
        high1 = high1.copy()
        high2 = high2.copy()
        removeHighCard(hand1)
        removeHighCard(hand2)
        return compareHighCards(hand1, hand2)



def findHighestCard(hand):
    highCard = hand[0]
    for card in hand:
        highCard = getHighCard(highCard, card)
    return highCard


def getHighCard(card1, card2):
    if int(card1[1:]) >= int(card2[1:]):
        return card1
    else:
        return card2

def removeHighCard(hand):
    hand.remove(findHighestCard(hand))


def parseHand(hand, river):
    cards = []
    for card in hand:
        cards.append(Card(card[0], int(card[1:])))
    for card in river:
        cards.append(Card(card[0], int(card[1:])))
    cards.sort()
    return cards


class Card():

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number