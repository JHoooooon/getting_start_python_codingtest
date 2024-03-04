"""
농부인 존의 농장에는 n 개의 언덕이 있고,    
각 언덕의 높이는 0 ~ 100 사이이다.

존은 자신의 농장을 스키 훈련 캠프로 등록하려고 한다

가장 높은 언덕과 가장 낮은 언덕의 높이 차이가 17 이하인 경우에만 스키장으로
등록할 수 있다

따라서 존은 일부 언덕의 높이를 줄이거나 줄여야 할수도 있다
그는 정수만큼만 높이를 변경할 수 있다

높이를 x 만큼 변경하는 비용은 x ** 2 이다.
언덕을 높이 1 에서 높이 4 로 변경하는 비용은 (4 - 1) ** 2 이다

존이 농장을 스키 훈련 캠프로 등록할 수 있도록 언덕의 높이를 변경하는 데
지불해야 하는 최소 금액을 결정하라

* 입력

skidesign.in 이라는 파일에서 입력을 읽어온다
입력은 다음 같은 라인들로 구성된다

-   농장에 있는 언덕 개수 n 을 포함한 라인 (1 ~ 1000)
-   한 라인당 한 언덕의 높이를 나타내는 총 n 개의 라인 (0 ~ 100)

* 출력

skidesign.out 이라는 파일에 출력을 쓴다
농부 존이 언덕의 높이를 변경하기 위해 지불해야 하는 최소 금액
각 테스트 케이스 수행의 제한시간은 4초

* 정리

-   가장 높은 언덕과 가장 낮은 언덕의 높이 차는 17 이하
-   높이를 x 만큼 변경하는데 드는 비용은 x ** 2
-   언덕의 높이를 변경하기 위해 지불해야 하는 최소금액을 구하라

* 풀이

-   파일에서 언덕의 개수 n 을 가져온다
-   파일에서 언덕의 높이 배열을 가져온다
-   각 언덕을 순회하며 낮은 언덕 기준이 되어, 나머지 언덕들과의 차를 구함   
    -   가장 낮은 언덕보다 작으면 23 에서 빼고,
        가장 큰 언덕보다 크면 40 에서 뺀다
    -   가장 낮은 언덕 23 
        -   23 + 17 = 40 (23 ~ 40)
            -   23 - 16 = abs(7)
            -   23 - 2 = abs(21)
            -   =   7 ** 2 + 21 ** 2 = 490
    -   가장 낮은 언덕 40 
        -   40 + 17 = 57 (40 ~ 57)
            -   40 - 23 = abs(17)
            -   40 - 16 = abs(24)
            -   40 - 2 = abs(38)
            -   =   17 ** 2 + 24 ** 2 + 38 ** 2 = 2309
    -   가장 낮은 언덕 16 
        -   16 + 17 = 33 (16 ~ 33)
            -   33 - 40 = abs(7)
            -   16 - 2 = abs(14)
            -   =   7 ** 2 + 14 ** 2 = 245
    -   가장 낮은 언덕 2 
        -   2 + 17 = 19 (2 ~ 19)
            -   19 - 23 = abs(4)
            -   19 - 40 = abs(21)
            -   =   4 ** 2 + 21 ** 2 = 545
    -   결과
        -   245

* 정리
    -   파일을 읽고, 언덕의 개수를 가져온다

    -   파일을 읽고, 언덕의 배열을 생성한다
        -   각 언덕의 높이는 해당 언덕이 가장 낮은 언덕임을 가정한다
        -   각 언덕의 최소 높이와 최대 높이를 계산하여 dict 으로 담은 배열

    -   언덕의 배열을 순회하며, 각 언덕이 가장 낮은 언덕일때 나오는 금액을 계산한다
        -   가장 낮은 언덕 + 17 = 가장 큰 언덕
        -   비교할 언덕이 가장 낮은 언덕보다 작으면 가장 낮은 언덕에서 빼기(절대값)
        -   비교할 언덕이 가장 큰 언덕보다 크면 가장 큰 언덕에서 빼기(절대값)
        -   각 순회된 언덕의 금액중 가장 낮은 금액을 반환한다

    -   가장 낮은 금액을 쓴다
"""

from typing import Dict

INPUT_FILE = 'skidesign.in'
OUTPUT_FILE = 'skidesign.out'

def get_hills_count(file: str) -> int:
    """
    파일을 읽어 언덕의 수를 반환하는 함수

    Params:
        file (str): 파일경로
    Retrun (int):
        언덕의 개수
    """
    hills_count = 0
    with open(file) as f:
        hills_count = int(f.readline())

    return hills_count

def write_minimum_amount(file: str, minimum_amount: int) -> None:
    """
    최소금액을 쓰는 함수

    Params:
        file (str): 파일경로
    Retrun (None):
        없음
    """
    with open(file, 'w') as f:
        f.write(str(minimum_amount))

def get_hills_hight(file: str) -> list[Dict[str, int]]:
    """
    언덕의 높이를 가져오는 배열

    Params:
        file (str): 파일경로
    Retrun (list[Dict[str, int]]):
        언덕의 높이의 최소 높이와 최대 높이를 가진 dict 을 가진 배열
    """

    hills = []

    with open(file) as f:
        lines = f.readlines()
        lines_len = len(lines)

        for idx in range(lines_len):
            if idx == 0:
                continue
            hill_hight = int(lines[idx].rstrip())
            hills.append({ 'low': hill_hight, 'high': hill_hight + 17})

    return hills;

def get_minimum_amount(hills: list[Dict[str, int]], hills_count: int) -> int:
    """
    언덕의 높이를 변경하려할때, 요구 되는 가장 최소 금액을 반환하는 함수

    Params:
        hills (list[Dict[str, int]]): 각 언덕의 최소, 최대 높이를 가진 배열
        hills_count (int): 언덕의 개수
    Retrun (int):
        언덕 높이 변경시 드는 최소 금액
    """
    min = None

    #   hills 를 순회
    for idx in range(hills_count):
        #   해당 언덕의 높이 변경시 드는 토탈 금액
        total = 0
        #   해당 언덕의 최소 높이
        low = hills[idx]['low']
        #   해당 언덕의 최대 높이
        high = hills[idx]['high']

        #   비교할 언덕의 배열  
        comparison_hill = hills[:idx] + hills[idx + 1:]

        #   비교할 언덕의 배열을 순회
        for hill in comparison_hill:
            #   비교할 언덕의 높이
            hill_hight = hill['low']
            #   비교할 언덕 높이 변경시 드는 금액
            amount = 0

            #   비교할 언덕의 높이가 최소 높이보다 보다 작으면
            if hill_hight < low:
                amount = (low - hill_hight) ** 2
            #   비교할 언덕의 높이가 최대 높이보다 크면
            elif hill_hight > high:
                amount = (hill_hight - high) ** 2
            #   이 둘중 아무것도 해당하지 않으면 최소 높이에서 최대 높이내의 언덕
            #   비용이 들지 않는다
            else:
                amount = 0

            #   토탈 금액을 합산
            total += amount

        #   토탈 금액이 산정한 최소 금액보자 작으면
        if min == None or min > total:
            min = total

    return min
            

hills_count = get_hills_count(INPUT_FILE)
hills = get_hills_hight(INPUT_FILE)
min_amount = get_minimum_amount(hills, hills_count)
write_minimum_amount(OUTPUT_FILE, min_amount)

"""
현재 책에 나온 솔루션이 혼란스럽다.
왜 0 ~ 100 까지의 각 언덕을 주어진 언덕과 비교하지?

지금 아무리 내용을 훑어봐도, 문제상 입력의 조건은 다음과 같다

-   농장에 있는 언덕 개수 n 을 포함한 라인 (1 ~ 1000)
-   한 라인당 한 언덕의 높이를 나타내는 총 n 개의 라인 (0 ~ 100)

한 라인당 한 언덕의 높이를 나타낸다
만약 한 라인당 언덕의 개수를 나타내는거라면 솔루션의 풀이가 맞다.

여기 문제제시 에서는 "한 라인당 한 언덕의 높이" 이다.
주어진 4개의 언덕을 사용해서 최소 비용을 만들 수 있는 금액을
반환하면 된다.

이 솔루션은 내용이 이상하다.
책이 잘못된것 같다는 생각이 든다.

내용을 아무리 몇번씩 읽어봐도 왜 1 ~ MAX_HEIGHT 까지의 모든 언덕의
최소 높이 언덕, 최대 높이 언덕을 비교하고 가져오는지 이해가 안간다.

만약, 

"문제 내용이 1 ~ 100 까지의 언덕이 있으며, 주어진 언덕과의 높이차가 17 이하
이어야 한다."

라고 하면, 솔루션 풀이가 맞다.
문제에서는 다음처럼 이야기한다

"농부인 존의 농장에는 n 개의 언덕이 있고,
각 언덕의 높이는 0 ~ 100 사이이다."

"각 언덕" 이라고 정확히 명시되어 있다
번역과정의 실수인지 모르겠지만, 솔루션 자체가 말이 안된다.
"""