# day03 -> day03_01.py

# 연산자
# 산술연산자(사칙연산)
print(20 + 20)
print(20 - 20)
print(20 * 20)
print(20 / 20) # 소숫점까지 표현

# 나머지 연산
print(20 % 8) # 4
# 몫 연산
print(20 // 8) # 2
# 제곱
print(2 ** 4) # 2의 4승

print("홍" + "길동")
print("홍" * 3) # 홍홍홍

# 비교연산자 -> 결과가 bool형
x = 10
y = 20
print(x == y) # 같나요?
print(x != y) # 다른가요?
print(x > y) # x가 y초과입니까?
print(x >= y) # x가 y이상입니까?
print(x < y)
print(x <= y) # 꺽쇄다음 =으로 이상,이하

print(5 < x < 20) # 가능

num = 112
# num이 짝수인가요?
print(num % 2 == 0)
# num이 5의 배수인가요?
print(num % 5 == 0)

# 현재 시각에서 50시간 더한 시각?
now = 9
result = (now + 50) % 24
print(result) # 시간

num = 10
num = num + 5
# num이 가진값을 5증가
num += 5
num -= 5
num *= 5
num /= 5

# 논리연산자 - bool자료형끼리의 연산
a = True
b = False
# and연산: 둘다 True여야 True
print(a and b)
# or연산: 둘중 하나라도 True면 True
print(a or b)
# not연산: bool값을 반전
print(not a) # True -> False

print(5 < x < 20)
print(x > 5 and x < 20)

# 연산자 우선순위
# 우선순위 동일시 왼쪽부터 실행
# () > 산술 > 비교 > 논리 > 대입

# 조건연산자(삼항연산자)
# (True일때 값) if 조건식 else (False일때 값)
score = 70
cut_line = 60
result = "pass" if score >= cut_line else "fail"

# 중첩가능 - 조건연산자는 하나의 값으로 취급가능
grade = "A" if score >= 90 else "B" if score >= 80 else "C"

real_id = "python"
real_pw = "1234"
# 도전!)
# 1. input을 통해 input_id / input_pw 입력받기
# 2. input_id과 real_id 비교, input_pw와 real_pw비교
# 둘다 같으면 "로그인성공", 하나라도 다르면 "로그인실패" 출력
input_id = input("아이디 입력 >")
input_pw = input("비밀번호 입력 >")

is_same_id = input_id == real_id
is_same_pw = input_pw == real_pw
is_login = is_same_id and is_same_pw
result = "로그인성공" if is_login else "로그인실패"
print(result)





