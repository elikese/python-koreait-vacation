"""
변수? 데이터를 재사용
함수? 코드를 재사용

함수 "정의"
def 함수이름(매개변수1, 매개변수2..):
    코드 작성

    return 데이터
- 매개변수와 리턴은 선택사항
"""

# 매개변수 x, 리턴x
def hello():
    # 호출되면 아래의 코드를 실행하세요
    print("hello 호출 됨!")
    print("안녕하세요")

print("함수 호출 전")
hello() # 함수 호출
print("함수 호출 후")


outer = 100
# 매개변수
def hello_name(name, address):
    # 매개변수(파라미터): 호출하는 쪽에서 값을 전달할 수 있음
    # 생존범위 존재 - 함수 안에서만 유효
    hello_data = 10 # 함수 내에서 변수 선언 - 함수안에서만
    print(outer) # 함수 밖 변수는 생존가능
    print(f"{address}에 사는 {name}님 안녕하세요")

# print(hello_data)
# print(name)
# print(address)
hello_name("홍길동", "부산")

def get_100():
    print("get_100 호출됨!")
    # 리턴: 함수의 호출 결과값
    return 100 # 리턴을 만나면 함수는 즉시종료
    print("아무거나")

return_val = get_100()
print(return_val) # 100

# 매개변수로 숫자 2개를 받아서
# 두 수를 더하고
# 결과가 짝수면 "짝수" 리턴
# 결과가 홀수면 "홀수" 리턴
# 함수명: print_add_result
def print_add_result(x, y):
    sum_num = x + y
    if sum_num % 2 == 0:
        return "짝수"

    return "홀수"

# 리턴은 호출결과 -> 데이터를 리턴했다면 데이터가 됨
result = print_add_result(10, 20)
print(result)
# 값이라면 값처럼 다룰 수 있다.
# f(g()): g -> f // f(g1(), g2()): g1 -> g2 -> f
result2 = print_add_result(get_100(), get_100())