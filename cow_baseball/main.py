"""
농부인 존은 n 마리의 소를 가지고 있다
소들은 각각 고유한 정수 위치에 연속으로 서서 즐겁게 야구공을 던진다

존은 이 우스꽝스러운 모습을 지켜보고 있다
그는 소 x 가 오른쪽에 있는 어떤 소 y 에게 공을 던진다음,
소 y 가 오른쪽에 있는 어떤 소 z 에게 공을 던지는것을 봤다

또한 두번째 투구 거리가 적어도 첫번째 투구 거리와 같고,
최대로는 첫번째 투구 거리의 두배라는 것을 알았다

(예를 들어, 첫번째 투구 거리가 5 라면, 두번째 투구거리는 최소 5 ~ 10 이다)

존이 관측치를 만족하는 소(x, y, z) 의 위치를 계산하라

* 입력

입력은 Baseball.in 이라는 파일에서 읽는다

-   소들의 수 n 이 포함된 라인이다
    n 은 3 ~ 1000 사이의 정수이다

-   한 라인당 소 한마리의 위치를 나타내는 총 n 개의 라인이다
    모든 소의 위치는 고유하며, 이는 1 ~ 100000000 사이의 정수이다

* 출력

Baseball.out 이라는 파일에 출력을 쓴다
농부 존의 관찰을 만족하는 소들 각각의 위치를 출력
각 테스트 케이스를 수행하는데 제한시간은 4초이다

"""

from bisect import bisect_left, bisect_right 

INPUT_FILE = 'Baseball.in'
OUTPUT_FILE = 'Baseball.out'

def write_satisfied_cow_num(file: str, satisfied_num: int) -> None:
    """
    만족하는 투구거리를 가진 위치 개수

    Parmas:
        file (str): 파일경로
        satisfied_num (int): 만족하는 투구거리를 가진 수
    """
    with open(file, 'w') as f:
        f.write(str(satisfied_num))


def get_cow_locs(file:str) -> list[int]:
    """
    소의 위치를 반환하는 함수

    Parmas:
        file (str): 파일경로

    Return (list[int]): 소의 위치 배열
    """
    cow_locs = []
    with open(file, 'r') as f:
        lines = f.readlines();
        for idx in range(len(lines)):
            if idx == 0:
                continue
            cow_loc = int(lines[idx])
            cow_locs.append(cow_loc)

    return cow_locs

#   1000 마리의 수를 처리해야 한다.
#   for 문을 3번 중첩하므로, 1000 ** 3 = 1000000000 이 된다
#   이는 4초를 넘길수 있는 연산이 될 수 있다
def get_satisfied_cow_locs(cow_locs: list[int]) -> int:
    """
    소를 기준으로 오른쪽으로 소의 기준 거리 ~ 소의 기준 거리 * 2 의 거리를 만족하는 개수

    Parmas:
        cow_locs (list[int]): 소의 위치 배열

    Return (int): 소의 기준거리 ~ 소의 기준거리 * 2 에 만족하는 소위치 개수
    """
    total = 0

    for cow_loc_x in cow_locs:
        for cow_loc_y in cow_locs:
            #   x 와 y 값의 거리 차를 계산 = 첫번째 투구거리
            difference_loc = cow_loc_y - cow_loc_x 
            #   x, y 의 거리차가 0 보다 크다면
            if difference_loc > 0:
                #   y 의 거리 + x, y 의 거리차 = 최소 투구거리
                low = cow_loc_y + difference_loc
                #   y 의 거리 + x, y 의 거리차 * 2 = 최고 투구거리
                high = cow_loc_y + difference_loc * 2

                #   z 값
                for cow_loc_z in cow_locs:
                    #   두번째 투구거리
                    #   두번째 투구 거리가 최소 투구거리와 최고 투구거리 사이라면
                    if cow_loc_z >= low and cow_loc_z <= high:
                        #   만족하는 투구거리
                        total += 1

    return total;


def get_better_satisfied_cow_locs(cow_locs: list[int]) -> int:
    """
    선형탐색
    아래는 for 문은 2번 중첩하며 필요한 수만큼 while 문을 돌린다
    이렇게 왼쪽에서부터 오른쪽 인덱스를 찾기 위해 스캔하는 방식을 선형탐색이라 한다
    이는 아까보다는 효율적이지만, 아직 효율적인 코드는 아니다

    Args:
        cow_locs (list[int]): 소의 위치 배열

    Returns:
        int: 투구거리에 만족하는 소의 위치 개수
    """
    #   위치를 정렬한다
    sorted_cow_locs = sorted(cow_locs, key=int)
    cow_locs_len = len(cow_locs)

    # total 값
    total = 0

    # location 계산
    for i in range(cow_locs_len):
        #   i + 1 한 값부터 순회
        for j in range(i + 1, cow_locs_len):
            #   j 인덱스 값에서 i 인덱스 값의 차는 첫번째 구간 간격
            difference_loc = sorted_cow_locs[j] - sorted_cow_locs[i]
            #   두번째 소 위치 + 첫번째 구간간격 =  두번째 구간간격의 최소간격
            low = sorted_cow_locs[j] + difference_loc
            #   두번째 소 위치 + 두번째 구간간격 * 2 =  두번째 구간간격의 최고간격
            high = sorted_cow_locs[j] + difference_loc * 2

            #   최소 구간간격에 만족하는 위치값 인덱스
            #   초기값은 j + 1 부터 시작
            left = j + 1

            #   최소 구간간격에 만족하는 위차값 인덱스 - 1 까지 순회
            while left < cow_locs_len and sorted_cow_locs[left] < low:
                left += 1

            #   최소 구간간격에 만족하는 위치값부터 최대 구간간격에 맞족하는 위치값 인덱스
            #   초기값은 left(최소 구간간격에 만족하는 인덱스 - 1) 이다
            right = left

            #   최소 구간간격에서 시작하여, 최대 구간간격까지의 인덱스
            while right < cow_locs_len and sorted_cow_locs[right] <= high:
                right += 1

            #   최대 구간간격 인덱스 - (최소 구간간격 - 1 인덱스) = 만족하는 구간간격 개수
            total = total + right - left

    return total;


def get_bisect_satisfied_cow_locs(cow_locs: list[int]) -> int:
    """
    이진탐색

    어떠한 값이 주어지면, 배열을 반으로 나누어 
    A 집합과 B 집합으로 나눈다
    해당 값이 A 집합의 가장 큰수보다 작으면, A 집합을
    해당 값이 B 집합의 가장 작은수보다 크면, B 집합을 선택한다
    선택된 집합을 다시 나누어 똑같은 로직을 반복하면,
    해당하는 값을 찾을수 있다

    선형탐색처럼 일일히 모든 값을 비교하는 방법이 아니다

    [1, 2, 3, 4, 5, 6] 라는 집합이 주어지고, 5 값을 찾는다고 하자
    선형탐색은 1 ~ 5 까지 검색하므로, 5 - 1 = 4 이다
    총 4번의 순회가 이루어진다

    반면 이진탐색은 다음과 같다
    6 / 2 = 3 이므로, 3 - 1 인덱스 값과 5 값을 비교한다
    인덱스 2 는 3 이므로 5 보다 작다
    그럼 3 인덱스 부터 시작한다
    3 / 2 = int(1) 이므로, 3 + 1 값을 5 값과 비교한다
    인덱스 4 는 5 이므로 5 값이다

    총 2번만에 5 값을 찾는다

    선형탐색은 4번, 이진탐색은 2번이므로, 이진탐색이 훨씬 효율적인것을
    볼수 있다

    Args:
        cow_locs (list[int]): 소의 위치 배열

    Returns:
        int: 투구거리에 만족하는 소의 위치 개수
    """

    #   위치를 정렬한다
    sorted_cow_locs = sorted(cow_locs, key=int)
    cow_locs_len = len(cow_locs)

    # total 값
    total = 0

    # location 계산
    for i in range(cow_locs_len):
        #   i + 1 한 값부터 순회
        for j in range(i + 1, cow_locs_len):
            #   j 인덱스 값에서 i 인덱스 값의 차는 첫번째 구간 간격
            difference_loc = sorted_cow_locs[j] - sorted_cow_locs[i]
            #   두번째 소 위치 + 첫번째 구간간격 =  두번째 구간간격의 최소간격
            low = sorted_cow_locs[j] + difference_loc
            #   두번째 소 위치 + 두번째 구간간격 * 2 =  두번째 구간간격의 최고간격
            high = sorted_cow_locs[j] + difference_loc * 2

            #   이진검색을 통해 low 와 값이 같거나, low 가 없다면 low 보다 큰 첫번째 인덱스를 반환한다
            left = bisect_left(sorted_cow_locs, low)
            #   이진검색을 통해 high 와 값이 같다면, 해당 인덱스 + 1 한 값을, high 값이 없다면 len 값을 반환한다
            right = bisect_right(sorted_cow_locs, high)

            #   right - left = left 값, 중간 값, right 값을 포함하는 개수
            total = total + right - left

    #   모든 값을 합산한 값
    return total


cow_locs = get_cow_locs(INPUT_FILE)
satisfied_cows_num = get_bisect_satisfied_cow_locs(cow_locs);
write_satisfied_cow_num(OUTPUT_FILE, satisfied_cows_num)

