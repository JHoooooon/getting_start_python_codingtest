"""
* 문제

다른 사람의 Gmail 주소를 쓰는 방법에는 여러가지가 있다는 것을 알고 있나?

누군가의 Gmail 주소를 가져와 @ 기호 앞에 + 기호와 문자열을 추가하면 새로 만든 주소로
보내는 모든 이메일은 이전의 Gmail 주소가 받게 된다

무슨 말이냐면, Gmail 주소에 관한 한 + 기호부터 @ 기호 바로 앞가지의 모든 문자는 무시된다 
예를 들어, 사람들에게 Gmail 주소를 소개할때 daniel.singaro@gmail.com 이라고 하지만,
이것은 주소를 쓸 수 있는 한가지 방법에 불과하다

daniel.zingaro+book@gmail.com 이라고 말하지만, 이건 주소를 쓸수 있는 한가지 방법에
불과하다. daniel.zingaro+book@gmail.com 이나 daniel.zingaro+hi.there@gmail.com 에
메일을 보내도 daniel.zingaro@gmail.com 이 메일을 받게 된다

그리고 @ 기호 앞의 점은 Gmail 주소에서 무시된다
danielzingaro@gmail.com(점이 없는 경우), daniel..zingaro@gmail.com(연속된 두 점이 있는 경우),
da.nielz.in.gar.o..@gmail.com (마구 쓴 여러개의 점이 있는경우) 등의 주소로 메일을 보내면
danielzingaro@gmail.com 이 메일을 받게 된다

마지막으로 주소 전체의 대소문자의 차이는 무시된다
만일 급히 서둘러 대소문자를 함께 써서
Daniel.Zingaro@gmail.com, DAnIELZIngARO+Flurry@gmAIL.COM 등의 주소로 메일을
보내도 danielzingaro@gmail.com 이 메일을 받게 된다

Email Addresses 문제에서는 이메일주소들이 입력되는데, 그중 고유한(중복이 없는) 주소가
몇개인지 알아내야 한다. 이 문제에서 이메일 주소에 대한 규칙은 앞서 Gmail 에 대해
논의된 규칙과 동일하다.

+ 기호부터 @ 기호 바로 앞까지의 문자는 무시되고, @ 기호 앞의 점은 무시되며,
전체 주소에서 대소문자는 구별되지 않는다

* 입력

입력은 10개의 테스트 케이스로 구성된다
각 테스트 케이스에는 다음 라인들이 포함된다

-   이메일 주소의 개수 n 이 포함된 라인. n 은 1 에서 100000 사이의 정수
-   한 라인당 하나의 이메일 주소를 담고 있는 n 개의 라인
    이메일 주소는 @ 기호 앞 문자는 문자, 숫자, 점, 더하기 기호로 구성
    @ 기호 뒤의 문자는 문자, 숫자, 점으로 구성

* 출력

각 테스트 케이스에 대해 고유한 이메일 주소의 개수를 출력
평가 사이트는 테스트 케이스의 실행 시간에 제한을 두고 있다
제한 시간은 30 초 이다

* 코드 정리

- @ 기호 앞 문자의 . 은 무시된다
- + 와 @ 사이의 문자는 무시된다
- 대문자가 포함되면 소문자로 변경된다.
- 첫 라인: 이메일 주소의 개수
- 이후 n 라인: 이메일들

-- TODOS --

1. 첫 라인을 사용하여 email 의 개수를 가져온다 -> email_count
2. 이후 라인들을 가져와 이메일을 배열화 시킨다 -> get_emails
3. @ 기호 앞 문자의 . 을 무시한 이메일들을 만들고 결과 배열에 넣는다 -> remove_dot
4. + 와 @ 사이의 문자를 무시하는 이메일들을 만들고 결과 배열에 넣는다 -> remove_plus_sign
5. 대문자를 소문자로 변경한 이메일들을 만들고 결과 배열에 넣는다 -> replace_to_lower
6. set 으로 고유한 값을 가진 리스트를 만든다
7. 만든 set 의 length 를 출력한다

"""

def get_emails() -> list:
    """
    이메일을 가져와 배열을 만드는 함수

    :return: email 리스트
    """
    global email_count

    emails = []

    for _i in range(email_count):
        email = input()
        emails.append(email)

    return emails

def remove_dot(emails: list) -> list:
    """
    이메일에서 @ 앞의 . 을 무시하는 함수

    Params:
        emails (list): 이메일 리스트
    Return:
        list: . 을 제외한 이메일 리스트
    """
    new_emails = []

    for email in emails:
        at_idx = email.find('@')
        dot_email = email[:at_idx].replace('.', '')
        new_email = dot_email + email[at_idx:]
        new_emails.append(new_email)

    return new_emails;

def remove_plus_sign(emails: list[str]) -> list:
    """
    이메일에서 + 와 @ 사이에 있는 문자열을 무시하는 함수

    Parmas:
        emails (list): 이메일 리스트
    Returns:
        list: + 와 @ 사이의 문자열을 무시한 이메일 리스트
    """
    new_emails = []

    for email in emails:
        plus_idx = email.find('+')
        at_idx = email.find('@')

        if (plus_idx != -1 and at_idx > plus_idx):
            new_email = email[0:plus_idx] + email[at_idx:]
            new_emails.append(new_email)
        else:
            new_emails.append(email)
    
    return new_emails

def replace_to_lower(emails: list[str]) -> list:
    """
    이메일에서 + 와 @ 사이에 있는 문자열을 무시하는 함수

    Parmas:
        emails (list): 이메일 리스트
    Returns:
        list: + 와 @ 사이의 문자열을 무시한 이메일 리스트
    """

    new_emails = []

    for email in emails:
        new_email = email.lower()
        new_emails.append(new_email)

    return new_emails

# 문제이해를 약간 잘못했음
#
# def to_email_dict(emails: list[str]) -> dict:
#     """
#     이메일을 키로, 이메일의 개수를 값으로 하는
#     dict 를 만드는 함수

#     Parmas:
#         emails (list): 이메일 리스트
#     Returns:
#         dict: 이메일을 키로, 이메일의 개수를 값으로 하는 dict 
#     """

#     email_dict = {}

#     for email in emails:
#         if email in email_dict:
#             email_dict[email] += 1
#         else:
#             email_dict[email] = 1
        
#     return email_dict

for i in range(10):
    email_count = int(input())
    emails = get_emails()
    emails = replace_to_lower(emails)
    emails = remove_dot(emails)
    emails = remove_plus_sign(emails)
    emails = set(emails)

    print(len(emails))