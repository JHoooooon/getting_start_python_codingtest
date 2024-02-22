"""
n 개의 주차공간이 있는 주차장을 관린한다  
각 주차 공간의 점유여부를 기록하고 있다. 어제와 오늘 양일 모두 점유된 주차 공간의 수를 표시하라

* 입력

총 3줄이며 각 라인은 다음과 같다

- 첫번째 라인에는 주차 공간의 수 n 이 있다. n 은 1 - 100 사이의 정수이다
- 두번째 라인에는 어제의 주차 정보가 포함된다. 
  여기에는 주차 공간별로 한 문자씩 총 n개의 문자로 이루어진 문자열이 있다
  'C' 는 주차 공간에 차기 있음을 나태나고, '.' 은 빈것을 나타낸다.
  'CC.' 는 처음 두개의 주차 공간은 점유되고 있고 세번째는 비어있을을 의미한다
- 세번째 라인에는 두번째 라인과 동일한 형식으로 오늘의 주차 정보가 포함된다

* 출력

어제 오늘 양일 모두 점유된 주차 공간의 수를 출력하라
"""

# 주차공간의 수
spaces_nums = int(input())

# 어제 주차된 공간 정보
yesterday_occupied_spaces_info = input()

# 오늘 주차된 공간 정보
today_occupied_spaces_info = input()

# 현재 주차 공간 위치
current_location = 0

# 어제 오늘 주차된 공간의 총수
total = 0

# 주차되었는지 확인하는 함수
def is_occupied(space):
  # space 가 C 이면 True
  if (space == 'C'):
    return True
  # 아니면 False
  else:
    return False

while(current_location < spaces_nums):
  if (is_occupied(yesterday_occupied_spaces_info[current_location]) and
    is_occupied(today_occupied_spaces_info[current_location])):
    total += 1

  current_location += 1

# 어제 오늘 주차된 공간의 수
print(f"{ total }")