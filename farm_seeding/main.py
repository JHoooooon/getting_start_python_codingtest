"""
* 문제

농부인 존에게 n 개의 목초지가 있다
존은 목초지 전체에 씨를 뿌리고 싶어 한다

목초지는 1,2, ..., n 으로 숫자가 매겨져 있다
그리고 존은 4가지 종류의 풀의 씨를 가지고 있는데, 씨는 각각 1, 2, 3, 4로 번호가 매겨져 있다
각 목초지 마다 한가지 유형의 씨를 선택해 뿌릴것이다

또한 존은 m 마리의 소를 키우고 있다
소는 각자 좋아하는 두개의 목초지가 있는데, 자신이 가장 좋아하는 두 목초지에만 관심이 있고
다른 목초지에는 관심이 없다

소의 건강한 식단을 위해 각 소가 좋아하는 두 목초지에는 서로 다른 종류의 풀이 있어야 한다
예를 들면, 어떤 소가 좋아하는 목초지 중 하나에 풀 유형 1 이 있고, 다른 하나는 풀 유형 4가 있으면
괜찮지만, 두 목초지 모두에 풀 유형 1이 있으면 안된다

어떤 목초지를 1마리 이상의 소가 좋아할 수 있지만, 그 목초지를 좋아하는 소의 수는
최대 3마리이다

다시말해, 각 목초지마다 해당 목초지를 좋아하는 소는 3마리 이하이다

각 목초지에서 사용할 풀 유형을 결정하라.
풀 유형 1 ~ 4 를 사용해야 하며, 각 소가 좋아하는 두 목초지에 심은 풀 유형은 달라야 한다

* 입력

revegetate.in 이라는 파일에서 입력을 읽는다
입력은 다음 라인으로 구성된다

- 목초지의 수 n 과 소의 수 m 을 포함하는 라인이다
  n 은 2와 100 사이의 정수이며, m 은 1 과 150 사이의 정수이다
  n 과 m 은 공백으로 구분된다

- 한마리당 한마리의 소가 좋아하는 두 목초지 번호로 구성된 총 m 개의 라인이다
  목초지 번호는 1 과 n 사이의 정수이며 공백으로 구분된다

* 출력

revegetate.out 파일에 출력을 쓴다

* 테스트 케이스

8 6
5 4
2 4
3 5
4 1
2 1
5 2

* 작성할 코드 정리

    - 풀의 유형은 4가지
    - 목초지의 수는 n
    -- 모든소가 한번에 목초지를 이용할수 있어야 한다
    - 소의 수는 m
    -- 소당 2개의 목초지
        --- 각 목초지는 다른 유형의 풀
    -- 각목초지마다 해당하는 목초지를 좋아하는 소의 최대 수는 3
    - 결과: 목초지에 심을 풀의 유형을 결정
    - 테스트 케이스를 보면 한가지 규칙적인 패턴이 만들어진다
    1. 소가 좋아하는 목초지가 3개 일때: 목초지를 2개 만들어야 한다
    2. 3개가 아닐때: 목초지는 1개 만들어야 한다
    3. 목초지에 맞는 풀 유형을 정해야 한다
    
    1 부터 5 까지 같은 풀타입이 안되는 리스트를 만들어본다

    5 4 
    2 4 
    3 5
    4 1 
    2 1
    5 2

    각 목초지의 갯수에 맞는 리스트를 구성한다
    각 idx 는 목초지에 같은 풀타입이 안되는 리스트를 만든것이다
    그리고 각 원소의 첫번째 인덱스는 풀타입을 지정한다
    아직 풀 타입이 지정되지 않아서 0 이다

    cows = [[5, 4], [2, 4], [3, 5], [4, 1], [2, 1], [5, 2]]
    rangelands = [0, 0, 0, 0, 0, 0, 0, 0]
    seeds = [1, 2, 3, 4]

    0 번 목초지를 seeds[0] 으로 한다

    rangelands = [1, 0, 0, 0, 0, 0, 0, 0]

    rangelands[1] 에 관심있는 cows 는 cows[1], cows[4], cows[5] 이다 
    이중 cows[4] 는 2, 1 번 목초지에 관심있다
    그러므로, seeds[0] 은 아니므로, rangelands[1] 은 가장 작은 seed 인 seeds[1] 로 한다

    rangelands = [1, 2, 0, 0, 0, 0, 0, 0]

    rangelands[2] 에 관심있는 cows 는 cows[2] 이다
    cows[2] 는 3, 5 목초지에 관심이 있다. 5 는 아직 어떠한 목초지도 할당되지 않았다
    3 목초지에 관심있는 소는 오직 cows[2] 뿐이므로 가장 작은 seeds[0] 을 준다

    rangelands = [1, 2, 1, 0, 0, 0, 0, 0]

    rangelands[3] 에 관심있는 cows 는 cows[0], cows[1], cows[3] 이다
    cows[1] 과 cows[2] 는 1번과 2번 목초지에 관심이 있다
    그러므로, rangelands[3] 은 seeds[0], seeds[1] 은 아니다
    rangelands[3] 에 seeds[2] 를 할당한다

    rangelands = [1, 2, 1, 3, 0, 0, 0, 0]

    rangelaneds[4] 에 관심있는 cows 는 cows[0], cows[2], cows[4] 이다
    cows[0], cows[2], cows[4] 는 4, 2, 3 번 목초지에 관심이 있다. 그러므로 seeds[0], seeds[2] 는 아니다
    현재 남은 seeds 는 seeds[3] 이므로, seeds[3] 을 할당한다

    rangelands = [1, 2, 1, 3, 4, 0, 0, 0]
    
    나머지 목초지는 좋아하는 cows 가 없으므로, 1 을 할당한다

    rangelands = [1, 2, 1, 3, 4, 1, 1, 1]

    이러한 로직으로 구성된다

- 위의 패턴들
    패턴을 보면 다음과 같다

    1. 선택된 rangeland 보다 작은 rangeland 중 선택된 seed 가 있다면
    해당 seed + 1 한 seed 를 가진다

    2. 선택된 rangeland 가 해당 cow 만 이용되며,
        이전 rangeland 와 겹치지 않는다면, seed 는 1 이다

- 규칙 패턴을 보았으니 이 패턴대로 만들어본다

-- 변수 정의
+ INPUT_FILE_PATH 상수
+ OUTPUT_FILE_PATH 상수
+ 풀 유형 리스트 -> seeds = [1, 2, 3, 4]
+ 목초지의 수 -> rangeland_count
+ 소의 수 -> cow_count
+ 목초지 배열 -> rangelands
+ 소 배열 -> cows

-- 함수 정의
1. out_file 이 있다면 삭제 -> remove_exists_file
2. 목초지 수와 소의 수를 생성 -> get_count
3. 소 배열 생성 -> get_cows
4. rangelands 배열 생성 -> get_rangelands
4. rangelands 의 각 목초지를 순회
4. 해당하는 목초지를 좋아하는 소 검색 -> find_cows
5. 해당하는 여러 목초지가 있는 소들인지 확인 -> set_seeds
        1. 있다면, 해당 목초지를 제외한 가장 작은 목초지를 가져온후,
            가장 최근에 할당된 목초지의 seed + 1 한값을 가장 작은 목초지에 할당
        2. 할당된 목초지가 없으며, 해당 cow 만 사용하는 목초지가 있을경우
            cow 만 사용하는 목초지에 seed[0] 을 할당
6. 처리된 목초지를 output_file 에 할당 -> write_file
7. 처리완료된 output_file 을 읽고 출력 -> print_output_file

"""

import os;

INPUT_FILE_PATH = 'revegetate.in'
OUTPUT_FILE_PATH = 'revegetate.out'
SEEDS = [1, 2, 3, 4]

def remove_exists_file(file_path: str) -> None:
    """
    해당하는 파일이 존재하면 삭제하는 함수

    :param file_path: 파일의 경로
    :return: None
    """
    if os.path.isfile(file_path):
        os.remove(file_path)

def get_count(file_path: str, type: str) -> int:
    """
    file_path 의 첫번째 줄에서 목초지 개수, 소의 개수를 가져오는 함수
    :param file_path: 파일 경로
    :param type: 'cow' | 'rangeland'
    """
    count = 0
    with open(file_path) as f:
        # 첫번째 라인을 배열화
        lis = f.readline().rstrip().split()
        if (type == 'rangeland'):
            count = int(lis[0])
        elif (type == 'cow'):
            count = int(lis[1])

    return count

def get_cows(file_path) -> list:
    """
    주어진 file_path 에서
    모든 소들을 담은 배열을 반환하는 함수

    :param file_path: 파일경로
    :return: list
    """
    result = []
    with open(file_path) as f:
        lines = f.readlines()[1:]
        for line in lines:
            line_list = line.rstrip().split()
            lis = []

            for item in line_list: 
                lis.append(int(item))

            result.append(lis)

    return result

def get_rangelands(rangeland_count: int) -> list:
    """
    목초지의 배열을 반환
    -> 목초지의 배열은 첫번째 원소를 제외한 나머지는 0 으로 초기화
    -> 첫번째 원소는 SEEDS[0] 의 값으로 지정

    :param rangeland_count: 목초지의 개수
    :return: 목초지의 배열
    """
    global SEEDS

    rangelands = []
    for _i in range(rangeland_count):
        rangelands.append(0)
    
    rangelands[0] = SEEDS[0]

    return rangelands

def find_cow(cows: list[list], idx: int) -> list:
    """
    해당하는 목초지의 소들을 찾는 함수
    찾는 인덱스의 목초지는 포함하지 않는다

    :param idx: 해당 목초지에 해당하는 인덱스
    :return: 소의 리스트
    """

    # 반환할 배열
    result = []

    # 파일에서 입력된 목초지의 값은 1부터 시작하므로
    # 인덱스에 1을 더한다
    rangeland_idx = idx + 1

    for cow in cows:
        if rangeland_idx in cow:
            lis = [item for item in cow if item != rangeland_idx]
            result.append(lis[0])

    return result

def set_seed(rangelands: list, idx: int, found_cows: list) -> list:
    """
    seed 유형을 설정하는 함수

    :param rangelands: 목초지 배열
    :param idx: 목초지의 해당 인덱스
    :param found_cows: find_cow 의 반환 배열
    :result: rangeland
    """ 

    global SEEDS;

    # rangelands 배열
    rangelands = rangelands[:]

    # found_cows 의 길이
    cows = found_cows[:]

    # rangeland_idx 가 전혀없는 cows 인지 식별
    # True 라면 이미 앞에 있는 목초지가 중복됨을 알려주며,
    # False 라면 앞의 목초지와 중복되지 않음을 나타낸다
    # 그러므로, 앞의 목초지의 가장 작은 SEED 값을 준다
    is_rangeland_idx = False

    target_idx = 0

    # rangeland 의 idx 값은 0 부터 시작하므로
    # 순회를 위해 idx + 1 한 값을 순회한다
    #
    # 여기서 i 값은 현재 seed 가 할당된 rangeland의 index 이다
    for i in range(idx + 1):
        # 파일상에 입력된 수는 1 부터 시작하므로,
        # 1 을 더해준다
        # 이는 목초지 인덱스값이 된다
        rangeland_idx = i + 1
        # found_cows 안에 rangeland_idx 가 있는지 확인
        if rangeland_idx in cows:
            if rangeland_idx > target_idx:
                target_idx = rangeland_idx 
            # is_rangeland_idx 가 존재하므로 True 로 설정
            is_rangeland_idx = True

    # 만약 rangeland_idx 가 있다면,
    if is_rangeland_idx:
        rangelands[idx] = SEEDS[rangelands[target_idx - 1]]
    # 그렇지 않다면 가장 작은 SEED 값을 준다 
    else:
        rangelands[idx] = SEEDS[0]

    # 만들어진 배열을 반환
    return rangelands;

rangeland_count = get_count(INPUT_FILE_PATH, 'rangeland')
cows = get_cows(INPUT_FILE_PATH)
rangelands = get_rangelands(rangeland_count)
idx = 0

while(idx < rangeland_count):
    found_cows = find_cow(cows, idx)
    rangelands = set_seed(rangelands, idx, found_cows)
    idx += 1

print("".join(str( item ) for item in rangelands))
