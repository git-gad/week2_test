def ask_player_action() -> str:
    choice = input('type H or S\n')
    while True:
        if choice == 'H' or choice == 'S':
            break
        choice = input('not valid\ntype H or S\n')
    return choice

def check_y_n():
    choice = input('want to play more? (y / n)\n')
    while True:
        if choice == 'y' or choice == 'n':
            break
        choice = input('not valid\ntype "y" or "n"\n')
    return choice