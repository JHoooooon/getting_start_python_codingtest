"""
미국의 주(States) 라고 하는 지리적인 지역으로 나뉘어져 있으며,
각 주에는 하나 이상의 도시(Cities) 가 있다

각 주에는 2개의 문자로 지정된 약어가 있다
예를 들어, Pennsylvania 주의 약어는 PA 이고, South Caroline 주의 약어는 SC 이다

도시 이름과 주의 약어는 모두 대문자로 작성한다

SCRANTON PA 와 PARKER SC 라는 한쌍의 문자열을 생각해보자
여기서 각 도시의 처음 두 문자가 상대 도시가 속한 주의 약어를 나타내고
있는 점이 특별하다

SCPANTON 의 처음 두 문자는 SC(PARKER가 속한 주) 이고, PARKER 의 처음 두 문자는
PA(SCRANTON 이 속한주) 이다 

이러한 특징을 충족하면서 같은 주에 있지 않은 도시들의 쌍을 특별한 관계라고 한다
제공되는 입력에서 특별한 관계의 도시 쌍들이 몇개나 되는지 계산하라

* 입력

citystate.in 이라는 파일에서 입력을 읽는다
입력은 다음 라인들로 구성된다

-   도시의 수 n 이 포함된 라인으로, n 은 1 ~ 200000 사이의 정수이다

-   한 라인당 한 도시의 정보로 구성된 n 개의 라인이다
    각 라인은 대문자로 된 도시의 이름, 공백 그리고 대문자로 된 주 약어를 표시한다
    각 도시의 이름은 2 ~ 10 자이며, 주 약어는 정확히 2 자이다.
    어떤 도시 이름이 여러 주에 존재할수는 있지만, 동일한 주에서는 해당 도시 이름이 한번까지만
    나올수 있다.
    이 문제에서 도시 또는 주의 이름은 이러한 요구사항을 충족하는 문자열이며,
    이는 실제 미국의 도시나 주의 명칭이 아닐수 있다

* 출력

-   citystate.out 파일에 출력을 쓴다

-   특별한 도시를 이루는 쌍의 수를 출력하라

-   각 테스트 케이스를 수행하는 데 지정된 제한시간은 4 초이다.

* 정리

-   도시의 이름과 주이름을 공백으로 구분된 문자열
    -   도시 이름은 2 ~ 10
    -   주의 약어는 2자
    -   문자열의 도시 이름의 첫 두 문자는 상대 도시가 속한 주 이름
-   특별한 관계
    -   같은 주에 있지 않은 도시이며, 같은 주에 속하지 않은 도시들의 쌍
    -   도시의 이름이 여러 주에 존재할수 있지만, 동일한 주에는 해당 도시 이름이 하나

* 풀이

1.  citystate.in 파일에서 도시의 개수를 받는다

2.  citystate.in 파일에서 각 도시의 배열을 받는다

3.  도시의 배열에서 주의 key, 관계된 주와, 도시들 배열을 가진 dict 의 value 를 가진 state_city_dict 을 만든다
    -   key 는 주
    -   value 는 관련 주, 도시들을 가진 dict
        -   관련 주는 relation: str
        -   도시들은 cities: list[str]

5.  state_cities_dict 의 주의 key 를 순회한다
    -   각 주에서 해당 주의 cities 의 길이와 relation 주의 cities 의 길이를 곱하여 합친다 
    -   relation 주가 있는지 추가 확인한다
    -   반환값은 total / 2 한 값이며, int 로 캐스팅하여 값을 버린다 

6. citystate.out 에 출력한다
"""
from typing import Dict, List

FILE_PATH = './citystate.in'
OUT_PATH = './citystate.out'

def get_city_count(path: str) -> int:
    """
    도시의 개수를 가져오는 함수

    Params :
        path (str): 파일 경로

    Return (int):
        도시의 개수
    """
    city_count = 0

    with open(path) as f:
        city_count = int(f.readline())

    return city_count

def write_totla_count(path: str, total: int) -> None:
    """
    특별한 관계의 개수를 쓰기 작업하는 함수

    Parmas :
        path (str): 쓰기 파일 경로

        total (int): 특별한 관계의 개수

    Return (None):
        없음
    """

    with open(path, 'w') as f:
        f.write(str(total) + '\n')

def get_cities(path: str) -> list[str]:
    """
    도시의 배열을 반환하는 함수

    Params :
        path (str): 파일 경로
        city_count (int): 도시의 수
    
    Return (list[str]):
        도시를 담은 배열
    """
    cities = []

    with open(path) as f:
        lines = f.readlines()

        for idx in range(len(lines)):
            if idx == 0:
                continue;
            else:
                line = lines[idx].rstrip()
                cities.append(line)

    return cities;

def get_state_city_dict(cities: list[str]) -> Dict[str, Dict[str, List[str]]]:
    """
    state 의 키를 가지며, 해당 state 에 속하는 city 가진 배열을 값으로 가진 dict 를 반환하는 함수

    Params:
        cities (list[str]): 도시들의 배열
    Return (Dict[str, List[Dict[str, str]]]):
        state 의 키를 가지며, 해당 state 에 속하는 city 가진 배열을 값으로 가진 dict
    "
    """

    #   반환할 딕셔너리 
    state_city_dict = {}

    #   각 도시들을 순환
    for state_city in cities:
        #   각 도시들의 공백 문자열을 쪼개서 만든 배열
        splited_state_city = state_city.split()
        #   1 번째 배열은 도시가 속한 주의 이름이다
        state = splited_state_city[1]
        #   0 번쩨 배열은 도시명이다
        relation_and_city = splited_state_city[0]
        #   도시명에서 처음 2 글자는 연관된 주 이름이다
        relation = relation_and_city[0:2]
        #   도시명에서 2 글자를 제외한 나머지 글자는 도시이름이다
        city = relation_and_city[2:]

        # 가지 자신을 참조하는 cities 는 제거
        if state == relation:
            continue;

        #   state_city_dict 에 state 가 있는지 확인 없다면 생성
        if not state_city_dict.get(state):
            state_city_dict[state] = {}

        #  state_city_dict[state] 에 relation 이 있는지 확인 없다면 생성
        if not state_city_dict[state].get('relation'):
            state_city_dict[state]['relation'] = relation

        #   state_city_dict[state] 에 cities 가 있는지 확인 있다면 city 추가
        if state_city_dict[state].get('cities'): 
            state_city_dict[state]['cities'].append(city)
        #   없다면 cities  생성
        else:
            state_city_dict[state]['cities'] = [city]

    # 결과 반환
    return state_city_dict

def get_special_relation_city_count(state_city_dict: Dict[str, List[Dict[str, str]]]) -> int:
    """
    특별한 관계를 갖는 도시의 쌍의 개수를 출력하는 함수

    Params:
        state_city_dict (Dict[str, List[Dict[str, str]]]):
            state 의 키를 가지며, 해당 state 에 속하는 city 가진 배열을 값으로 가진 dict
    Return (int):
        특별한 관계를 가진 쌍의 모든 개수
    """
    #   특별한 관계의 개수
    total = 0
    #   모든 주의 키
    state_keys = state_city_dict.keys()

    #   각 주를 순회
    for state in state_keys:
        #   순회된 key 를 바다 state_city_dict 의 relation_city 배열을 순회
        relation_cities = state_city_dict.get(state)
        #   관계가 맺어진 state
        target_relation_name = relation_cities.get('relation')
        #   관계가 맺어진 state 의 객체
        target_relation = state_city_dict.get(target_relation_name)

        #   target_relation 이 존재한다면
        if target_relation:
            #   현재 state 의 cities 의 길이
            relation_cities_len = len(relation_cities.get('cities'))
            #   관계가 맺어진 state 의 cities 의 길이
            target_relation_cities_len = len(target_relation.get('cities'))

            #   이를 곱해서 total 값을 구함
            #   관계 쌍 이기에 발생할수 있는 쌍의 모든 경우의 수를 구한다
            total += target_relation_cities_len * relation_cities_len

    #   발생한 2 개의 쌍의 모든 경우의 수를 더한 값이므로,
    #   나누기 2 를 하여 쌍의 개수를 구한다
    return int(total / 2)

city_count = get_city_count(FILE_PATH)
cities = get_cities(FILE_PATH)
state_city_dict = get_state_city_dict(cities)
total_count = get_special_relation_city_count(state_city_dict)
write_totla_count(OUT_PATH, total_count)

