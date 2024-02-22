"""
2월 18일은 CCC(Canadian Computing Competition) 를 위한 특별한 날이다

사용자에게 숫자로 된 달과 숫자로된 날짜를 요청한다음 해당 날짜가 2월18일 이전, 이후 또는 날짜인지 확인하는
프로그램을 작성하시오

- 2월 18일 이전이면 Before 을 출력
- 2월 18일 이후이면 After 를 출력
- 2월 18일이면 Special 을 출력

- 입력

2개 숫자값을 입력받는다

첫번째는 달을 입력받으며, 1 부터 12 까지 제한한다 
두번째는 날짜를 입력받으며, 1 부터 31 까지 제한한다

- 출력

After, Before, Special 중 하나를 출력
"""

# 달을 입력
MONTH = int(input())
# 날짜를 입력
DAY = int(input())

# 달이 2보다 크거나 날짜가 18보다 크면 After
if MONTH > 2 or DAY > 18:
  print("After")
# 달이 2보다 작거나 날짜가 19보다 크면 Before
elif MONTH < 2 or DAY < 18:
  print("Before")
# 나머지는 전부 Special 이다
else:
  print("Special")