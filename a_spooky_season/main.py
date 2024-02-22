"""
"spooky season" 으스스한 시즌

"spooky" 시즌이 도래했으며, 해당 시즌의 "spooking level" 이 얼마나 되는지 찾는 문제이다
"spooking level" 은 S(2 <= S <= 20) 이며, `spoo...ooky` 문자열로 표현된다
이 "spoo..ooky" 문자열의 `o` 가 "spooking level" 이다

- 입력

첫번째 줄은 오직 하나의 정수("S")를 입력한다

- 출력

한줄의 문자열을 출력하며, 이는 주어진 정수("S") 값에 대응된다 
예를 보면 다음과 같다

> input
5

> output
spoooooky
"""

while True: 
  s = int(input("으스스함 Level 을 입력해주세요: "))

  if s < 2 or s > 20:
    print("\n!!" + '-' * 30)
    print("\n2 부터 20 까지의 으스스함 level 을 입력할수 있습니다\n")
    print('-' * 32 + "\n")
    continue;

  result = "sp" + "o" * s + "ky"
  print("\n현재 으스스함은", result, "입니다.")
  break;
  