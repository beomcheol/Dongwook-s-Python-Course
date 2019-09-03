from random import randint


class Player:
    name = ""
    health = 30

    def __init__(self, name):
        self.name = name

    @staticmethod
    def attack():
        damage = randint(1, 5)
        print('You attack {}!!'.format(damage))
        return damage

    def attacked(self, damage):
        self.health = max(0, self.health - damage)

    def heal(self):
        recover = randint(1, 10)
        print('Recovery... {}'.format(recover))
        self.health = min(30, self.health + recover)


class Monster:
    NAME = "Goblin"
    health = 10

    @classmethod
    def attack(cls):
        damage = randint(3, 10)
        print('{} attack {}!!!!'.format(cls.NAME, damage))
        return damage

    def attacked(self, damage):
        self.health = max(0, self.health - damage)


class Game:
    player: Player
    monster = Monster()
    turn = 0

    def __init__(self, player_name):
        self.player = Player(player_name)

    def play(self):
        self.print_score()
        while self.player.health and self.monster.health:
            print('\nTurn {}'.format(self.turn + 1))
            cmd = input('Enter the command A(attack) or H(heal): ').lower()
            if cmd == 'a':
                self.monster.attacked(Player.attack())
            elif cmd == 'h':
                self.player.heal()
            else:
                print('Wrong command!')
                continue
            self.player.attacked(Monster.attack())
            self.print_score()
            self.turn += 1

        if self.monster.health == self.player.health:
            print('DRAW')
        elif not self.monster.health:
            print('You WIN!')
        elif not self.player.health:
            print('You lost..')
        else:
            print('DRAW')

    def print_score(self):
        print('{}: {}, {}: {}'.format(self.player.name, self.player.health, self.monster.NAME, self.monster.health))


if __name__ == '__main__':
    name = input('Enter the Player name : ')
    Game(name).play()
