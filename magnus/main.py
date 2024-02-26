"""
Magnus 는 Kile 에게 체스 게임을 졌으며, 그는 경쟁으로 부터 벗어나 편안함을 되찾았다 
곧 그는 COCI 대회에 대해 듣고 그곳에서 자신의 실력을 시험해 보기로 결정한다

그는 Kile 에게 다음과 같은 메일을 보낸다
"COCI 를 준비해주세요."

Kile 은 다음과 같이 대답한다
"COCI 에 참여하고 싶나요? 좋아요! 준비작업은 다음과 같아요
하위 단어 HONI(COCI 의 크로아티아어 약어) 를 구성하는 4개의 연속되는 문자를 HONI 블록이라고 불러요
N 개길이의 단어를 사용하여, 그 단어에 가능한 한 많은 HONI 블록의 개수를 찾으세요"

- 입력

첫번째 줄에는 영어 알파벳 대문자로 구성된 N(1 - 100,000) 길이의 단어가 포함된다

- 출력

HONI 블럭의 개수를 출력하라
H, O, N, I 글자를 Magnus 는 하나의 HONI 블록을 포함하는 단어를 얻을수 있다

# 약간 번역하는 과정에서 약간 애매한 부분이 있는데 이는 HONI 의 문자중 연속되는 문자는 하나의 문자로 취급한다는 이야기다
# 반면, 연속되지 않지만 HONI 문자열로 구성된다면, 하나의 HONI 문자열로 취급한다
# 모든 경우의수에서 HONI 가 만들어져야 한다
# 중간에 다른 상관없는 문자열은 무시한다

Sample Input 1
MAGNUS

Sampel Output 1
0

Sample Input 2
HHHHOOOONNNNIIII

Sampel Output 2
1

Sample Input 3
PROHODNIHODNIK

Sampel Output 3
2
"""

# 문자열을 받는다
word = input()

# HONI_BLOCK 의 카운트
count = 0

# start 인덱스
startIdx = 0

# user_input 의 길이
input_len = len(word)
found = False

# HONI 문자열의 총 개수 반환
# print(total_count)

