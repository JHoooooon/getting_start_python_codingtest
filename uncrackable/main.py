"""
매우 재미있는 웹사이트에 계정을 등록하고 싶다

이미 username 이 선택되었지만, 패스워드 요구사항이 꽤나 엄격해 보인다.
이 패스워드는 반드시 8 - 12자 길이의 문자열이어야 하며, 모든 문자는 a - z, A - Z, 0 - 9 이다.

여기에서 해당 문자는 다음과 같은 규칙을 가진다

- 소문자는 최소 3개 이상이어야 한다
- 대문자는 최소 2개 이상이어야 한다
- 숫자는 최소 1개 이상이어야 한다
- 입력시 최대 100 자로 구성된 비어있지 않은 문자열로 구성되어야 한다

사이트에서 비밀번호를 입력하고 거부당할 위험을 감수하기 보다는 비밀번호가
모든 규칙을 유효하게 충족하는지 여부를 스스로 판단하고 싶을 것이다

* 입력

첫번째 라인은 하나의 문자열을 담는다 이는 패스워드를 의미한다

* 출력

만약 패스워드가 유효하다면 `Valid` 를, 그렇지 않다면 `Invalid` 를 출력한다

"""
# user_pass 를 입력받음
user_pass = input()

# 소문자 카운트
lower_count = 0
# 대문자 카운트
upper_count = 0
# 숫자 카운트
num_count = 0
# 문자 숫자
char_count = len(user_pass)

# 소문자인지 확인하는 함수
def is_lower(char):
  code = ord(char)
  if code >= 97 and code <= 122:
    return True
  else:
    return False

# 대문자인지 확인하는 함수
def is_upper(char):
  code = ord(char)
  if code >= 65 and code <= 90:
    return True
  else:
    return False

# 숫자인지 확인하는 함수
def is_number(char):
  code = ord(char)
  if code >= 48 and code <= 57:
    return True
  else:
    return False

# char_count 가 12 보다 크거나 8 보다 작으면 invalid
if ((char_count <= 12 and char_count >= 8)):
  for idx in range(char_count):
    if (is_lower(user_pass[idx])):
      lower_count += 1
    elif (is_upper(user_pass[idx])):
      upper_count += 1
    elif (is_number(user_pass[idx])):
      num_count += 1
    
    """
    char = user_pass[idx]
    if (char.islower()):
      lower_count += 1
    elif (char.isupper()):
      upper_count += 1
    elif (char.isdigit):
      num_count += 1
    """

  if (lower_count < 3 or upper_count < 2 or num_count < 1):
    print('Invalid')
  else:
    print('Valid')
else:
  print('Invalid')