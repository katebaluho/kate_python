from tic_tac_toe.game import game_init, game_cycle, game_end


def main():
    game_vars = game_init()
    while True:
        game_cycle(**game_vars)
        if not game_end():
            break
        game_vars = game_init(user = game_vars['users'][0])

main()