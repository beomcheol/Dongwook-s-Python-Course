def print_score():
    print('Player: {}, Monster: {}'.format(player, monster))


if __name__ == '__main__':
    player = 30
    monster = 10
    turn = 0

    print_score()
    while turn < 10:
        print('Turn {}'.format(turn + 1))
        cmd = input('Enter the command A or D or H: ').lower()
        if cmd == 'a':
            print('You attack!!')
            monster -= 2
            monster = max(monster, 0)
        elif cmd == 'd':
            print('You are under attack!!!!')
            player -= 5
            player = max(player, 0)
        elif cmd == 'h':
            print('Recovery...')
            player += 10
            player = min(player, 30)
        else:
            print('Wrong command!')
            continue
        print_score()
        if monster == 0 or player == 0:
            break
        turn += 1

    if not monster:
        print('You WIN!')
    elif not player:
        print('You lost..')
    else:
        print('DRAW')
