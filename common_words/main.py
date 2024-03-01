"""
* 도전과제

m 개의 단어가 주어집니다. 주어진 단어는 고유한 단어가 아닐수도 있다
예를 들어, brook 이 라는 단어가 여러번 나타날 수도 있다

그리고 정수 k 도 주어진다
출현빈도가 k 번째로 높은 단어를 찾는 것이다

만약 w 라는 단어보다 출현 빈도가 높은 단어가 k - 1 개 있다면,
w 는 k 번째로 높은 단어이다

데이터 세트에 따라 k 번째로 높은 빈도를 가진 단어가 존재하지 않거나,
하나 있거나, 여러개 있을 수 있다

k 번째로 가장 많이 사용된 단어(빈도가 높은 단어) 의 정의를 확실히 이해해야 한다
k = 1 이면 자신보다 더 빈도가 많은 단어가 없으므로, 가장 자주 발생하는 단어를 묻는것이 된다
k = 2 이면 자신보다 빈도가 높은 단어가 1개인 단어, k = 3 이면 빈도가 높은 단어가 2개인 단어를
묻는것이다

* 입력

입력은 '테스트 케이스의 수를 제공하는 라인' 과 '테스트 케이스의 값들이 담긴 라인들' 로 구성된다
각 테스트 케이스는 다음의 라인들로 구성된다

-   케이스에 있는 단어의 수 m 과 찾고자 하는 출현 빈도 순위 k 를 포함하는 라인,
    m 은 0 ~ 10000 사이의 정수이고, k 는 최솟값이 1 인 정수이다.
    m 과 k 는 공백으로 구분된다

-   각 라인마다 한 단어를 제공하는 총 m 개의 라인이다
    한 단어는 최대 20자로 구성되며, 모든 문자는 소문자이다

* 출력

각 테스트 케이스에 대해 다음 라인을 출력하세요

-   다음과 같이 'p' 번째로 빈도가 높은 단어라는 정보를 포함하는 라인이다

    "p most common word(s)"

    여기서 p 는 k 가 1 이면 1번째, k 가 2이면 2번째, k 가 3 이면 3번째, k 가 4 이면 4번째라는
    식으로 빈도 순위를 뜻한다

-   k 번째로 빈도가 높은 단어를 포함한 라인으로, 한줄에 한 단어씩 출력한다
    만일 k 번째 빈도가 높은 단어가 없을 경우 출력이 없다

-   빈 라인이다

* 날 혼란스럽게 하는 문장

- 이게 번역체라서 이해를 못한건지, 문제자체가 이런건지 애매하다...
- 원 문장을 보기는 했는데, 비슷하게 해석되서 더 혼란스러웠다...

1.   만약 w 라는 단어보다 출현 빈도가 높은 단어가 k - 1 개 있다면,
    w 는 k 번째로 높은 단어이다

2.  자신보다 더 높은 단어

-   위의 2 문장때문에 꽤나 헤맸다.
    처음에 의도하는바가 잘 이해가 안된것이다
    여기서 말하는는 다음과 같다

    1. 출현 빈도 k 보다 높은 단어
        -   k 출현 빈도 보다 높은 빈도를 가진 단어
    2. 출현 빈도가 높은 단어가 k - 1 개 있다면, w 는 k 번째로 높은 단어이다
        -   k 출현 빈도 보다 높은 단어가 k - 1 개 이어야만
            w 는 k 번째로 높은 단어이다

            이말은, w 라는 단어가 총 3 번 나온다면
            w 단어보다 출현빈도가 높은 단어의 개수는 k - 1 개이어야만
            인정된다는 말이다.

    결론:
        인정되는 단어는
        k 의 출현빈도를 가지며, k 보다 출현빈도가 많은 단어의 수가 k - 1 이어야
        한다.

* 정리

-   한 라인에 공백을 기준으로 m 과 k 을 받는다

-   단어
        - m 은 단어의 수 (1 ~ 10000)
        - 한 단어는 최대 20자
        - 단어는 모두 소문자

-   출현빈도
        - k 는 출현 빈도 순위 (최솟값 1인 정수)
        - k = 1: 가장 빈도가 높은 단어
        - k = 2: 2 번째로 빈도가 높은 단어
        - k = 3: 3 번째로 빈도가 높은 단어

-   출력의 마지막은 빈라인이 포함되어야 한다    

* 코드 정리

1.  반복되는 테스트케이스의 개수 --> get_repeat_count
2.  단어의 개수와 출현빈도 순위를 받는다 --> get_count
3.  단어의 개수 만큼의 배열을 생성한다 --> get_words
4.  단어의 배열을 순회하며, 각 단어의 출현빈도를 나타내는 객체를 생성한다 --> get_common_words
5.  출현빈도를 key 로 하고 단어의 배열을 값으로 갖는 객체로 변경한다 --> get_reverse_common_words
5.  각 단어의 출현빈도 객체를 순회하여 출현빈도가 k 와 같으며, 해당하는
    단어보다 출현빈도가 더 높은 단어의 수가 k - 1 이라면
    해당 단어의 배열을 반환한다 --> get_kth_frequent_words
7.  1st, 2nd, 3rd, 그외는 th 처럼 kth 마다 서수 접미사를 생성한다 --> get_ordinal_suffix
6.  k 번째의 단어를 가진 배열을 순회하여 출력한다 --> print_kth_frequent_words

"""
def get_repeat_count():
    """
    인풋으로 부터 테스트 케이스의 개수를 반환하는 함수

    Retrun (int):
        테스트 케이스의 개수
    """

    return int(input())


def get_count() -> list[int]:
    """
    단어의 출현빈도 혹은 단어의 개수를 리턴하는 함수

    Return:
        단어의 출현빈도 와 단어의 개수를 가진 배열
        [0]: 단어의 개수
        [1]: 출현빈도
    """
    line = input().split()
    counts = []

    for item in line:
        counts.append(int(item))

    return counts


def get_words(word_count: int) -> list[str]:
    """
    단어의 인풋을 받아 배열을 생성하는 함수

    Params:
        word_count (int): 인풋으로 받을 단어의 개수
    Return:
        단어의 리스트
    """
    words: list[str] = []

    for _i in range(word_count):
        word = input()
        words.append(word)

    return words

def get_common_words(words: list[str]) -> dict:
    """
    리스트 원소를 key 로, 원소의 출현빈도를 value 로 가진 dict 를 반환하는 함수

    Params:
        words (list[str]): 단어를 가진 배열
    Return:
        단어의 출현빈도를 가진 딕셔너리
    """
    common_words = {}

    for word in words:
        if word in common_words:
            common_words[word] = common_words[word] + 1
        else:
            common_words[word] = 1

    return common_words

def get_reverse_frequent_word(common_words: dict) -> dict:
    """
    만들어진 common_words 의 value 를 key 로 하고
    해당 value 의 list 를 value 값으로 하는 함수

    Parmas:
        common_words (dict): value 를 key 로하며, key 값의 배열을 생성할 dict
    Returns (dict):
        결과 dict 
    """

    result_dict = {}

    for key, value in common_words.items():
        if (value in result_dict):
            result_dict[value].append(key)
        else:
            result_dict[value] = [key]

    return result_dict

def get_kth_frequent_word(k: int, common_words: dict) -> list[str]:
    """
    k 번째로 빈도가 높은 단어의 리스트를 반환하는 함수

    Params:
        k (int): 출현빈도 순위
        common_words: 단어의 출현빈도를 가진 딕셔너리
    Return:
        k 번째 출현빈도를 가진 단어리스트 
    """

    kth_frequent_dict = get_reverse_frequent_word(common_words) 
    kth_frequent_list = sorted(list(kth_frequent_dict.keys()), reverse=True)
    kth_frequent_len = len(kth_frequent_list)
    idx = 0
    total = 0

    """
    규칙은 
    
    k 번째 출현빈도를 가지며 k 이전의 단어는 k - 1 의 개수를 가져야함
    k = 출현빈도
    total = k - 1
    """

    while(idx < k):
        if total == k - 1:
            break
        else:
            if kth_frequent_len > idx:
                total += len(kth_frequent_dict[kth_frequent_list[idx]])
            idx += 1

    if (k == 1):
        return kth_frequent_dict[kth_frequent_list[0]]
    elif (total == k - 1):
        return kth_frequent_dict[kth_frequent_list[idx]]
    else:
        return []

def get_ordinal_suffix(kth_count: int) -> str:
    """
    서수 접미사를 생성하는 함수

    Params:
        kth_count (int): kth 숫자
    Return:
        kth 마다 반환할 서수 접미사
    """

    kth_str = str(kth_count)

    if kth_str[-1] == '1' and kth_str[-2:] != '11':
        return kth_str + 'st'
    elif kth_str[-1] == '2' and kth_str[-2:] != '12':
        return kth_str + 'nd'
    elif kth_str[-1] == '3' and kth_str[-2:] != '13':
        return kth_str + 'rd'
    else:
        return kth_str + 'th'

def print_kth_frequent_words(kth_count: int, kth_frequent_words: list[str]) -> None:
    """
    결과를 출력하는 함수

    Params:
        kth_count (int): 단어 출현빈도 순위
        kth_frequent_words (list[srt]): k 번째 출현빈도를 가진 단어 리스트
    Return (None):
        리턴은 없으며, 내용을 출력한다
    """

    kth = get_ordinal_suffix(kth_count);

    print(f"{kth} most common word(s):")
    for word in kth_frequent_words:
        print(word)
    print()

# 테스트 케이스를 반복할 개수
repeat_count = get_repeat_count()

# 테스트 케이스 실행
for i in range(repeat_count):
    counts = get_count()
    word_count = counts[0]
    kth_count = counts[1]
    words = get_words(word_count)
    common_words = get_common_words(words)
    kth_frequent_words = get_kth_frequent_word(kth_count, common_words)
    print_kth_frequent_words(kth_count, kth_frequent_words)
