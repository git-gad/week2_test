from core.player_io import ask_player_action

def calculate_hand_value(hand: list[dict]) -> int:
    result = 0
    l = ['J', 'K', 'Q']
    # result = []
    # for card in hand:
    #     if card['rank'] == 'A':
    #         result.append(card)
    #     else:
    #         result.insert(0, card)
    # i = 0
    # for card in hand:
    #     if card['rank'] == 'A':
    #         ace = hand.pop(i)
    #     i += 1
    # hand.append(ace)
            
    for card in hand:
        if card['rank'].isdigit():
            result += int(card['rank'])
        elif card['rank'] in l:
            result += 10
        else: 
            if result + 11 < 22:
                result += 11
            else:
                result += 1
    return result
        
def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player['hand'].append(deck.pop(0))
    player['hand'].append(deck.pop(0))
    dealer['hand'].append(deck.pop(0))
    dealer['hand'].append(deck.pop(0))
    player_score = calculate_hand_value(player['hand'])
    dealer_score = calculate_hand_value(dealer['hand'])
    print(f'your hand: {player_score}')
    print(f'dealer hand: {dealer_score}')

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer['hand']) <= 17:
        dealer['hand'].append(deck.pop(0))
    dealer_score = calculate_hand_value(dealer['hand'])
    return dealer_score
    
def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer) 
    choice = ask_player_action() 
    while choice == 'H':
        player['hand'].append(deck.pop(0))  
        total = calculate_hand_value(player['hand'])
        if total > 21:
            print(f'you got {total}, looser')
            print(f'your hand: {player["hand"]}')
            print(f'dealer hand: {dealer["hand"]}')  
            return
        print(f'you got {total}')
        choice = ask_player_action()
    your_score = calculate_hand_value(player['hand'])
    dealer_score = dealer_play(deck, dealer)
    if dealer_score > 21:
        print(f'your hand: {player["hand"]}')
        print(f'dealer hand: {dealer["hand"]}')  
        print(f'you got {your_score}, dealer got {dealer_score}\ncongratulations!!!')  
    elif your_score > dealer_score:
        print(f'dealer hand: {dealer["hand"]}')  
        print(f'your hand: {player["hand"]}')
        print(f'you got {your_score}, dealer got {dealer_score}\ncongratulations!!!')
    elif your_score == dealer_score:
        print(f'dealer hand: {dealer["hand"]}')  
        print(f'your hand: {player["hand"]}')
        print('its push(draw)')
    else:
        print(f'dealer hand: {dealer["hand"]}')  
        print(f'your hand: {player["hand"]}')
        print(f'you lost with {your_score}, dealer got {dealer_score}\ncome back again')
        
        
    
# deck = build_standard_deck()

# shuffled_deck = shuffle_by_suit(deck)
# player = {'hand': []}
# dealer = {'hand': []}

# run_full_game(shuffled_deck, player, dealer)
# print(shuffled_deck)
# deal_two_each(shuffled_deck, player, dealer)
# print(player)
# print(dealer)
# print(shuffled_deck)
# dealer_play(shuffled_deck, dealer)