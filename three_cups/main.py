"""
야바위꾼 앞에  불투명한 컵  3개가  나란히 있다
하나는 왼쪽에 있고, 하나는 가운데, 하나는 오른쪽에 위치한다

공은 가장 왼쪽에 있는 컴 아래에 있다
야바위꾼이 컴의 위치를 교환할때 공의 위치를 추적하는것이 이번 과제이다

- A 왼쪽컵과 가운데 컵을 교환
- B 가운데 컵과 오른쪽 컵을 교환
- C 왼쪽 컵과 오른쪽 컴을 교환

입력

한줄이며, 최대 50 자까지 입력가능
각 문자는 수행하는 위치 교환유형 A, B, C 이다

출력

공의 최종위치를 출력

1: 공이 왼쪽 컵 아래 있을 경우
2: 공이 가운데 컵 아래 있을경우
3: 공이 오른쪽 컵 아래 있을 경우

"""

# 공을 담은 컵 배열
# 공이 있는 원소는 1, 아니면 0
cups = [1, 0, 0]

# swap_type 값을 받아 공의 위치를 변경하는 함수
def swap_ball(swap_type: str):
  temp = None;
  # swap_type 이 A 일때
  # - A 왼쪽컵과 가운데 컵을 교환
  if (swap_type == 'A'):
    temp = cups[0]
    cups[0] = cups[1]
    cups[1] = temp

  # swap_type 이 B 일때
  # - B 가운데 컵과 오른쪽 컵을 교환
  elif (swap_type == 'B'):
    temp = cups[1]
    cups[1] = cups[2]
    cups[2] = temp

  # swap_type 이 C 일때
  # - C 왼쪽 컵과 오른쪽 컴을 교환
  elif (swap_type == 'C'):
    temp = cups[2]
    cups[2] = cups[0]
    cups[0] = temp

while True:
  # swap_types 를 input 으로 받는다
  swap_types = input()

  if not swap_types.isupper():
    print('대문자로 ABC 를 입력해주세요.')
    continue

  # swap_types 는 swap_type 의 시퀀스 문자열이므로
  # 해당 문자를 각각받아서 처리해야 한다
  for swap_type in swap_types:
    # 각 받은 swap_type 을 swap_ball 에 넣어서 실행
    swap_ball(swap_type)

  # 1 의 값을 가진 index 를 찾아서 + 1 한 값이
  # 공의 위치이다.
  print(cups.index(1) + 1)
