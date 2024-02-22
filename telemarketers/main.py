"""
텔레마케터의 전화번호는 네자리이며, 다음의 3가지 조건을 충족해야 한다

1. 첫번째 숫자는 8 또는 9
2. 네번째 숫자는 8 또는 9
3. 두번째 세번째 숫자는 동일

예) 네자리 숫자가 8119 인 전화번호는 텔레마케터의 번호이다
전화번호가 텔레마케터의 번호인지 확인하고 전화를 받을지 안받을지 결정한다

- 입력
한 라인의 숫자 하나씩 총 네게의 숫자를 제공하는 4줄의 입력
숫자는 0 부터 9 이다

- 출력
전화번호가 텔레마케터 번호이면 'ignore' 
그렇지 않으면 'answer'
"""

# 번호입력
PHONE_NUMBER = input()

# 번호의 숫자가 9 인지 8 인지 확인하는 함수
def is_eight_or_nine(number):
  if number == '8' or number == '9':
    return True
  else:
    return False

# 두 인자값이 같은지 확인하는 함수
def is_equal(first_arg, second_arg):
  if first_arg == second_arg:
    return True
  else:
    return False

# 전화번호의 첫숫자와 마지막 숫자가 8 또는 9 이고, 가운데 2 숫자가 같다면 'ignore'
if (is_eight_or_nine(PHONE_NUMBER[0]) and
    is_eight_or_nine(PHONE_NUMBER[3]) and
    is_equal(PHONE_NUMBER[1], PHONE_NUMBER[2])):
  print('ignore')
# 그렇지 않다면 'answer'
else:
  print('answer')

