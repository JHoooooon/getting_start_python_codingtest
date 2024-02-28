"""
----------------------------------------------------------------------------------------------------------------------

파일열기

open(file: FileDescriptorOrPath, mode: OpenTextMode = 'r')

'r': 읽기 (default)
     파일을 열지만, 존재하지 않으면 error
'w': 쓰기
     파일의 쓰기 작업을 하지만, 파일이 존재한다면 해당 파일을 삭제하고
     새 파일을 생성
'x': 베타적 생성
     새파일을 생성하지만, 이미 파일이 존재하면 error
'a': 추가
     파일의 끝에 내용을 추가
     파일이 없으면 새 파일 생성
'b': 바이너리
     파일을 바이너리 형식으로 open
     텍스트 파일, 이미지, 동영상등 처리할때 사용
't': 텍스트 
     파일을 텍스트 형식으로 open 
'+': 읽기와쓰기모드
     'r', 'w', 'a' 같은 모드와 함께 사용가능

input_file = open('word.in', 'r')
input_file.readline()
> '12 13\n'

input_file.readline()
> 'perhaps begger poetry will be written in the language of digital computers\n'

input_file = open('word.in', 'r')
input_file.readline().rstrip() # rstrip 으로 가장 왼쪽의 `\n` 을 제거
> '12 13'

input_file.readline().rstrip()
> 'perhaps begger poetry will be written in the language of digital computers'

o_file = open('out.out', 'w')
o_file.write('1')
o_file.write('2')
o_file.close()

i_file = open('out.out', 'r')
i_file.readline()
> '12'
i_file.readline()
> ''

만약, wirte 시에 줄을 구분하고 싶다면 마지막에 '\n' 을 넣어주어야 한다

o_file = open('out.out', 'w')
o_file.write('1\n')
o_file.write('2\n')
o_file.close()

i_file = open('out.out', 'r')
i_file.readline()
> '1\n'
i_file.readline()
> '2\n'
i_file.readline()
> ''

항상 작업이 끝나면 파일을 닫아야 한다
이는 더이상 파일이 필요하지 않으며 더이상의 메모리 참조가 없으므로
가비지 컬렉터에 의해 해당 메모리 참조가 제거된다

이는 OS 의 리소스관리를 위해 반드시 필요한 작업이다

i_file = open('out.out', 'r')
i_file.readline()
'1\n'
i_file.readline()
'2\n'
i_file.close()
i_file.readline()
Error!!

이를 위한 with 문이 존재한다

with open('out.out', 'r') as f:
    i_f = f.read()
    print(i_f)

----------------------------------------------------------------------------------

* 문제

이는 해당 구문이 끝나면 알아서 close() 를 실행해 준다

베시는 에세이를 쓰고 있다.
에세이의 각 단어에는 소문자 또는 대문자만 포함된다

그녀의 선생님은 한줄에 쓸수 있는 최대 문자 수(공백 제외)를 지정했다
이 요구사항을 충족하기 위해 베시는 다음 규칙을 사용해서 에세이의 단어를 기록한다

- 다음 단어가 현재 라인에 맞으면 현재 라인에 추가한다
  한 라인 내 단어들 사이에 공백을 포함한다

- 다음 단어가 현재 라인에 맞지 않으면 새 라인에 넣는다
  이 라인은 새로운 현재 라인이 된다

각 라인에 올바른 단어로 에세이를 출력하라

* 입력

word.in 이라는 파일에서 입력을 읽는다
입력은 두줄로 구성된다

- 첫번째 라인에는 공백으로 구분된 두개의 정수 n, k 가 있다
  n 은 에세이 단어 수로, 1 ~ 100 사이 정수이다
  k 는 한줄에 표시될 수 있는 최대 문자수(공백 제외)로, 1 ~ 80 사이의 정수이다

- 두번째 라인에는 공백으로 구분된 n 개의 단어가 있다
  각 단어는 최대 k 개의 문자로 구성된다

* 출력

word.out 이라는 파일에 출력을 쓴다. 올바른 형식의 에세이를 출력하라

* 만들 코드 정리

- 첫번째 라인은 에세이의 단어수인 n 과 한줄에 표시될수 있는 최대 문자수 k 가 있다
- 두번째 라인이 공백을 구분자로한 n 개의 단어를 가진다

1. 첫번째 라인의 단어수 n 과 최대 문자수 k 를 가져온다 -> get_count
2. 두번째 라인을 가져와 각 단어를 배열로 만든다 -> get_words
3. 어느 단어까지 구성했는지 알수있는 idx 변수를 사용한다 -> wirte_lines 의 idx 변수
5. 이전 단어의 인덱스에서 부터 현재 인덱스까지 리스트를 자르기 위해 prev_idx 변수를 사용한다 -> wirte_lines 의 prev_idx 변수
6. 각 단어를 n - idx 순회,
   각 단어의 문자를 count 하여 합산,
   합산된 count 가 k 보다 크면, 그 특정 단어의 index 보다 작은 단어까지만 한줄로 구분한다 -> wirte_lines
   - idx: 현재 index
   - prev_idx: 이전 인덱스
   - n - idx: 라인화된 단어를 제외한 순회당할 단어의 개수가 된다  
   - 만들어진 각 라인은 word.out 에 추가된다 -> write_line
7. idx 가 n 보다 작을때 순회를 멈춘다 
8. word.out 을 출력한다. -> print_read_lines
  """

import os;

FILE_PATH = 'word.in'
FILE_OUTPUT_PATH = 'word.out'

def get_count(file_path: str, type: str) -> int:
    """
    word 수와 line 수를 반환하는 함수

    :param file_path: 파일위치
    :param type: 'word' | 'line' 이다
    :return: int 값 
    """
    count = 0
    with open(file_path, 'r') as f:
        line_and_word_count = f.readline().rstrip().split()
        if (type == 'word'):
            count = int(line_and_word_count[0])
        elif (type == 'line'):
            count = int(line_and_word_count[1])

    return count;

def get_words(file_path: str) -> list:
    """
    words 의 list 를 반환하는 함수

    :param file_path: 파일위치
    :return: words 를 담은 list 반환
    """
    # words 를 담을 리스트
    words_lis = []
    # line 을 담을 변수
    line = ''
    # 라인 인덱스
    line_idx = 0
    with open(file_path, 'r') as f:
        # 라인인덱스가 1 이면 words 를 가진 문자열
        # 라인인덱스가 1 이될때까지 순회
        while(line_idx < 2):
            line = f.readline().rstrip();
            # line_idx 증가
            line_idx += 1
    
    words_lis = line.split()
    # 만들어진 리스트 반환
    return words_lis

def write_line(out_path: str, words: list) -> None:
    """
    words 배열을 빈 공백을 구분자로 하는 문자열로 변환후
    out_path 에 추가하는 함수

    :param out_path: 쓰기 작업할 파일경로
    :param words: 쓰기 작업할 리스트
    :return: None
    """

    # add 모드로 file open
    with open(out_path, 'a') as f:
        # 빈 공백 문자열을 구분자로한 문자열
        line = " ".join(words) + '\n'
        # line 쓰기 작업
        f.write(line)


def write_lines(output_path:str, words_count: int, line_limit: int, words: list) -> None:
    """
    파일에 쓰기 작업을 할 함수   

    :param output_path: 쓰기작업할 파일 경로
    :param words_count: 문자 개수
    :param line_limit: 최대 라인 개수
    :parma words: word 를 담은 리스트
    :return: None
    """

    # 만약 파일이 있으면 해당 파일 삭제
    if os.path.isfile(output_path):
        os.remove(output_path)

    # words 의 현재 인덱스
    idx = 0
    # words 의 이전 인덱스
    prev_idx = 0

    # idx 는 words_count 보다 작을때까지 순회된다
    while(idx < words_count):
        # word_list 단어의 문자 개수 카운트 변수
        count = 0

        # idx 를 기준으로 자른 새로운 words 배열
        word_list = words[idx:]

        # word_list_len 길이 만큼 순회
        for word in word_list:
            # word 의 길이를 count 에 합산
            count += len(word)
            # 합산된 count 가 line_limit 보다 크면 쓰기 작업후 break
            if count > line_limit:
                # 순회된 prev_idx 부터 현재까지 순회된 idx 까지 자른 리스트를 전달
                write_line(output_path, words[prev_idx:idx])
                # prev_idx 에 현재 idx 를 할당
                prev_idx = idx
                break;
            # idx 증가
            idx += 1

def print_read_lines(file_path: str) -> None:
    """
    파일의 모든 라인을 읽는 함수

    :param file_path: 읽을 파일 경로
    :return: None
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)

# 문자 개수
words_count = get_count(FILE_PATH, 'word')
# 최대 라인 개수
line_limit = get_count(FILE_PATH, 'line')
# 문자를 담은 리스트
words = get_words(FILE_PATH)
# words 의 라인을 쓰기 작업
write_lines(FILE_OUTPUT_PATH, words_count, line_limit, words)
# output 된 파일 읽기 
print_read_lines(FILE_OUTPUT_PATH)

"""
* 코드 개선

현재 내가 작성한 코드에서 write_lines 에서
words[prev_idx:idx] 로 잘라 wirte_line 으로 넘겨주고 있다
이 코드는 다음처럼 변경 가능하다

라인변수 선언
line = ''

# word_list_len 길이 만큼 순회
for word in word_list:
    # word 의 길이를 count 에 합산
    count += len(word)
    # 합산된 count 가 line_limit 보다 크면 쓰기 작업후 break
    if count > line_limit:
        # 순회된 prev_idx 부터 현재까지 순회된 idx 까지 자른 리스트를 전달
        write_line(output_path, line)
        # 라인값을 빈 문자로 초기화
        line = ''
        break;
    # line 는 빈공백을 구분자로 word 를 합친 문자열이다 
    line += word + " "
    # idx 증가
    idx += 1

그럼 write_line 값도 변경해야 한다

def write_line(out_path, line):
    # add 모드로 file open
    with open(out_path, 'a') as f:
        # 빈 공백 문자열을 구분자로한 문자열
        line += '\n'
        # line 쓰기 작업
        f.write(line)

파이썬의 slice 를 쓰면 새로운 배열이 생성되는것으로 알고 있다
차라리 새로운 배열객체를 만드는것보다는 문자열로 연결해서 처리하는것이 더 좋아보인다
코드 상으로도 더 보기 쉬워진다.

수정해본 wirte_lines 에서
line 을 if 문 밑으로 내렸는데 책에서는 다음처럼 처리했다

# word_list_len 길이 만큼 순회
for word in word_list:
    # line 는 빈공백을 구분자로 word 를 합친 문자열이다 
    line += word + " "
    # word 의 길이를 count 에 합산
    count += len(word)
    # 합산된 count 가 line_limit 보다 크면 쓰기 작업후 break
    if count > line_limit:
        # 순회된 prev_idx 부터 현재까지 순회된 idx 까지 자른 리스트를 전달
        write_line(output_path, line[:-1])
        # 라인값을 빈 문자로 초기화
        line = ''
        break;
    # idx 증가
    idx += 1

음.. -1 값으로 slice 하면 맨뒤의 원소는 제외하고 앞에 있는 모든 원소를 가져온다
이렇게 처리해도 될듯하다.
"""