## 준비
python 3.7 버전 사용합니다.
homebrew 사용해서 설치하시면 됩니다

`brew install python3`

\*.py로 파일을 하나 만드세요, ide는 pycharm 추천

## 기본
### 실행

```
if __name__ == '__main__':
    pass
```

가 python script 실행되는 기본 entrypoint입니다.
사실 없어도 순차적으로 실행되지만 추후 모듈화때를 대비하여..

### convention
snake_case 입니다.
class 명만 camelCase

상수는 모두 대문자로 씁니다.
private으로 쓸 함수, 변수는 앞에 _를 붙입니다.

### 데이터
#### primitive type
```
int = 1
float = 1.1
char = ‘a’
string = ‘hello world’
```

#### container type
```
list = [1,2,3]
dict = {‘a’: 1}
tuple = (1,2,3)
```

### 출력
`print('hello world')`

### 입력
`input()`

### 분기

```
if CONDITION:
    # do smth
elif SECOND_CONDITION:
    # do smth
else:
    # do smth
```

### 반복문

```
for i in [1,2,3,4,5]:
    if i == 1:
       continue
    if i > 3:
        break
```
continue는 loop를 skip합니다.
break는 loop를 탈출합니다.

### 함수 선언

```
def foo(a, b, *args, **kwargs):
    print(a, b, args, kwargs)
```
\* 는 keywords argument로 지정되지 않은것들이 넘어옵니다.

e.g.

foo(1, 2, 3, 4, 5)
> 1 2 (3, 4, 5) {}

\*는 keywords argument가 넘어옵니다.

foo(1, 2, do=3, smth=4)
> 1 2 () {‘do’: 3, ‘smth’: 4}

## 연습
위의 내용을 이용하여 게임을 만들겁니다.
1. 플레이어의 체력은 30으로 시작합니다.
2. 몬스터의 체력은 10으로 시작합니다.
3. 입력은 10회 입력 받습니다.
1. 입력은 A, D, H 만 받습니다.
4. A 입력시 몬스터의 체력을 2 깍습니다.
5. D 입력시 플레이어의 체력을 5 깍습니다.
6. H 입력시 플레이어의 체력을 10 회복합니다.
7. 플레이어의 체력은 30을 넘을 수 없습니다.
8. 플레이어나 몬스터의 체력이 0이 되면 프로그램을 종료합니다.
9. 매 loop 시마다 플레이어의 체력과 몬스터의 체력을 출력합니다.
10. 프로그램 종료시, 플레이어의 체력이 0이 되면 패배 를 출력하고 몬스터의 체력이 0이 되면 승리 를 출력합니다.