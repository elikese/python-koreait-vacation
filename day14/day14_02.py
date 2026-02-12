# else: 예외없이 성공했을 경우
try:
    age = "10"
    age = int(age)
except ValueError as e:
    print("숫자가 아니네요")
else:
    # try안에 코드가 에러없이 작동될 가정하에 작성됨
    if age > 19:
        print("성인!")
    else:
        print("미성년자!")

# finally: 예외가 발생하건 말건 항상 실행

file = None
try:
    file = open("./hi.txt", "r", encoding="utf-8")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("hi.txt 없는데요")
finally:
    # 예외와 상관없이
    # 주로 자원반납
    if file is not None:
        file.close()

# 도전) 아래의 코드를 try-except-else-finally
# 에러없이 성공시 result를 출력!
# 에러발생과 무관하게 "계산완료!" 출력
# try:
#     num1 = input("첫번째 숫자입력 >")
#     num1 = int(num1)
#     num2 = input("두번째 숫자입력 >")
#     num2 = int(num2)
#     result = num1 / num2
# except (ValueError, ZeroDivisionError) as e:
#     print("정상적인 값을 입력하세요")
# else:
#     print(f"결과:{result}")
# finally:
#     print("계산완료!")

# 예외객체를 의도적으로 생성하는 문법
# raise 에러클래스()
try:
    raise ValueError("저는 님이 만든 에러입니다")
except ValueError as e:
    # e를 출력하면 생성할때 넣어준 메세지가 출력됨
    print(e)

# 커스텀(비즈니스) 예외
# Exception 클래스를 상속받으면 ok
class ScoreError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class TestScore:
    def __init__(self, score):
        if not (0 <= score <= 100):
            raise ScoreError("0~100 값만 가능합니다")
        self.score = score

t1 = TestScore(50)
try:
    t2 = TestScore(999)
except ScoreError as e:
    print(e)
    # 에러상황시 분기시고 싶은 코드를 작성

email = input("이메일 >>>")
# @가 없으면 EmailError를 발생시켜주세요
# EmailError를 만들어주세요
class EmailError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

try:
    if "@" not in email:
        raise EmailError("@가 없습니다")
except EmailError as e:
    print(e) # "@가 없습니다"
else:
    print("올바른 이메일 형식입니다")

