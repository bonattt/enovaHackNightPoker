"""
Thomas Bonatti
{river: [card, card, ....],
me: [card, card]
ops: [[card, card], [card, card], ...]
"""


def checkWin(json_dict):
    river = json_dict["river"]
    my_hand = sorted(json_dict["me"] + river)
    my_score = get_hand_rank(my_hand)
    opponent_hands = json_dict["ops"]
    for k in range(len(opponent_hands)):
        opponent_hands[k] = sorted(opponent_hands[k] + river)

    best_rank = -1

    for hand in opponent_hands:
        if best_rank == -1:
            best_hand = hand
            best_rank = get_hand_rank(hand)
        else:
            current = get_hand_rank(hand)
            if current > best_rank:
                best_rank = current
                best_hand = hand
            elif current < best_rank:
                continue
            else:
                best_hand = compare_high_cards(hand, best_hand)
    ####
    if my_score > best_rank:
        return True
    elif my_score == best_rank:
        winner = compare_high_cards(my_hand, hand)
        if winner == 2:
            return False
        else:
            return True
    else:
        return False


"""gets the best hand made from the cards"""
def get_hand_rank(cards):
    cards.sort()
    # if is_straight_flush(cards):
    #     return 8
    if is_four_of_a_kind(cards):
        return 7
    if is_full_house(cards):
        return 6
    if is_flush(cards):
        return 5
    # if is_straight(cards):
    #     return 4
    if is_three_of_a_kind(cards):
        return 3
    if is_two_pair(cards):
        return 2
    if is_pair(cards):
        return 1
    else:
        return 0


def is_straight_flush(hand):
    return is_flush(hand) and is_straight(hand)


def is_four_of_a_kind(hand):
    count = count_numbers(hand)
    return count_contains_group(count, 4)


def is_full_house(hand):
    numbCount = count_numbers(hand)
    hasThree = count_contains_group(numbCount, 3)
    hasTwo = count_contains_group(numbCount, 2)
    return hasThree and hasTwo


def is_flush(hand):
    suitCount = count_suits(hand)
    for suit in suitCount:
        if suitCount[suit] >= 5:
            return True

    return False


def is_straight(sorted_hand):
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

    currentVal = sub_hand.pop().number
    if currentVal + increment == prev:
        return straight_helper(sub_hand, currentVal, increment, consecutive+1)
    else:
        return straight_helper(sub_hand, currentVal, increment, 1)


def is_three_of_a_kind(hand):
    count = count_numbers(hand)
    return count_contains_group(count, 3)


def is_two_pair(hand):
    count = count_numbers(hand)
    firstPair = count_contains_group(count, 2)
    secondPair = count_contains_group(count, 2)
    return firstPair and secondPair


def is_pair(hand):
    count = count_numbers(hand)
    return count_contains_group(count, 2)


def count_contains_group(dict, count):
    for key in dict:
        if dict[key] >= count:
            dict[key] = 0
            return True
    return False


def count_numbers(hand):
    numbCount = {}
    for card in hand:
        if int(card[1:]) in numbCount:
            numbCount[int(card[1:])] += 1
        else:
            numbCount[int(card[1:])] = 1
    return numbCount


def count_suits(hand):
    suit_count = {}
    for card in hand:
        suit = card[0]
        if suit in suit_count:
            suit_count[suit] += 1
        else:
            suit_count[suit] = 1
    return suit_count


def compare_high_cards(hand1, hand2):
    if len(hand1) == 0:
        # base case: draw
        return -1
    high1 = find_highest_card(hand1)
    high2 = find_highest_card(hand2)
    if int(high1[1:]) > int(high2[1:]):
        return 1;
    if int(high1[1:]) < int(high2[1:]):
        return 2;
    else:
        high1 = high1.copy()
        high2 = high2.copy()
        remove_high_card(hand1)
        remove_high_card(hand2)
        return compare_high_cards(hand1, hand2)



def find_highest_card(hand):
    highCard = hand.value
    for card in hand:
        highCard = get_high_card(highCard, card)
    return highCard


def get_high_card(card1, card2):
    if int(card1[1:]) >= int(card2[1:]):
        return card1
    else:
        return card2

def remove_high_card(hand):
    hand.remove(find_highest_card(hand))


def parse_hand(hand, river):
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