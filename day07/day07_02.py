# 반복문 - while문
# for문 - 반복횟수 기준
# while문 - 조건 기준
"""
while 조건식(bool자료형):
    조건식결과가 True일 동안
    반복될 코드 - 조건을 변경해주는 코드포함
"""

num = 5
# (조건검사 -> 실행) x n
while num > 0:
    print(f"현재 숫자: {num}")
    num -= 1 # 조건을 변경할 코드

# break로 탈출하는 형태
num = 5
while True:
    if num == 0:
        break
    num -= 1

# flag로 탈출하는 형태
num = 5
my_flag = True
while my_flag:
    if num == 0:
        my_flag = False
    num -= 1

# 조건중심의 반복
pw = "123123"
max_trial = 3 # 최대 시도횟수
trial = 0 # 시도횟수
# 3회 초과시 "문이 잠겼습니다" 출력 후 탈출
# 시도횟수 증가 -> pw 틀릴 때
# 공백을 입력시 -> 시도횟수 증가없이 다시 입력받게
# 공백: 문자열의 길이가 0이면 or bool("")
while True:
    my_input = input("비밀번호 입력 >")

    # 공백("")을 bool로 형변환시 False
    if not my_input: # 자동형변환
        print("공백입력, 다시입력하세요")
        continue # 다시 처음부터

    if my_input == pw:
        print("문이 열렸습니다")
        break
    else:
        trial += 1

    if trial == max_trial:
        print("문이 잠겼습니다")
        break