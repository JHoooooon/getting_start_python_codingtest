"""
# DMOJ 에서는 Do the Shuffle 로 되어있다

각각 A, B, C, D, E 라는 노래 5곡이 있다
좋아하는 노래들로 재생목록을 만들어 앱에서 관리하고 있다
처음에 노래는 A, B, C, D, E 순서로 재생되며, 앱에는 4개의 버튼이 있다

- 버튼1
재생목록의 첫번째 곡을 재생목록의 끝으로 이동시킨다
예를 들어, 재생목록이  A, B, C, D, E 일때 이 버튼을 누르면
B, C, D, E, A 가 된다

- 버튼2
재생목록의 마지막 곡을 재생목록의 시작 부분으로 이동시킨다
예를 들어, 재생목록이  A, B, C, D, E 일때 이 버튼을 누르면
E, A, B, C, D 가 된다

- 버튼3
재생목록의 처음 두곡의 위치를 바꾼다
예를 들어, 재생목록이  A, B, C, D, E 일때 이 버튼을 누르면
B, A, C, D, E 가 된다

- 버튼4
재생목록을 재생한다

사용자가 어떤 버튼을 눌렀는지 알려주고, 사용자가 버튼 4를 누르면 재생목록의 노래 순서를 출력하라

* 입력

입력은 한쌍의 라인들로 구성된다

첫번째 라인은 버튼 번호(1,2,3,4) 를 제공하고,
두번째 라인은 사용자가 버튼을 누른 횟수(1 - 10까지) 를 제공한다

이는 버튼4 를 누를때까지 계속 반복된다

* 출력

버튼을 모두 누른 후 재생목록의 노래 순서를 출력
재생목록은 한줄로 출력되어야 하며, 그 안에는 각 노래를 구분하는 공백이 있어야 한다
"""

# 플레이중인지 확인하는 변수
played = False
# 노래 목록
songs = ['A', 'B', 'C', 'D', 'E']

# 버튼 누르는 함수
def press_btn(btn: int):
    # 노래목록 
    global songs
    # 플레이 변수
    global played

    # 1번 버튼
    if (btn == 1):
        temp = songs[0]
        songs = songs[1:]
        songs.append(temp)

    # 2번 버튼
    elif (btn == 2):
        temp = songs.pop()
        songs.insert(0, temp)
    # 3번 버튼
    elif (btn == 3):
        temp = songs[0]
        songs = songs[1:]
        songs.insert(1, temp)
    # 4번 버튼
    elif (btn == 4):
        # played 를 True 하여 반복문 중단
        played = True

while(not played):
    # 버튼 번호 입력
    btn = int(input())
    # 버튼을 몇번 누를지 입력
    n_press = int(input())

    # n_press 만큼 버튼 클릭
    for _i in range(n_press):
        press_btn(btn)
    
# 빈문자열을 구분자로한 노래 목록 출력
print(" ".join(songs))

"""
책에서는 "ABCDE" 를 문자열로 받아서 처리하는 방법을 사용한다
    songs = "ABCDE"
    if (btn == 1):
        songs = songs[1:] + songs[0]

    # 2번 버튼
    elif (btn == 2):
        songs = songs[-1] + songs[:-1] 
    # 3번 버튼
    elif (btn == 3):
        songs = songs[1] + songs[0] + songs[2:]

자꾸 슬라이스를 사용하기 보다는 temp 에 담아서 값을 치환하는 방식을
사용하려고 하는듯하다.
python 을 사용한다면 slice 를 더 많이 사용하려고 하자.
slice 가 다해 먹는다..
"""