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
#   최대 100 점까지 득점이 가능하며,
#   사과팀이 이겼으면 A 를, 바나나팀이 이겼으면 B 를, 비겼으면 T 를 출력하라

apple_three = int(input())
apple_two = int(input())
apple_one = int(input())

banana_three = int(input())
banana_two = int(input())
banana_one = int(input())

apple_total = apple_three * 3 + apple_two * 2 + apple_one
banana_total = banana_three * 3 + banana_two * 2 + banana_one

if apple_total > banana_total:
    print('A')
elif apple_total < banana_total:
    print('B')
else:
    print('T')
```

이역시, 항상 같은 양의 작업을 수행한다
하지만, 3점슛을 수억개나 기록했다면, 이는 오래걸릴수 있다

하지만, 각 유형의플레이에서 최대 100점까지 득점한다고 적혀있다
이러한 작은 숫자로 작업하게 된다면, 컴퓨터는 일정한 수의 단계로 이 숫자를
읽거나 작업할 수 있다고 말할수 있다

일반적으로 수십억까지의 숫자는 `작은것` 이라 생각할수 있다

`Big O` 에서 고정 시간 알고리즘을 `O(1)` 이라고 한다
`1` 은 고정 시간 알고리즘에서 한단계만 수행한다는 것이 아니다

`10` 또는 `10000` 과 같이 고정된 수의 단계를 수행하더라도 여전히 고정시간 작업이다
모든 고정 시간 알고리즘은 `O(1)` 로 표시된다

### 선형시간 (Linear Time)

대부분의 알고리즘은 고정 시간 알고리즘이 아니며, 입력 양만큼의 작업을 수행한다
예를 들어, 입력 10 개를 처리하는것 보다 1000 개를 처리하는데 더 많은 작업을 수행한다

이러한 알고리즘을 서로 구별하는것은 입력양고 알고리즘이 수행하는 작업량의 관계이다

선형 시간 알고리즘은 입력 양ㅇ과 수행된 작업량의 사이에 선형 관계가 있는 알고리즘이다
50 개의 값이 있는 입력에 대해 선형 시간 알고리즘을 실행한 다음, 100 개의 값이 있는 입력에 대해
다시 실행한다고 가정해보자.

알고리즘 값이 50개인 경우에 비해 약 2배의 작업을 수행한다

```py
"""
<< 풀이는 책의 솔루션으로 대체한다 >>

야바위꾼 앞에  불투명한 컵  3개가  나란히 있다
하나는 왼쪽에 있고, 하나는 가운데, 하나는 오른쪽에 위치한다

공은 가장 왼쪽에 있는 컵 아래에 있다
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
swaps = input()

ball_location = 1

for swap_type in swaps:
    if swap_type == 'A' and ball_location == 1:
        ball_location = 2
    elif swap_type == 'A' and ball_location == 2:
        ball_location = 1
    elif swap_type == 'B' and ball_location == 2:
        ball_location = 3
    elif swap_type == 'B' and ball_location == 3:
        ball_location = 2
    elif swap_type == 'C' and ball_location == 3:
        ball_location = 1
    elif swap_type == 'C' and ball_location == 1:
        ball_location = 3

print(ball_location)
```

위의 `swaps` 의 문자개수에 따라 루프가 달라진다
이 알고리즘이 수행하는 작업량은 위치 이동의 수에 정비례한다

입력의 양이 `n` 이라면, `n` 은 위치이동의 횟수이다
수행하는 `5` 개 위치이동이 있는 경우 `n` 은 `5` 이다

`n` 개의 위치 이동이 있는 경우 프로그램은 `n` 개의 작업을 수행한다
`for` 루프가 `n` 번 반복을 수행하고, 각 반복이 일정한 수의 단계를 수행하기 때문이다

일정한 수라면 각 반복에 얼마나 많은 단계를 수행하는지 상관하지 않는다

알고리즘이 총 `n` 단계를 수행하든, `10n` 을 수행하든, `1000n` 을 수행하든
이는 선형 시간 알고리즘이다

`Big O` 에서는 이를 `O(n)` 이라 한다

`n` 이 `10n` 을 수행하더라도 이는 `n` 이다.
이는 입력과 알고리즘의 선형 관계에서 세부적인 다른 사항을 제외하면 선형 시간 알고리즘에
초점을 맞추는데 도움이 된다

`2n + 8` 단계를 가지고 있다면 이것은 어떤 종류의 알고리즘일까?
이 역시 선형시간 알고리즘이다

`n` 이 충분히 커지면 선형 항(`2n`) 이 상수 항(`8`) 을 무시해도 되게 만들기 때문이다
예를 들어, `n` 이 `5000` 이면 `8n` 은 `40000` 이고, `8` 은 `40000` 에 비해 너무 작기 때문에
무시해도 된다

많은 파이썬 작업들은 작업을 수행하는데 고정 시간이 걸린다
예를 들어, 리스트에 값 추가, 딕셔너리에 값 추가, 시퀀스 또는 딕셔너리의 인덱싱은 모두 고정시간이 걸린다

반면, 일부 파이썬 작업은 작업을 수행하는데 선형시간이 걸린다
이들은 고정 시간이 아닌 선형시간으로 계산하도록 주의해야 한다

예를 들어, 파이썬 입력 함수를 사용하여 긴 문자열을 읽는 것은 선형시간이 걸린다
입력 라인의 각 문자를 읽어야 하기 때문이다

이렇게 리스트에서 값을 획득하는 작업은 모두 선형시간이다

```py
string = input()

for char in string:
    print(char)
```

이는 입력한 문자열값을 읽어서 하나의 문자를 출력한다
리스트를 통해 값을 획득한후 출력하므로 선형시간이다

### 이차(제곱) 시간 (Quadratic Time: O(n**2))

고정시간 알고리즘(입력 양이 증가해도 더많은 작업을 수행하지 않는 알고리즘) 과
선형시간 알고리즘(입력 양이 증가함에 따라 선형적으로 더 많은 작업을 수행하는 알고리즘) 에
대해서 논의했다

`O(n ** 2)` 는 입력양이 증가함에 따라 더 많은 작업을 수행한다
`n` 이 `10` 이라면 `10 ** 2` 의 양을 수행하므로, `100` 개의 값을 처리한다

다음을 보자

```py
#   O(N)
for i in range(n):
```

```py
#   O(N**2)
for i in range(n):
    for j in range(n):
```

`n` 개의 값을 입력할때 `n * n` 을 처리하므로, 이를 `O(n**2)` 로 표현한다
만약 입력이 `1000` 이라고 하면 `O(N)` 은 `1000` 번 반복되지만,
`O(N**2)` 는 `1000000` 번 반복된다

이는 시간제한이 있는 테스트케이스 같은경우 좋은 방법이 아니다

### 삼차(세제곱) 시간 (Cubic Time: (O(N**3)))

하나의 루프가 선형 시간으로 이어질 수 있고, 두개의 중첩 루프가 이차 시간으로 이어질수 있는
세개의 중첩 루프는 어떨까?

이는 `Big O` 에서 `O(N**3)` 으로 표기한다

이는 `n` 이 `10` 일때, `O(N**2)` 는 `100`, `O(N**3)` 은 `1000` 이 된다
만약 `n` 이 `1000` 일때는 `1000000000` 번 반복된다

`n` 이 `10000` 이라면, `1000000000000` 번 박복된다
조단위의 반복은 계산시 상당히 느릴수 있다고 유추할수 있다

### 다중변수 (Multiple Varaibles)

```py

"""
브리에 베이커리는 여러 가맹점이 있으며, 각 가맹점은 소비자에게 구운 제품을 판매한다
13년 동안 사업의 이정표에 도달한 프리에 베이커리는 매출에 따라 보너스를 수여하는 행사를 할 것이다
보너스는 일일 매출과 가맹점당 매출에 따라 다르다
보너스 지급 방식은 다음과 같다

- 모든 가맹점의 총 매출이 13의 배수인 날에는 매출을 13으로 나눈 몫으로 보너스가 주어진다
  예를 들어, 전체 가맹점 빵을 26 개 판매한 날에는 26 / 13 = 2 보너스 합계가 추가된다

- 하루의 총 매출이 13의 배수인 모든 가맹점에 대해 13 으로 나눈 몫이 주어진다
  예를 들어 빵 39개를 판매한 가맹점은 39 / 13 = 3 보너스 합계가 주어진다

지급된 보너스의 총계를 구하시오

* 입력

입력은 총 10개의 테스트 케이스로 구성된다
각 테스트 케이스에는 다음과 같은 라인들이 포함된다

- 가맹점의 수 f 와 영업일수 d 가 공백으로 구분된 라인으로, f 는 4 에서 130 사이의 정수이고
  d 는 2 에서 4745 사이의 정수이다
- 한 라인당 영업일 하루의 정보로 구성된 총 d 개 의 라인이다
  각 라인에는 공백으로 구분된 f 개의 정수가 있으며,
  각 정수는 가맹점별 매출을 나타낸다
  d 개의 라인중 첫번째 라인은 첫째 날의 가맹점별 매출을 제공하고, 두 번째 라인은 둘째날의 가맹점 별 매출을
  제공하는 식이다. 각 정수는 1 에서 13000사이의 수이다

* 출력

각 테스트 케이스에 대해 부여된 총 보너스의 수를 출력하라
"""

# 여기서는 N 개의 테스트 케이스 아닌, 하나의테스트 케이스를 기준으로 생각한다
# 샵의 개수와 영업일수를 입력
SHOPS_AND_DAYS = input().split()
# 샵의 개수
NUM_OF_SHOPS = int(SHOPS_AND_DAYS[0])
# 영업일수
NUM_OF_DAYS = int(SHOPS_AND_DAYS[1])
# 샵의 배열
shops = []
# 보너스
bonus = 0

# 영업일수를 기반으로 반복
# shops 배열에 각 영업일수에 따른 매출액을 2차원 배열로 생성
for idx in range(NUM_OF_DAYS):
    # 각 매출액을 입력후 배열화
    revenues = input().split()
    # 입력된 각 매출액을 정수로 변환
    for idx in range(NUM_OF_SHOPS):
        revenues[idx] = int(revenues[idx])
    # 정수로 변환된 매출액 배열을 shops 에 push
    shops.append(revenues)

# 영업일 마다 모든 shop 을 순회
for shop_idx in range(NUM_OF_DAYS):
    # 모든 shop 매출액의 합계
    total = 0
    # shop 의 매출액 순회
    for revenue_idx in range(NUM_OF_SHOPS):
        # 매출액을 합산
        total += shops[shop_idx][revenue_idx]
    # 매출액이 13 으로 나누어 떨어지면 보너스 지급
    if total % 13 == 0:
        bonus += total // 13

# 특정 shop 의 매출액을 순회
for revenue_idx in range(NUM_OF_SHOPS):
    # 합계
    total = 0
    # 영업일별 shop 순회
    for shop_idx in range(NUM_OF_DAYS):
        # shop 인덱스에서, 매출액 인덱스를 순회하여
        # 특정 shop 의 매출액 합계 계산
        total += shops[shop_idx][revenue_idx]
    # 총 합계가 13 으로 나누어떨어지면 보너스 지급
    if (total % 13 == 0):
        bonus += total // 13

print(bonus)
    

```

위는 `for` 문이 여러번번 중첩되므로, `O(N**2)` 라고 볼수 있다

> 가장 외부의 테스트케이스별 반복을 도는 `for` 문은 제외하고 생각한다

여기서 여기서 중요한점은 여기서 말하는 `N` 값은 어떻게 이루어지는지에 대한것이다
이 `N` 은 `shops(d)` 와 `revenue(f)` 의 개수에 따라 반복이 달라지므로, `df` 이다.

서로 연관이 있는 값이며, `for` 문 반복시 하나는 `d(shops)` 를 기준으로 `f(revenue)` 를
반복하고, 다른 반복문은 `f(revenue)` 를 기준으로 `d(shops)` 를 반복한다

### 로그시간 (Log Time)

선형 탐색은 처음부터 끝까지 검색하지만, 이진 탐색은 리스트 중값 값과 비교하면서
검색한다

`512` 개의 값을 가진 리스트에 이진 탐색을 사용해 값을 찾으면,

1. 512 / 2 = 256
2. 256 / 2 = 128
3. 128 / 2 = 64
4. 64 / 2 = 32
5. 32 / 2 = 16
6. 16 / 2 = 8
7. 8 / 2 = 4
8. 4 / 2 = 2
9. 2 / 2 = 1

처럼 `9 단계` 이후로는 `1` 개의 값만 남는다
이는 고정시간이 아니며, 아주 적은 단계를 거쳐 입력 양이 증가함에 따라 단계수도 약간 증가한다

이러한 이진탐색은 `Logarithmic-time` 또는 `Log-time` 알고리즘의 예이다
`Big O` 에서 로그시간 알고리즘은 `O(log n)` 이라고 한다

숫자가 주어지만 이 함수는 `1` 이하가 되기 위해 해당 숫자를 밑 수로 나누어야 하는 횟수를 알려준다
컴퓨터 과학에서는 일반적으로 밑 수는 `2` 이므로, `1` 이하가 되기 위해 숫자를 `2` 로 나누어야
하는 횟수를 구하게 된다

이는 `x = log n` 으로 표현된다
`log` 는 컴퓨터 프로그래밍에서 일반적으로 사용하는 로그는 이진로그이다
`log n` 의 `n` 은 `512` 가 되고, `x` 는 `512` 를 `2` 로 몇번 나누어 `1` 보다 작은값이 되는 값이다

`x = 9` 가 되므로, 총 `9` 번의 연산이 이루어진다
예를 들어, `log 1000000` 이라면 `x = 19.9315..` 인데, 올림하여 `x = 20` 인것을 볼수 있다

`1000000` 처리하는데 `20` 번의 반복만으로 처리가 되는것이다
선형시간을 로그시간으로 변경하는것만으로도, 큰 성능향상을 볼 수 있다

### n log n 시간

정렬 알고리즘 중 가장 유명한 세가지 알고리즘이 있다

`Bubble sort`, `Selection sort`, `Insertion sort` 이다
이는 `O(N**2)` 이 걸리는 알고리즘이다

이는 상당히 느릴수 있다. 반면 `quick sort` 와 `merge sort` 라는 두가지 유명한
알고리즘이 있다

이는 `O(n log n)` 만큼의 시간이 걸리는 알고리즘이다
이는 `1000` 개의 처리 라고 한다면, `1000 log 1000` 만큼 반복한다

`log 10000 = 14` 로 가정하고, `14 * 10000 = 140000` 이다  
`O(N**2) = 100000000` 와는 많은 차이가 난다

리스트 정렬시 파이썬에서 사용하는 정렬 알고리즘은 `O(n log n)` 이다
