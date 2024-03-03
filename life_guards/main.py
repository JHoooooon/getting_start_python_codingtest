"""
* 도전과제

농부인 존은 자기 소들을 위해 수영장을 구입했다
수영장은 시간 0 부터 1000 까지 운영된다

존은 수영장을 감시할 인명 구조원을 고용한다
각 인명구조원은 지정된 시간 동안 수엉장을 감시한다

예를 들어, 인명구조원은 시간 2에 일을 시작하여 시간 7 에 일을 마친다
여기서는 이런 시간 간격을 2 ~ 7 처럼 표시한다

간격에 해당하는 시간 단위 수는 종료 시각에서 시작 시각을 뺀 값이다.
예를 들어, 시간 간격이 2 ~ 7 인 인명구조원은 7 - 2 = 5시간을 근무한다

이 간격은 2 ~ 3, 3 ~ 4, 4 ~ 5, 5 ~ 6, 6 ~ 7 이라는 5개의 단위 시간으로 구성된다
안타깝게도 농부 존은 n 명이 아니라 n - 1 명만 고용할수 있을 만큼의 돈을
가지고 있기 때문에 인명구조원 한명을 해고해야 한다

인명 구조원 한명을 해고 한후 감당할 수 있는 시간 단위 수를 결정하라

* 입력

lifeguards.in 이라는 파일에서 입력을 읽는다
입력은 다음의 라인들로 구성된다

-   고용된 인명구조원의 수 n 이 포함된 라인으로, n 은 1 ~ 100 사이의 정수
-   한 라인당 인명 구조원 한명의 정보로 구성된 총 n 개의 라인
    각 라인은 인명구조원의 근무 시작 시간, 공백, 근무 종료 시간을 표시한다
    시작 및 종료 시각은 0 ~ 1000 사이의 모든 정수이며, 시작과 종료가 동일한
    근무 시간은 존재하지 않는다

* 출력

lifeguards.out 이라는 파일에 출력을 쓴다
n - 1명의 인명구조원으로 감당할 수 있는 최대 시간 단위 수를 출력하라
각 테스트 케이스를 수행하는데 지정된 제한 시간은 4 초이다.

* 정리

-   수영장 운영시간은 0 ~ 1000 시간

-   인명구조원
    -   시간범위: 0 ~ 1000 시간
    -   시작시간
    -   종료시간
    -   시작, 종료가 동일한 근무 시간은 없다

-   최대 시간 단위
    -   확실히 번역체라 애매하게 설명된다.
    -   시간 간격이 가장짧은 직원만 해고하면 될것 같았다.

    -   여기서 혼란스러웠던점은, 시간 간격이다.
        여기서 말한 최대 시간 단위는, 각 직원이 최대한 연달아서 근무가능한
        최대 시간 간격을 말하는거다.


* 풀이

-   직원의 수를 파일에서 읽어온다

-   파일을 읽어, 각 직원의 시간 간격을 가진 배열을 만든다

-   각 직원을 순회하며, 해당 직원을 제외한 나머지 직원의 시간간격 
    set 을 만든후 lenght 값을 반환한다.
    -   여기서 length 값은 시간 간격이다

-   각 직원을 순회하며 만들어진 시간간격 길이를 비교하여,
    가장 큰 시간간격을 반환한다

-   가장 큰 시간간격을 파일에 출력한다

"""
from typing import Dict

INPUT_FILE = 'lifeguards.in'
OUTPUT_FILE = 'lifeguards.out'

def get_employees_count(file: str) -> int:
    """
    직원의 수를 반환하는 함수

    Params:
        file (str): 파일경로

    Return (int):
        직원의 수
    """
    employees_count = 0
    with open(file) as f:
        employees_count = int(f.readline())

    return employees_count

def write_file(file: str, covered_time: int) -> None:
    """
    출력파일에 시간간격의 합을 쓰는 함수

    Parmas:
        file (str): 파일경로
        total_time_rate (int): 시간간격의 합산 결과
    Return (None):
        반환값 없음
    """
    with open(file, 'w') as f:
        f.write(str(covered_time))

def get_employees(file: str) -> list[int]:
    """
    각 직원들의 시간간격을 가진 배열을 반환하는 함수

    Params:
        file (str): 파일경로
    Return (list[int]):
        직원들의 시간 간격을 가진 배열
    """
    employees = []
    with open(file) as f:
        lines = f.readlines()

        for idx in range(len(lines)):
            if idx == 0:
                continue;
            employee = lines[idx].split()
            start_time = int(employee[0])
            end_time = int(employee[1])

            employees.append({'start_time': start_time, 'end_time': end_time})

    return employees


def get_time_interval(ignore_idx: int, employees: list[Dict[str, int]]) -> int:
    """
    시간 간격의 길이를 반환하는 함수

    Params:
        ignore_idx (int): 제외될 employees 인덱스 
        employees (list[Dict[str, int]]): 직원들 배열

    Return (int):
        시간 간격의 길이
    """
    time_interval = set()
    employees_len = len(employees)

    for idx in range(employees_len):
        if idx == ignore_idx:
            continue
        for time in range(employees[idx]['start_time'], employees[idx]['end_time']):
            time_interval.add(time)

    return len(time_interval)

def get_covered_time(employees_count: int, employees: list[Dict[str, int]]) -> int:
    """
    감당할수 있는 최대 시간단위 수를 계산하는 함수

    Params:
        employees_count (int): 직원의 수
        employees (list[Dict[str, int]]): 직원의 배열

    Return (int):
        최대 시간 단위 수
    """
    covered_time = 0

    for idx in range(employees_count):
        time_interval_len = get_time_interval(idx, employees)

        if covered_time < time_interval_len:
            covered_time = time_interval_len
        
    return covered_time

employees_count = get_employees_count(INPUT_FILE)
employees = get_employees(INPUT_FILE)
covered_time = get_covered_time(employees_count, employees);
write_file(OUTPUT_FILE, covered_time)