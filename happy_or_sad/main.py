"""
종종 이모티콘을 사용하여 감정을 표현한다
:-) 이 연속적인 문자는 `행복한 얼굴` 을 나타내며, :-( 는 `슬픈 얼굴` 을 나타낸다
메시지의 전반적인 분위기를 결정하는 프로그램을 작성하라

- 입력

1 에서 255 문자를 포함하는 하나의 문자열 입력

- 출력

1. 입력라인에 행복하거나 슬픈 이모티콘이 포함되어 있지 않으면 `none` 출력
2. 입력라인에 동일한 수의 행복한 이모티콘과 슬픈 이모티콘이 포함되어 있으면 `unsure` 출력
3. 입력라인에 행복한 이모티콘이 더 많으면 `happy` 출력
4. 입력라인에 슬픈 이모티콘이 더 많으면 `sad` 출력

"""

EMOTICON = input()
SAD_COUNT = EMOTICON.count(':-(')
HAPPY_COUNT = EMOTICON.count(':-)')

if (SAD_COUNT == 0 and HAPPY_COUNT == 0):
  print('none')
elif (SAD_COUNT > HAPPY_COUNT):
  print('sad')  
elif (SAD_COUNT < HAPPY_COUNT):
  print('happy')  
else:
  print('unsure')