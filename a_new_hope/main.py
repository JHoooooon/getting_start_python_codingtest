"""
"내전의 시대에서 반란군이 사악한 시스템에 맞써 첫번째 승리를 거두었습니다"

이는 `start wars` 사건이 먼 은하계에서 일어났다는것을 알고 있다
그런데 얼마나 먼 은하계인지 알수 있을까?

다음의 문장 형식으로 `far` 단어를 특정 횟수만큼 반복하여 설명할수 있다

`A logn time ago in a galaxy far, far away...`

`far` 단어가 두번 반복되는것을 보여준다
그러나 `far` 의 반복은 `N(1 <= N <= 5)번` 이며, `far` 를 제외한 나머지 문장은 변경되지 않는다

`far` 단어의 반복은 마지막 문자를 제외하고 쉼표가 있어야 한다

`N` 이 주어질때, 올바른 문장을 만들수 있는가?

- 입력

정수 `N` 을 입력으로 받는다

- 출력

`N` 번 만큼 반복된 `far` 를 사용하여 해당하는 문장 한줄을 출력

example input:
4

example output: 
A long time ago in a galaxy far, far, far, far away...
"""

while True:
  n = int(input("얼마나 먼 은하계인지 숫자를 입력해주세요: "))

  if n < 1 or n > 5:
    print("\n" + "-" * 30)
    print("\n!!최소 1 에서 5 까지의 정수로 입력해주세요\n")
    print("-" * 30 + "\n")
    continue;

  fars = ("far, " * n)[:-2]

  print("A long time ago in a galaxy", fars, "away...")
  print("\n" + "-" * 30 + "\n")
