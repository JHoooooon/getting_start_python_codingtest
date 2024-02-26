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

for _i in range(10):
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
    
