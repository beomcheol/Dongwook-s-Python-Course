## 준비
lecture 1 을 이용합니다.

## 사용할 것
### import module
from random import randint 을 통해 모듈을 import 할 수 있습니다.
자세한 함수의 사용법은 검색 혹은 import 이후 help(randint) 를 통해 아실 수 있습니다.

### class
```
class Foo:
    a = 10
    def __init__(self, a):
        self.a = a
    
    def add_a(self, value):
        return self.a + value
    
    @classmethod
    def add_class_a(cls, value):
        return cls.a + value
   
    @staticmethod
    def add_5(value):
        return value + 5
```

와 같은 형식으로 class 선언이 가능합니다. 
__init__은 생성자 입니다.

decorator가 붙지 않은 method는 instance method입니다.
instance variable은 `self.*` 를 통해 접근 가능합니다.

e.g.

`Foo(30).add_a(1)`

> 31

class method는 class variable을 사용하는 method입니다.
class를 instance로 만들지 않아도 사용 가능합니다. 이때 cls.* 통해 class variable을 가져올 수 있습니다.

e.g.

`Foo.add_class_a(5)`

> 15

static method는 instance, class variable을 사용하지 못하는 method입니다.
class를 instance로 만들지 않아도 사용 가능합니다.

e.g.

`Foo.add_5(50)`

> 55


## 연습
lecture 1 의 코드를 player, monster, game 세가지 class로 캡슐화 할겁니다.

1. player의 이름은 생성자를 통해 입력받으세요.
2. player의 기본 체력은 30입니다.
3. player는 attack, heal method를 갖고 있습니다.
4. player의 attack은 1~5까지 random한 int를 return 합니다.
5. player의 heal은 1~10까지 random한 int로 player의 health를 회복합니다.
6. monster 는 ‘goblin’ 이라는 이름을 갖고 있습니다.
7. monster의 기본 체력은 10입니다.
8. monster는 attack method만을 갖고 있습니다.
9. monster의 attack은 3~10까지 random한 int를 return합니다.
10. game class의 method들을 통해 게임을 진행합니다.
11. 최초 사용자(프로그램 구동자)는 플레이어의 이름을 입력받고
12. 매턴 공격 할지, 회복할지를 결정합니다.
13. 그에 따라 플레이어와 몬스터는 공격을 주고 받습니다. (몬스터만 매턴 공격만 합니다.)
둘 중 하나의 체력이 0에 도달하면 게임을 종료합니다.
14. 매턴 플레이어의 체력과 몬스터 체력을 출력하세요.
15. 종료시 lecture 1과 마찬가지로 승리, 패배 메시지를 출력하세요.