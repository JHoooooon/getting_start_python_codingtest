"""
어느날 여름 저녁, 사랑하는 치즈군 봉제인형과 함께 웅크린 채 C.C 는 피자를 먹고싶어한다
그녀는 크고 치즈가 듬뿍 들어간 피자를 정말 좋아하지만, 무엇이든 만족하며 먹을수 있다
그녀는 망설임 없이 를르슈의 신용카드를 빼앗고 아주 중요한 전화를 거는데...

- C.C 는 피자의 너비가 3 units 이며 치즈함량이 최소 95% 이상이면 `absolutely` 만족한다
- C.C 는 피자의 너비가 1 units 이며, 치즈함량이 최대 50% 이면 `fairly` 만족한다
- 그외에는 C.C 가 받는 어떤 피자에도 `vary` 한다

- 입력

첫번째 입력 W 는 (1 <= W <= 3) 이며, 피자의 너비이다
두번째 입력 C 는 (0 <= C <= 100) 이며, 최대 치즈 함량이다

- 출력

C.C is M satisfacation with her pizza 를 출력

M 은 `absolutely`, `fairly`, `vary` 중 하나를 가리킨다

"""

W = int(input())
C = int(input())
SATISFACATION = ['absolutely', 'fairly', 'vary']

if (W == 3 and C >= 95):
  print(SATISFACATION[0])
elif (W == 1 and C <= 50):
  print(SATISFACATION[1])
else:
  print(SATISFACATION[2])

