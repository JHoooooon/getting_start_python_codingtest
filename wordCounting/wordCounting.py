print("Welcome to wordCounting:")
print("-" * 20)
wording = input("내용을 입력해주세요:\n")

# count 는 입력한 값이 문자열에서 몇번 나오는지 체크한다
# count 를 사용하여, 공백의 개수를 세고 + 1 한 값이 총 단어의 수가 된다.
counting = wording.count(' ') + 1

print("현재 입력한 내용의 단어는 총", counting, "입니다.")
