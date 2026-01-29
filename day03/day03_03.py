# 조건문
"""
멀티라인 - 주석처럼 사용가능
if bool자료형:
    if가 True일때 실행될 코드
elif bool자료형:
    elif가 True일때 실행될 코드
else:
    위의 조건들이 모두 False일때 실행될 코드

---
파이썬에서는 들여쓰기에 민감하다
: 이후로 들여쓴부분을 하나의 코드구역으로 간주한다.
"""

if False:
    print("if문 안쪽입니다.")
    print("if문 안쪽입니다.")
    print("if문 안쪽입니다.")
print("if문 바깥입니다.")

# if ~ elif ~ else
# 1. 하나의 코드블럭만 실행
# 2. 순차적으로 위에서 아래로 검사

age = 15

# 조건은 내림차순, 오름차순으로 작성되어야함
if age >= 20:
    print("성인!")
elif age >= 17: # age < 20
    print("고등학생!")
elif age >= 14: # 이전조건이 False
    print("중학생!")
elif age >= 8:
    print("초등학생!")
else:
    print("미취학아동!")
# 코드블럭 하나만 실행하고 탈출

is_login = False
is_banned = True
if not is_login:
    print("로그인을 하셔야합니다.")
elif is_banned:
    print("정지된 계정입니다.")

# 홀짝판별
# num을 input으로 입력받고
# 짝수면 "짝수입니다" 출력
# 홀수면 "홀수입니다" 출력
num = input("숫자 입력 >")
num = int(num) # str -> int
if num % 2 == 0:
    print("짝수입니다")
elif num % 2 != 0:
    print("홀수입니다")

