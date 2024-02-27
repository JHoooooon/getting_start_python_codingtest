"""
레나에게는 개봉하지 않은 액션 피규어 상자 n 개가 있다
상자를 열면 액션 피규어의 가치가 떨어지기 때문에 상자를 열 수 없다
따라서 한 상자 안에 있는 액션 피규어의 순서는 변경할 수 없다

또한 상자를 돌리면 액션 피규어가 잘못된 방향을 향하게 될 수 있기 때문에
상자를 회전할 수도 없다

각 액션 피규어는 높이로 지정된다
예를 들어, 어떤 상자 안에 왼쪽에서 오른쪽순으로 높이가 4, 5, 7 인 피규어가 있다
액션 피규어 상자를 이야기할 때, 높이는 항상 왼쪽에서 오른쪽으로 오름차순으로 나열할 것이다

레나는 상자를 정리하려 한다
즉, 액션 피규어의 높이가 왼쪽에서 오른쪽으로 증가하거나 동일하게 유지되도록 상자를
정렬하려는 것이다

그녀가 상자를 정리할 수 있을지 없을지 여부는 상자 내 액션 피규어의 높이에 따라 달라진다
예를 들어, 첫번째 상자 높이가 4, 5, 7 인 액션 피규어가 있고 두번째 상자의 높이가 1 과 2 인
액션피규어가 있을 경우, 두 번째 상자를 먼저 배치하여 이러한 상자들을 정리할 수 있다

그러나 첫번째 상자를 그대로 두고 두번째 상자의 액션 피규어 높이를 6, 8 로 변경하면
이 상자를 정리할 방법이 없다

레나가 상자를 정리할 수 있을지 확인하라

* 입력

입력은 다음의 라인으로 구성된다

- 상자의 수 n 을 포함하는 라인으로, n 은 1 ~ 100 사이의 정수이다
- 상자마다 한 라인씩 총 n 개의 라인이다
  각 라인은 상자 내 액션 피규어의 수를 나타내는 k 로 시작한다
  k 는 1 ~ 100 사이의 정수이다 (k 는 적어도 1 이므로 빈상자에 대해 걱정할 필요가 없다)
  k 다음에는 이 상자 안에 있는 액션 피규어들의 높이를 나타내는 k 개의 정수가 있다
  액션 피규어의 높이는 1 ~ 10000 사이의 정수이며, 한 라인안에 각 정수 사이에는 공백이 존재한다

* 출력

레나가 상자를 정리할 수 있으면 YES 를 아니면 NO 를 출력하라
"""

"""
정리

1. 상자의 수: n    
2. 상자안의 피규어수 및 액션 피규어들의 높이: k [1 ~ 1000] ...
3. 각 상자의 두번째 인자(피규어의 가장 작은 크기) 순으로 정렬 [O]
4. A 상자, B 상자 비교시 A 의 원소값중 가장 큰값 과 B 의 가장 작은 값을 비교
   B 의 가장 작은값이 A 의 가장 큰 원소값 보다 작으면 NO 아니면 YES [O]
"""

# --------------------- 
# 상자의 수
n = int(input())

# --------------------- 
# 박스의 배열
box_list = None

# --------------------- 
# 결과
result = None

# --------------------- 
# 박스가 정상인지 확인하는 함수
def box_ok(box_list: list):
    for box in box_list:
        box = box[1:]
        box_len = len(box)
        for idx in range(box_len - 1):
            if box[idx] <= box[idx + 1]:
                return True
            else:
                return False

# --------------------- 
# set 박스 리스트 함수
def set_box_list():
    # 새로 생성할 박스 리스트
    box_list = []

    # n 번 만큼 순회
    for _i in range(n):
        # figure box 배열 생성
        box = []

        # 입력 받는 box
        input_box = input().split()

        for figure in input_box:
            # 문자를 int 로 캐스팅
            box.append(int(figure))
        
        # int 로 캐스팅된 box 를 박스 리스트에 push
        box_list.append(box)

    # box_list 에서 원소의 두번째 원소를 기준으로 정렬
    # 원소의 두번째 원소는 figure 의 시작높이이다
    return sorted(box_list, key=lambda x:x[1])

# --------------------- 
"""
- 뒤박스와 크기를 비교하는 함수
  현재 박스의 마지막 원소와 이후 뒤따라 오는 박스의 두번째 원소를 비교하여
  현재 박스의 원소가 뒤따라 오는 박스보다 작으면 True
  아니면 False

box_list: 박스 리스트 배열
idx: 현재 박스 리스트 위치

"""
def is_clean(box_list: list, idx: int):
    # 현재 박스의 가장 큰값
    current_box_max = max(box_list[idx][1:])

    # 뒤따라 오는 박스의 가장 작은값
    after_box_min = min(box_list[idx + 1][1:])

    # 현재 박스의 가장 큰값이 뒤따라 오는 박스의 가장 작은 값보다
    # 작으면 NO
    if (current_box_max > after_box_min):
        return 'NO'

    # "NO" 를 반환하지 않았다면, 나머지는 "YES" 이다
    return "YES"

# --------------------- 
# box_list 할당
box_list = set_box_list()

# --------------------- 
# box 에 이상이 있다면 NO
if not box_ok(box_list):
    result = "NO"

# 이상이 없다면,
else:
    # --------------------- 
    # 각 박스를 순환
    for idx in range(n):
        if (idx <= n - 2):
            result = is_clean(box_list, idx)
            if result == "NO":
                break;

print(result);