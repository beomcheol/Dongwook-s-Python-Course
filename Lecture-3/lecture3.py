from random import randint
import json


class MinMax:
    min: int
    max: int

    def __init__(self, min_max_dic):
        self.min = min_max_dic['min']
        self.max = min_max_dic['max']

    def rand(self):
        return randint(self.min, self.max)


class Player:
    name: str
    health_point = 10
    attack_point = MinMax({'min': 1, 'max': 5})
    level = 1
    exp = 0

    def __init__(self, player_name):
        self.name = player_name

    def attack(self):
        if not self.health_point:
            return 0
        damage = self.attack_point.rand()
        print('{} is attack {}!!'.format(self.name, damage))
        return damage

    def attacked(self, damage):
        self.health_point = max(0, self.health_point - damage)

    def heal(self):
        recover = randint(1, 10)
        print('Recovery... {}'.format(recover))
        self.health_point = min(30, self.health_point + recover)

    def gain_exp(self):
        self.exp += 1
        if self.exp >= self._required_exp_for_next_level():
            self._level_up()
        else:
            self._print_status()

    def is_die(self):
        return self.health_point <= 0

    def _level_up(self):
        self.level += 1
        self.health_point = self._max_health_point()
        self.attack_point = MinMax({'min': 1 + self.level, 'max': 5 + self.level})
        self.exp = 0
        print('Level up!!')
        self._print_status()

    def _required_exp_for_next_level(self):
        return fibonacci(self.level + 2)

    def _max_health_point(self):
        return (self.level - 1) * 3 + 10

    def _print_status(self):
        print('{}\'s Level: {}, exp: {}, HP: {}, AP: {}-{}'
              .format(self.name, self.level, self.exp, self.health_point, self.attack_point.min, self.attack_point.max))


class Monster:
    name: str
    health_point: int
    attack_point: MinMax
    level: int
    monsters_dictionary: dict

    def __init__(self, monster_dic):
        self.name = monster_dic['name']
        self.level = monster_dic['level']
        self.health_point = MinMax(monster_dic['health']).rand()
        self.attack_point = MinMax(monster_dic['attack'])

    @classmethod
    def choice_monster_for_player(cls, player: Player):
        filtered_monsters = []
        for mon_dic in cls.monsters_dictionary:
            mon = Monster(mon_dic)
            if mon.level <= player.level + 1:
                filtered_monsters.append(mon)
        filtered_len = len(filtered_monsters)
        if filtered_len == 1:
            return filtered_monsters[0]
        else:
            return filtered_monsters[randint(0, filtered_len - 1)]

    def attack(self):
        if not self.health_point:
            return 0
        damage = self.attack_point.rand()
        print('{} is attack {}!!!!'.format(self.name, damage))
        return damage

    def attacked(self, damage):
        self.health_point = max(0, self.health_point - damage)

    def is_die(self):
        return self.health_point <= 0

    def print_status(self):
        print('Level: {}, HP: {}, AP: {}-{}'
              .format(self.level, self.health_point, self.attack_point.min, self.attack_point.max))


class Game:
    player: Player
    monster: Monster
    turn = 0

    def play(self, player_name):
        self.player = Player(player_name)

        print('Game Start!!\n')
        self._bring_a_new_monster()
        while not self.player.is_die():
            print('\nTurn {}'.format(self.turn + 1))
            cmd = input('Enter the command A(attack) or H(heal) or Q(quit): ').lower()
            if cmd == 'a':
                self.monster.attacked(self.player.attack())
            elif cmd == 'h':
                print('heal')
                self.player.heal()
            elif cmd == 'q':
                print('Bye Bye ~ ~')
                break
            else:
                print('Wrong command!')
                continue
            self.player.attacked(self.monster.attack())
            self._calculate_fight_result()
            self.turn += 1

    def _bring_a_new_monster(self):
        self.monster = Monster.choice_monster_for_player(self.player)
        print('{} is appear!!'.format(self.monster.name))
        self.monster.print_status()

    def _calculate_fight_result(self):
        self._print_score()
        if self.player.is_die():
            print('You lost...')
            return
        if self.monster.is_die():
            print('{} is Die!! May be a new Monster will appear!!\n...'.format(self.monster.name))
            self.player.gain_exp()
            print('...\n...')
            self._bring_a_new_monster()
            return

    def _print_score(self):
        print('{}: {}, {}: {}\n'
              .format(self.player.name, self.player.health_point, self.monster.name, self.monster.health_point))


def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    name = input('Enter the Player name : ')
    with open('monsters.lib', 'r') as f:
        Monster.monsters_dictionary = json.loads(f.readline())['monsters']
    print('Hello, {}'.format(name))
    Game().play(name)
