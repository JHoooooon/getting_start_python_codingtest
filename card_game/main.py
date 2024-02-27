"""
2인용 카드 게임을 구현한다

A 와 B 두사람이 카드게임을 하고 있다
게임은 52장의 카드 덱에서 시작한다
덱에 남은 카드가 없을때까지 덱에서 플레이어 A, 플레이어 B, 플레이어 A, 플레이어 B 순서대로 카드를 꺼낸다

덱에는 13종류의 카드가 있다
2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace 이다

덱에는 이런 유형의 카드가 각각 4 장씩있다
예를 들어 2 이 4장, 3 이 4장, ace 가 4장  존재한다.

따라서 (13 가지 유형당 4 개 가있으니 52 장이다)

높은 카드는 jack, queen, king, ace 이다
플레이어가 높은 카드를 받으면 점수를 얻을 수 있으며, 점수를 매기는 규칙은 다음과 같다

- 플레이어가 jack 을 가져간 후 덱에 최소한 1장의 카드가 남아있고
  덱의 다음 카드가 높은 카드가 아닌 경우 플레이어는 1점 얻는다

- 플레이어가 queen 을 가져간 후 덱에 최소한 2장의 카드가 남아있고
  덱의 다음 카드 2장의 카드중 어느것도 높은 카드가 아닌 경우 플레이어는 2점을 얻는다

- 플레이어가 king 을 가져간 후 덱에 최소한 3장의 카드가 남아있고
  덱의 다음 3장의 카드 중 높은 카드가 없으면 플레이어는 3점을 얻는다

- 플레이어가 ace 를 가져간 후 덱에 최소한 4장의 카드가 남아있고 덱의 다음 4장 카드중
  높은 카드가 없으면 플레이어는 4점을 얻는다

* 입력

입력은 52 줄로 구성된다.
각 라인에는 덱에 있는 카드 유형 중 하나가 포함되며,
플레이어가 덱에서 카드를 가져가는 순서대로 입력된다

첫 번째 라인은 덱에서 가져온 카드이고, 두번째 라인은 덱에서 가져온 두번째 카드이다

* 출력

플레이어가 득점할때마다 다음 라인을 출력한다

Player p scores q point(s).

여기서 p 는 플레이어 A 일때 A, 플레이어 B 일때 B 이다
그리고 q 는 방금 득점한 점수이다

게임이 끝나면 다음 두줄을 입력한다

Player A: m point(s)
Player B: n point(s)

m 은 플레이어 A 의 총점이고, n 은 플레이어 B 의 총점이다
"""

# deck
deck = None
# player A point
a_point = 0
# player B point
b_point = 0

#----------------------------------------
# high 카드가 있는지 확인하는 함수
def is_high_card(card: str):
    # high card 목록
    high_card = ['jack', 'queen', 'king', 'ace']

    # high_card 가 있다면 True
    if card in high_card:
        return True
    # 아니면 False
    else:
        return False

#----------------------------------------
# point selector 함수
def point_selector(high_card: str):
    if high_card == 'jack':
        return 1
    elif high_card == 'queen':
        return 2
    elif high_card == 'king':
        return 3
    elif high_card == 'ace':
        return 4

#----------------------------------------
# 포인터 얻는 함수
def get_points(deck: list, high_card: str):
    # high card 목록
    high_card = ['jack', 'queen', 'king', 'ace']

    # deck 에서 high_card 를 가지고 있는지 확인
    # high_card 를 가진다면 지속하지 못하므로 False
    # 아니라면 True
    is_continue = False

    # 포인트를 얻기 위한 최소 소지 카드 수
    least_n = high_card.index(high_card) + 1

    # deck 에 남아있는 카드 갯수
    deck_length = len(deck)

    # 최소 소지 카드수보다 덱 카드 개수가 적으면 return 0
    if deck_length < least_n:
        return 0

    # 주어진 덱에 high_card 가 있는지 확인
    for i in range(least_n):
        # high_card 인지 확인
        # high_card 라면 True 이므로, False 로 변환
        is_continue = not is_high_card(deck[i]);

        # is_continue 가 False 라면 리턴 0
        if is_continue == False:
            return 0;

    # high_card 가 없으므로, 포인트 계산하여 리턴
    return point_selector(high_card)

#----------------------------------------
# player 를 선택하는 함수
def player_selector(idx: int):
    player = None

    # idx 가 0 포함 짝수이면 A
    if (idx % 2 == 0):
        player = 'A'
    # idx 가 홀수이면 B
    else:
        player = 'B'
    # player 반환
    return player

# 게임 플레이 인덱스
# 게임은 한번에 하나의 카드를 가지므로, 
idx = 0

#----------------------------------------
# input 을 받아 deck 을 세팅
def set_deck():
    # 빈배열의 덱
    deck = []

    # 52 번 순회하여 입력을 deck 에 push
    for _i in range(52):
        card = input()
        deck.append(card);
    
    # 덱 반환
    return deck;

#----------------------------------------
# deck 세팅
deck = set_deck()

#----------------------------------------
# Play Game
# idx 값이 52 보다 작거나 같아야 한다
while(idx < 52):
    # player 선택
    player = player_selector(idx)
    card = deck[idx]

    # 입력된 카드를 deck 에서 삭제
    deck.pop(idx);

    # high_card 인지 확인
    if is_high_card(card):
        # high_card 라면 point 를 얻는다
        # 0 - 4 중 하나의 포인트
        point = get_points(deck, card)

        # point 가 0 이 아니라면 output 후 플레이어 포인트 합산
        if point != 0:
            print(f"Player { player } scores { point } point(s).")
            # 얻은 포인트를 player 에 따라 합산
            if player == 'A':
                a_point += point
            else:
                b_point += point

    # 인덱스 증가
    idx += 1

# 출력 포인트 
print(f"Player A: {a_point} point(s).")
print(f"Player B: {b_point} point(s).")