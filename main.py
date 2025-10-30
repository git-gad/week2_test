from core.game_logic import *
from core.deck import build_standard_deck, shuffle_by_suit
from core.player_io import ask_player_action, check_y_n



if __name__ == "__main__":
    while True:
        deck = build_standard_deck()
        shuffled_deck = shuffle_by_suit(deck)
        player = {'hand': []}
        dealer = {'hand': []}
        run_full_game(shuffled_deck, player, dealer)
        choice = check_y_n()
        if choice == 'n':
            break
        
        