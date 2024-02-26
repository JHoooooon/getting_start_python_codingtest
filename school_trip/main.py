"""
학생들은 학년 말에 수학여행을 가고 싶지만, 그러기 위해서는 비용을 지불해야 한다
수학 여행에 드는 돈을 모으기 위해 브런치 프로그램을 준비한다

브런치에 참가하려면 1학년은 $12, 2학년은 $10, 3학년은 $7, 4학년은 $5 를 내야 한다
브런치를 통해 모인 돈 중 50% 는 수학여행 비용으로 사용할 수 있다
(나머지 50% 는 브런치 비용으로 사용된다)

수학여행 비용, 연간 학생 비율, 총 학생 수를 알 수 있다
학생들이 돈을 더 모아야 하는지 판단하라

- 소수점 내림으로인해 누락되는 학생수는 가장 많은 학생을 가진 학년에 누락된 학생수를 더하라

* 입력

입력은 총 3줄로 된 테스트케이스 10(총 30줄)로 구성된다
다음은 각 테스트 케이스에 대한 설명이다

- 첫번째 라인에는 수학여행 비용($)이 포함되어 있다
  비용은 50 ~ 50000 사이의 정수이다

- 두번째 라인에는 1학년부터 4학년까지의 학년별 브런치 참여 학생 비율을
  나타내는 숫자 4개가 포함되며, 이는 공백으로 구분된다. 각 숫자는 0 과 1 사이의 부동 소수점이고 합계는 1(100%) 이다

- 세번째 라인은 브런치에 참석하는 학생 수 n 을 포함한다. n 은 4 ~ 2000 사이의 정수이다

* 출력

각 테스트 케이스에 대해 학생들이 수학여행을 위해 돈을 더 마련해야 한다면 YES 를 출력
아니면 NO 를 출력
"""

# 반복할 개수
idx = 10
# 학년별 내야할 비용 리스트
GRADE_AMOUNTS = [12, 10, 7, 5]

# 학년별 참여 인원 리스트 반환 함수
# lis: 학년별 참여 비율 리스트
# total: 총 참여 인원
def get_participation_list(lis: list, total: int): 
    # 반환할 리스트 
    result = []
    # lis 에서 rate 값을 받아 순환
    for rate in lis:
        # rate * total 값을 곱하여 학년별 인원수를 push
        result.append(int(float(rate) * total))

    # 소수점 내림으로 인해 생긴 누락된 학생
    uncounded = total - sum(result)

    # 가장큰 학생수를 가져온후
    most = max(result)

    # 해당 학생수를 가진 학년의 인덱스를 찾음
    idx = result.index(most)

    # 해당 인덱스의 학년수와 uncounded 학년수를 더한다
    result[idx] += uncounded

    # 리스트 반환
    return result

# 학년별 모인 수학여행 금액
# lis: 학년별 참여 인원 리스트
def get_education_traval_amount(lis: list):
    # 학년별 비용 리스트 참조
    global GRADE_AMOUNTS

    # 모인 전체 비용
    total_amount = 0

    # lis 에서 학년인원 수를 순회하여 전체 비용계산  
    for idx in range(len(lis)):
        # total_amount + 학년의 총인원수 * 학년이 내야할 branch 비용 = total_amount
        total_amount = total_amount + lis[idx] * GRADE_AMOUNTS[idx]

    # 모인 모든 금액의 반은 수학여행 금액으로 사용
    return total_amount / 2

# 총 3개의 테스트 케이스
for _i in range(idx):
    # 수학여행 비용
    education_traval_amount = int(input())
    # 학년별 참여 비율
    participation_rate_list = input().split()
    # 총 학생 참여 인원
    n = int(input())

    # 참여 인원 리스트
    participation_list = get_participation_list(participation_rate_list, n)
    # 모인금액에서 수학여행에 쓸 비용
    amount = get_education_traval_amount(participation_list)
    # 출력
    print('NO' if amount > education_traval_amount else 'YES')