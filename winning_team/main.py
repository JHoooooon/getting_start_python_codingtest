"""
농구에서는 점수를 얻는 방법은 총 3가지로, 3점 슛과 2점 슛, 1점 자유투가 있다
사과 팀과 바나나팀의 농구 경기를 보면서 각 팀의 3점, 2점, 1점 성공 횟수를 기록했다
사과팀이 이겼는지, 바나나팀이 이겼는지, 두팀이 비겼는지 표시하라

- 입력

앞의 세 라인은 사과팀에 대한 점수이며, 뒤의 세 라인은 바나나팀의 점수이다

첫째라인 사과팀의 3점슛 성공횟수
둘째라인 사과팀의 2점슛 성공횟수
셋째라인 사과팀의 1점슛 성공횟수
넷째라인 바나나팀의 3점슛 성공횟수
다섯째라인 바나나팀의 2점슛 성공횟수
여섯째라인 바나나팀의 1점 자유투 성공횟수

각 숫자는 0 에서 100 사이이다

- 출력

출력은 문자 한개이다.

사과팀이 이길경우 A
바나나팀이 이길경우 B
동점인 경우 T

"""
# 사과팀 3점슛
A_THREE_POINT = int(input()) * 3
# 사과팀 2점슛
A_TWO_POINT = int(input()) * 2
# 사과팀 자유투
A_FT = int(input())

# 바나나팀 3점슛
B_THREE_POINT = int(input()) * 3
# 바나나팀 2점슛
B_TWO_POINT = int(input()) * 2
# 바나나팀 자유투
B_FT = int(input())

# 사과팀 총 점수
A_TOTAL_POINT = A_THREE_POINT + A_TWO_POINT + A_FT
# 바나나팀 총 점수
B_TOTAL_POINT = B_THREE_POINT + B_TWO_POINT + A_FT

# 사과팀이 바나나팀보다 점수가 클때
if A_THREE_POINT > B_TOTAL_POINT:
  print('A')
# 사과팀이 바나나팀보다 점수가 작을때
elif A_THREE_POINT < B_TOTAL_POINT:
  print('B')
# 그외의 상황(동점일때)
else:
  print('T')

