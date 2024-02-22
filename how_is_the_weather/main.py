from math import floor

"""
섭씨를 화씨로 변환하는 프로그램을 작성하라

"F" 는 화씨온도이며, "C" 는 섭씨온도이다
화씨에서 섭씨를 구하는 공식은 다음과 같다

C = 5/9 * (F - 32)

주어진 C 는 -40 - 40 사이이며, F 값역시 동일하다

- 입력

C 로 주어지는 정수

- 출력

섭씨를 화씨로 바꾼 정수

example input

20

exmple output

68
    input("\n", "-" * 50)
"""

# 화씨를 구하는 공식은 다음처럼 변환할수 있다
# F = C / 5/9 + 32
# 여기서 사칙연산을 하는 과정에서 문제가 생긴다
# 위의 공식은 C 와 5/9 로 나누는것이 아닌 C 와 5 를 나눈값과 9 를 나눈다
# F = (C / 5) / 9 + 32
# 이는 원치 않는 결과이다. 그러므로 곱셈식으로 변경한다
# F = C * 9 / 5 + 32

while True:
  C = int(input("섭씨를 입력해주세요(-40 - 40): "))

  if C < -40 or C > 40:
    input("\n", "-" * 50)
    input("\n섭씨는 -40 부터 40 까지의 정수를 입력해주세요\n")
    input("\n", "-" * 50)
    continue

  F = C * 9 / 5 + 32;

  print(f"화씨는 {floor(F)} 입니다.")