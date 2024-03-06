# Python 으로 시작하는 코딩 테스트

> 내용은 `Python` 으로 시작하는 코딩테스트의 책 내용을 대략적으로 정리한다
>
> 문제는 `DMOJ` 에서 출제된 문제이다.

## BIG_O

### 고정 시간(Constant Time)

가장 바람직한 알고리즘은 입력 양이 증개해도 더 많은 작업을 수행하지 않는 알고리즘이다
문제의 입력 케이스에 관계없이 이러한 알고리즘은 거의 동일한 수의 단계를 수행한다

이를, 고정 시간 알고리즘이라고 한다

`telemarketers` 문제를 생각해 보자

```py
#   4자리의 번호중 첫자리, 마지막 자리가 8, 9 이고
#   두번째와 세번째 자리가 같다면 telemarketer 번호이다.
#   해당 번호일시, ignore 를 출력하고 아니면 answer 를 출력하라
num1 = int()
num2 = int()
num3 = int()
num4 = int()

if ((num1 == 8 or num1 == 9) and
    (num4 == 8 or num4 == 9) and
    (num2 = num3)):

    print('ignore')
else:
    print('answer')

```

이 솔류션은 전화번호가 4자리가 무엇이든 상관없이 동일한 양의 작업을 수행한다
코드는 입력을 읽는 것으로 시작해 num1, num2, num3, num4 와 몇가지 비교를 수행한다

2장의 앞부분에서 Winning Team 문제를 풀었다

```py
#   사과팀과 바나나팀중 더 많은 점수를 얻은 팀을 찾아내는 문제이다
#   3점, 2점, 1점을 낼수있는 각 점수를 얻을수 있다
#   사과팀이 이겼으면 A 를, 바나나팀이 이겼으면 B 를, 비겼으면 T 를 출력하라

apple_three = int(input())
apple_two = int(input())
apple_one = int(input())

banana_three = int(input())
banana_two = int(input())
banana_one = int(input())

apple_total = apple_three * 3 + apple_two * 2 + apple_one
banana_total = banana_three * 3 + banana_two * 2 + banana_one
```
