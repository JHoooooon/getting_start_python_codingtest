"""
루카는 수업 시간에 비밀분장을 쓰고 있습니다
선생님이 그것을 읽을수 없도록 원래의 문장을 쓰는 대신 인코딩을 해서 작성합니다

문장의 각 모음 (a, e, i, o, u) 뒤에 문자 p 와 해당 모음을 다시 추가합니다
예를 들면, I like you 라는 문자를 쓰는대신 ipi lipikepe yopoupu 라고 씁니다

선생님이 루카가 인코딩한 문장을 습득했습니다. 선생님을 도와 루카의 원문을 알아내세요

* 입력
입력은 루카의 규칙으로 인코딘된 한 줄의 텍스트입니다
문자열은 소문자와 공백으로 구성되며, 각 단어사이에 정확히 하나의 공백이 있습니다
한 문자의 최대 길이는 100자 입니다

* 출력
루카가 보내려 했는 원문을 출력합니다
"""

word = input()
result = ""
idx = 0

while(idx < len(word)):
    result += word[idx]
    if (word[idx].lower() in ['a', 'e', 'i', 'o', 'u']):
        idx += 3
    else:
        idx += 1

print(result)