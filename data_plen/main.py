"""
페로는 한달에 데이터를 x MB 제공하는 휴대전화 공급자의 데이터 요금제를 사용
하고 있다. 특정 달에 사용하지 않은 데이터는 다음달로 이월된다.

예를 들어 x 가 10 이고, 페로가 어떤 달에 4 MB 만 사용했다면, 나머지 6 MB 는 그다음달로 이월된다
다음달에 10 + 6 = 16MB 사용가능한것이다.

페로가 처음 n 개월 동안 사용한 데이터량이 메가바이트 단위로 주어진다.
다음달에 페로가 사용할 수 있는 데이터량을 계산하라

* 입력

입력은 다음과 같은 라인들로 구성된다

- 페로에게 매월 주어지는 데이터량 x 를 포함한 라인으로, x 는 1 - 100 사이의 정수이다
- 페로가 데이터 요금제를 사용한 개월수 n 을 포함한 라인으로, n 은 1 - 100 사이의 정수이다
- 데이터 요금제 사용기간 동안 페로가 사용한 데이터량을 월별로 한줄씩 제공하는 총 n 개의 라인이다
  각 숫자는 최소 0 이며, 사용가능한 메가바이트 수(x)를 초과하지 않는다.

* 출력

다음달에 사용할 수 있는 메가바이트 수를 출력
"""

# 매월 주어지는 데이터량
x = int(input())

# 데이터 요금제를 사용한 개월수
n = int(input())

# 현재 month
current_month = 0

# 사용가능한 총 메가바이트수
total_data = x

# 사용한 개월수 마다 사용한 데이터 량을 월별로 입력
while(current_month < n):
  # 해당 달에 사용한 data 량
  d = int(input())

  # 첫달 데이터이고 첫달 데이터량보다 해당 월에 사용한 데이터가 크다면,
  if (total_data < d):
    print(f"{d} 는 매월 제공되는 데이터량 {total_data} 보다 큽니다. 다시 입력해주세요.")
    continue;

  # total_data 와 남은 데이터량을 더하여 이월
  total_data = total_data - d + x
  # month 값 증가
  current_month+= 1

# 사용가능한 데이터량 출력
print(total_data)

"""
다른 풀이

# total_data 에 매월 제공되는 데이터와 요금제를 사용한 개월수 + 1 한값을
# 곱하면, 총 data 수가 나온다
total_data = x * (n + 1)

# 총 데이터에서 각 개월마다 사용한 데이터량을 빼면
# 당월에 사용가능한 데이터 총합이 나온다
for _i in range(n):
  d = int(input())
  total_data -= n;

# 당월 사용 데이터 총합
print(total_data)
"""