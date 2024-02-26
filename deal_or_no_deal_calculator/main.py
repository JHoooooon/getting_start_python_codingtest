"""

Deal or No Deal 은 NBC 의 게임 쇼이다.

게임의 CCC 버전에서는 10개의 선택이 가능하다
$100, $500, $1000, $5000, $10000, $25000, $50000, $1000000, $500000, $1000000 가 상상의 서류가방에 봉인되어 있다 

이러한 금액은 (1 - 10) 으로 번호가 지정된다.
예를 들어 (1 ~ $100), (2 ~ $500), (3 ~ $1000), ..., (10 ~ $1000000) 으로 되어 있다

게임이 시작되기 전에 참가자는 서류가방중 하나를 자신의 것으로 선택하여
보관하게 된다

게임중에 참가자가 다른 서류가방중 하나를 선택하고 내부 금액을 공개했기 때문에 가능한 10가지중 
하나가 게임에서 제거되었다

어느 시점에서 참가자는 서류 가방 열기를 중단하고, 'banker' 는 선택하지 않은 서류 가방과 공개된
금액에 따라 참가자에게 거레 제안을 한다

그런 다음 참가자에게 '거래' 또는 '거래없음'(Deal or No Deal?) 이라는 질문을 받는다

남은 금액(즉, 자신의 서류가방을 포함하여 개봉하지 않은 모든 서류가방) 의 평균을 계산하고 비교하여
플레이어가 '거래' 또는 '거래없음'(Deal or No Deal?) 을 선택해야 하는지 결정하는데 도움이 되는 
프로그램을 작성하라

그 가치를 'banker' 의 제안에 적용한다.
제안이 평균보다 높으면, 플레이어는 'deal' 해야 한다, 그렇지 않으면 'no deal' 을 말해야 한다

* 입력

열린 케이스 수를 나타내는 n 을 입력받으며, 그 뒤에 뱅커의 제안된 금액이 입력된다
n 은 1 ~ 10 사이의 정수목록이다.

이는 제거된 것을 나타내며, 맨 뒤에는 `banker` 의 제안이 따른다
예를 들어,
3 2 5 10 300 은 $500, $1000, $1000000 가 들어있는 서류 가방이 제거되었으며,
banker 의 제안이 $300 임을 나타낸다

제거된 서류 가방 값에 대해 중복된 번호가 입력되지 않았다고 가정할 수 있으며
'banker' 제안이 10 보다 큰 정수라고 가정한다

* 출력

deal 또는 no deal 을 출력한다
"""

# 서류가방의 목록
brifcases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
# 현재 남은 서류가방의 목록
delete_brifcase_idx = []
# 총 입력 개수
n = int(input())

# 평균값을 구하는 함수
def get_avg(lis: list):
    global delete_brifcase_idx

    # 제공된 리스트를 복사
    target = lis[:]

    # delete_brifcases_idx 의 index 를 가져와
    # target 에서 해당하는 값 삭제
    for idx in delete_brifcase_idx:
        target.remove(lis[idx - 1])

    # 모든 값을 더할 변수
    sum = 0
    # target 에서 값을 가져와 모든 값을 더한다
    for val in target:
        sum += val
    # 더한후 taget 의 길이값으로 나누고 소수점 값을 버리기 위해
    # int 로 캐스팅 한다
    return sum / len(target)

# offer 의 마지막 값이 banker 의 제안된 금액으로 하기 위해
# range(n + 1) 한 값을 순회
for _i in range(n + 1):
    # offer 입력
    offer = int(input())
    # offer 가 10 보다 작거나 같거나
    # offer 가 delete_brifcase_idx 안에 존재하지 않은 값이라면
    # delete_brifsase_idx 에 push 
    if (offer <= 10 and offer not in delete_brifcase_idx):
            delete_brifcase_idx.append(offer)

# 평균값 저장
avg = get_avg(brifcases)

# 만약 banker 가 제공한 금액(offer)이 평균값 보다 크면,
# deal 아니면, no deal
print('deal' if offer > avg else 'no deal');