"""
이 이야기는 골디락스와 세 마리의 곰에 대한 이야기이다.
각 곰은 자신이 좋아하는 의자에서 죽을 한그릇씩 먹는다
처음에 말하지 않았던 것은 골디락스가 테이블 위의 그릇을 이리저리 움직였다는 것이다
그래서 그릇은 원래있던 자리에 있지 않는다

그릇은 무게에 따라 분류할수 있으며, 가장 가벼운 그릇은 아기 곰의 그릇,
중간 그릇은 엄마곰의 그릇, 가장 물거운 그릇은 아빠 곰의 그릇이다

세가지 무게를 읽고 엄마 곰 그릇의 무게를 출력하는 프로그램을 작성하라
모든 가중치는 100 보다 작은 정수라고 가정한다
"""

firstBowl = int(input())
secondBowl = int(input())
thirdBowl = int(input())

if (firstBowl > secondBowl):
  if (secondBowl > thirdBowl):
    print(secondBowl)
  elif(firstBowl > thirdBowl):
    print(thirdBowl)
  else:
    print(firstBowl)
elif (firstBowl > thirdBowl):
  print(firstBowl)
elif (secondBowl > thirdBowl):
  print(thirdBowl)
else:
  print(secondBowl)

