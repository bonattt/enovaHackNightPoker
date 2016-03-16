# runs the given amount of simulation for the given player hand, returns the 
def runMonteCarlo(c1, c2, river, player_count, simulations_to_run):
    win_count = 0
    games_played = 0
    for run in range (0, simulations_to_run):
        newDeck = base_deck[:]
        if c1 in newDeck:
            newDeck.remove(c1)
        if c2 in newDeck:
            newDeck.remove(c2)
        for i in range (0, len(river)):
            r_card = river[i]
            if r_card in newDeck:
                newDeck.remove(r_card)
        is_win = simulateGame(c1, c2, river, newDeck, player_count)
        win_count = win_count + is_win
        games_played += 1
    #print (float(win_count) / float(games_played))
    
# simulates game. First builds a new random board state, next checks board state if win or loss
def simulateGame(c1, c2, river, newDeck, player_count):
    my_obj = generateOpponentHands(player_count, newDeck)
    my_hand = [c1, c2]
    my_obj['me'] = my_hand
    my_obj['river'] = generateRiver(river, newDeck)
#     print (my_obj)
#     print(newDeck)
    return checkWin(my_obj)

#generates the opponents' hands based on player count
def generateOpponentHands(player_count, newDeck):
    state_obj = {}
    op_list = []
    for i in range (0, player_count):
        op = getCardSet(newDeck)
        op_list.append(op)
    state_obj['op'] = op_list
    return state_obj

#given a deck, will remove two cards from the deck at random and return the hand drawn
def getCardSet(newDeck):
    count = len(newDeck)
    r_num = random.randrange(0, count, 1)
    op1 = newDeck.pop(r_num)
    count -= 1
    
    r_num = random.randrange(0, count, 1)
    op2 = newDeck.pop(r_num)
    
    return [op1, op2]


# given a deck will return a list of 5 river cards
def generateRiver(river, newDeck):
    for i in range (0, len(river) - 1):
        count = len(newDeck)
        rand = random.randrange(0, count, 1)
        river.append(newDeck.pop(rand))
    return river