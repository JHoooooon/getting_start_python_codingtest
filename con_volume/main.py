from math import pi, pow, floor;

"""
직원뿔의 부피를 계산

- 입력
입력은 두줄의 텍스트로 구성
첫번째 라인은 원뿔의 반지름인 정수 r 이고, 두번째라인은 원뿔의 높이인 정수 h 이다.
r 과 h 는 1 과 100 사이의 값이다

- 출력
반지름이 r 이고 높이가 h 인 직원뿔의 부피를 출력하라. 
"""

print("원뿔의 부피를 구하는 프로그램")
print("-" * 20)

r = int(input("원뿔의 반지름을 입력해주세요:\n"))
h = int(input("원뿔의 높이를 입력해주세요:\n"))

result = pi * pow(r, 2) * h / 3

print("원뿔의 지름은", floor(result), "입니다!")