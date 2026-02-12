# day14_01
# 예외(error)처리
# 파이썬에서는 error도 객체다
# 파이썬은 error객체를 감지하면, 즉시 코드진행을 멈춘다

"""
예외처리 문법
try:
    예외가 발생할 가능성이 있는 코드
except(예외종류1, 예외종류2...):
    try안에 코드에서 예외가 발생할 경우 실행할 코드
--- 선택 ---
else:
    예외없이 try안에 코드가 성공했을때 실행할 코드
finally:
    예외여부와는 상관없이 반드시 마지막에 실행할 코드
"""

# 예외 종류
# 1. SyntaxError - 문법에러(코드아래 빨간줄)
# 2. TypeError - 타입이 맞지 않는 '연산'시 발생
try:
    a = "아무개"
    b = 25
    print(a + b) # error 생성되면서 즉시 정지
    print("저는 실행될까요?") # no
except TypeError as e: # e라는 변수에 에러객체를 대입하겠다
    print(f"에러 내용: {e}")

# 3. NameError: 변수 선언전에 읽으려고 할때
# 4. IndexError: 인덱스 범위를 벗어난걸 읽을 때
my_numbers = [1,2,3,4,5]

# 에러 가능성이 존재하는 코드
# input_num = input("숫자입력 >")
# input_num = int(input_num)
# print(my_numbers[input_num])

# 5. KeyError: dict에 없는 key로 읽으려고 할 때
# 6. ImportError: 없는 .py파일을 import 할 때
# 7. ZeroDivisionError: 0으로 나누려고 할 때
# 8. ValueError: 타입은 맞는데, 값이 이상할 때
try:
    sample = "abc"
    int(sample) # 문자열ok, 숫자같은 문자열

    names = ["철수", "영희"]
    names.remove("병철") # 문자열ok, 리스트에 있는 값이어야함
except ValueError as e:
    print(f"에러내용: {e}")

# try:
#     num = input("숫자 입력 >")
#     num = int(num) # ValueError
#     result = 100 / num # Zero~Error
#     print(result)
# except (ValueError, ZeroDivisionError) as e:
#     print("올바른 값을 입력하세요")

# 도전) 아래의 코드에서 예외가 발생할 경우를 고려하여
# try - except를 작성해 주세요
try:
    colors = ["빨강", "파랑", "노랑", "검정"]
    my_idx = input("찾으실 색상번호 입력 >")
    my_idx = int(my_idx) # ValueError
    result = colors[my_idx] # IndexError
    print(f"선택한 색상: {result}")
except (ValueError, IndexError) as e:
    print("0~3사이 값만 입력하세요")
    print(f"에러내용: {e}")

