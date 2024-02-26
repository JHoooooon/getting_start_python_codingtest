"""
직선 도로 위에 n 개의 마을이 각기 다르게 위치해 있다
각 마을은 도로에서의 위치를 나타내는 정수로 표시된다

한 마을의 왼쪽 이웃은 그 마을 다음으로 작은 위치에 있는 마을이고,
오른쪽 이웃은 그 마을 다음으로 큰 위치에 있는 마을이다

한 마을의 크기는 그 마을과 왼쪽 이웃 마을 사이에 있는 공간 절반, 그리고 그 마을과 오른쪽 이웃 마을사이에
있는 공간 절반으로 구성된다

예를 들어, 위치 10에 기준이 되는 마을이 잇다고 가정해보자
이때, 그 마을의 왼쪽 이웃이 위치 6에 있고, 오른쪽 이웃이 위치 15에 있다면,
기준 마을의 크기는 위치 8(6 과 10사이의 중간)부터 위치 12.5(10과 15사이의 중간) 사이의 간격이다

맨 왼쪽과 맨 오른쪽 마을에는 이웃이 하나뿐이므로 이웃의 정의가 의미없다
그러므로 이 문제에서 두 마을은 무시한다
마을의 크기는 해당 마을의 경계지점, 즉 가장 오른쪽에서 가장 왼쪽의 위치를 뺀값으로 계산된다

예를 들어 8 에서 12.5 사이의 크기는 12.5 - 8 = 4.5 이다.
가장 작은 마을의 크기를 구하시오

* 입력

입력은 다음의 라인들로 구성된다

- 마을의 수 n 을 포함하는 라인으로, n 은 3 에서 100 사이의 정수이다
- 한줄에 하나씩 각 마을의 위치를 나타내는 총 n 개의 라인이다
  마을의 위치는 -1,000,000,000 에서 1,000,000,000 사이의 정수이며, 각 마을의 위치가
  왼쪽에서 오른쪽 순으로 입력될 필요는 없다.
  마을들은 이 n 개의 라인중 어디에나 있을 수 있다

* 출력

가장 작은 마을의 크기를 출력하라. 소수점 첫째 자리 숫자까지 포함
"""

# 마을의 수
n = int(input())

# 마을을 담을 리스트
vilages = []

# 마을의 크기 리스트
sizes = []

# 마을의 크기계산 함수 
def set_vilage_size(idx: int):
    global n
    global vilages
    global szies 

    if (idx < n - 1 and idx > 0):
        # 왼쪽 마을의 위치값
        left = vilages[idx - 1]
        # 오른쪽 마을의 위치값
        right = vilages[idx + 1]

        # right - left: 오른쪽 마을에서 왼쪽 마을까지의 간격
        # / 2: 해당 간격의 / 2 한 값이 중간마을의 크기
        distinct = (right - left) / 2

        # 중간마을의 크기 push
        sizes.append(distinct);

for _i in range(n):
    vilage = int(input())
    vilages.append(vilage)

# 마을을 오름차 순으로 정렬
vilages.sort(key=int)

# 각 마을을 순회하며, sizes 리스트에 크기를 담는다
for idx in range(n):
    set_vilage_size(idx)

# 가장 작은 값을 출력
print(min(sizes))
