"""
*   문제
전체길이가 n 피트이고 각 부분(피트)이 특정 색상으로 된 스카프가 있다
스카프 모양으로는 총 m 개의 사양이 있다

각 사양은 스카프의 시작 부분과 마지막 부분의 색상을 지정하여 원하는 스카프의 모양을 나타낸다
목표는 이 사양들 중 하나에 맞는 가장 긴 스카프를 만들수 있게끔 스카프를 자르는 것이다

*   입력

-   스카프 길이가 n 과 사양의 개수 m 을 포함하는 라인
-   n 과 m 은 각각 1 ~ 1000000 사이의 정수이며, 공백으로 구분
-   스카프 시작부터 마지막 부분까지 순서대로 각 부분의 색상을 나타내는 정수 n 개로 구성된 라인
    각 정수는 1 ~ 1000000 사이이며, 공백으로 구분
-   한 라인당 한 스카프 사양의 정보를 포함한 총 m 개의 라인
    각 스카프 사양은 시작 부분 색상과 마지막 부분 색상을 나타내는 정수로 구성
    두 정수는 공백으로 구분

*   출력

-   기존 스카프를 잘라 만들수 있는, 사양에 맞는 스카프의 최대 길이를 출력
    각 테스트 케이스를 수행하는데 지정된 시간은 .4 초

*   정리

-   첫 라인의 n 은 스카프의 총 길이, m 은 주어진 스카프 모양 개수
-   두번째 라인은 주어진 주어진 스카프 모양으로 이루어진 6 피트의 스카프
-   세번째 부터 m 번 라인까지는, 스카프 모양

-   주어진 스카프 모양의 시작부분에서 끝나는 부분까지 알맞는 최대 스카프 길이를
    출력

*   코드 정리

-   스카프 길이와 사양의 개수를 받는다
-   전체 스카프의 배열을 가져온다
-   m개 사양의 배열을 가져온다
-   각 사양의 시작 인덱스와 끝나는 인덱스를 계산하여, 잘라내고 길이값을
    가져온다.
-   가져온 스카프 길이중 가장 큰 값을 출력한다
"""

from typing import Dict 

def get_scarf_spec():
    """
    스카프 길이 및 모양을 반환하는 함수

    Retrun (Dict(str, str)):
        스카프 길이 및 모양을 가진 디셔너리
    """
    line = input()
    str_scarf_spec = line.rstrip().split()

    scarf_spec = {}

    # 첫번째 라인은 총 2개로 상수 = O(1)
    for idx in range(len(str_scarf_spec)):
        if (idx == 0):
            scarf_spec['len'] = int(str_scarf_spec[idx])
        elif (idx == 1):
            scarf_spec['shape'] = int(str_scarf_spec[idx])

    return scarf_spec;

def get_scarf():
    """
    스카프를 가져오는 함수

    Return (list(int)):
        스카프를 배열로 가져오는 함수
    """

    line = input()

    str_scarf = line.rstrip().split()
    scarf = []

    #   O(N) 스카프의 길이에 따라 값이 달라진다
    for item in str_scarf:
        shape = int(item)
        scarf.append(shape)

    return scarf

def get_mostidx(scarf: list[int], scarf_len: int):
    """
    scarf 모양의 가장왼쪽 인덱스와 가장오른쪽 인덱스를 반환

    Args:
        scarf (list[int]):
            스카프 모양의 리스트
        scarf_len (int):
            스카프의 개수

    Return (list[Dict[str, int]]):
        스카프 모양을 가진 배열
    """

    leftmost_idx = {}
    rightmost_idx = {}

    for idx in range(scarf_len):
        color = scarf[idx]

        if not color in leftmost_idx:
            leftmost_idx[color] = idx
            rightmost_idx[color] = idx
        else:
            rightmost_idx[color] = idx
    
    return [leftmost_idx, rightmost_idx]

def get_longest_scarf(shape_len: int, mostidx: list[Dict[str, int]]):
    """
    모양에 맞는 최대 스카프 길이를 출력

    Args:
        scarf (list[int]): 모양을 배열로 가진 스카프
        shpaes (list[list[int]]): 모양의 배열

    Return (int):
        최대 스카프 길이
    """
    longest_scarf_len = 0
    leftmost_idx = mostidx[0]
    rightmost_idx = mostidx[1]

    for _idx in range(shape_len):
        scarf_shape = input().rstrip().split()
        first = int(scarf_shape[0])
        last = int(scarf_shape[1])

        if first in leftmost_idx and last in leftmost_idx:
            scarf_len = rightmost_idx[last] - leftmost_idx[first] + 1

            if scarf_len > longest_scarf_len:
                longest_scarf_len = scarf_len

    return longest_scarf_len

        

scarf_spec = get_scarf_spec()
scarf = get_scarf()
shapes = get_mostidx(scarf, scarf_spec['len'])
longest_scarf_len = get_longest_scarf(scarf_spec['shape'], shapes);
print(longest_scarf_len)