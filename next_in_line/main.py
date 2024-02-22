"""
세 아이와 함께 사는 가족을 알고있다
세아이의 나이는 수열을 형성한다

첫째 아이와 둘째 아이의 나이차이는 둘째 아이와 막내 아이의 나이차이와 같다
예를 들어 인접한 두쌍의 차이가 5년이므로, 이들의 나이는 5세, 10세, 15세가 된다

막내아이와 둘째 아이의 나이가 주어질때, 첫째 아이는 몇살인가?

- 입력

2 개의 정수를 입력받는다, 
첫번째 줄은 막내아이의 나이(0 <= Y <= 50) 이며,
두번째 줄은 둘째 아이의 나이(Y <= M <= 50) 이다.

- 출력

첫째아이의 나이를 출력

- 1 example input

12
15

- 1 example output

18

- 2 example input

10
10

- 2 example output

10

"""

while True:
  m = None
  y = int(input("\n막내아이의 나이를 입력해주세요(0 - 50): "))

  if y < 0 or y > 50:
    print("\n", "-" * 50)
    print("\n막내 아이의 나이는 0 부터 50까지 입력해주세요: ")
    continue;

  while True:
    m = int(input(f"\n둘째아이의 나이를 입력해주세요 ({y} - 50): "))

    if m < y or m > 50:
      print("\n", "-" * 50)
      print("\n둘째 아이의 나이는", y, "부터 50까지 입력해주세요: ")
      continue;
    else:
      break
  
  # 막내아이(y)와 둘째아이(m)의 나이차를 가져온후
  # 나이차에 둘째아이 나이값을 더한다
  oldestAge = (m - y) + m

  print(f"첫째아이의 나이는 {oldestAge} 입니다.")
  break;