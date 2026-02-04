# import: .py파일 밖에서 코드를 복붙해 오는 것
import random

# 1~6 사이 랜덤 정수를 하나 뽑아오는 것
my_random_number = random.randint(1, 6)
print(my_random_number)
pocket = ["500원", "100원", "1000원"]
# 무작위 하나 선택
first_pocket = random.choice(pocket)

# 업다운게임
# 입력 < 랜덤 : 업!
# 입력 > 랜덤 : 다운!

# 입력값이 1~100사이인지 검증하는 코드(조건문)
# 1~100 가 아니면 다시 입력받도록 구현
answer_num = random.randint(1, 100)
while True:
    my_guess = input("1~100사이 숫자 입력>")
    # if문으로 0~9문자를 입력했는지 검증
    # 문자열.isdecimal() -> "0"~"9" 문자로만 이루어졌나?
    if not my_guess.isdecimal():
        print("숫자만 입력하세요")
        continue

    my_guess = int(my_guess) # 검증 후 형변환

    ok_condition = 1 <= my_guess <= 100
    if not ok_condition:
        print("1~100사이 입력하세요")
        continue

    if my_guess < answer_num:
        print("up!")
    elif my_guess > answer_num:
        print("down!")
    else:
        print(f"정답!! : {answer_num}")
        break