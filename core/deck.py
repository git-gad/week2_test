from random import randint 
    
def build_standard_deck() -> list[dict]:
    deck = []
    ranks = ['J', 'Q', 'K', 'A']
    for card in range(2, 11):
        ranks.append(str(card))
    suits = ['H', 'C', 'D', 'S']
    for rank in ranks:
        for suit in suits:
            card = {'rank': rank, 'suit': suit}
            deck.append(card)
    return deck

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    while swaps > 0:
        i = randint(0, 51)
        j = randint(0, 51)
        if i == j:
            continue
        elif deck[i]['suit'] == 'H':
            if j % 5 == 0:
                deck[i], deck[j] = deck[j], deck[i]
                swaps -= 1    
        elif deck[i]['suit'] == 'C':
            if j % 3 == 0:
                deck[i], deck[j] = deck[j], deck[i]
                swaps -= 1  
        elif deck[i]['suit'] == 'D':
            if j % 2 == 0:
                deck[i], deck[j] = deck[j], deck[i]
                swaps -= 1  
        elif deck[i]['suit'] == 'S':
            if j % 7 == 0:
                deck[i], deck[j] = deck[j], deck[i]
                swaps -= 1 
    return deck
        

