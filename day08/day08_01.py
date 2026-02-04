import random

# 가위바위보
rsp = ["가위", "바위", "보"]
my_score = 0
com_score = 0

# 3판 2선승제로 변환
# 나 vs 컴, 둘 중 2점을 얻으면 승리
while True:
    my_choice = input("가위, 바위, 보 입력 >")
    my_choice = my_choice.strip() # 공백제거

    # 입력값 검증
    # 내가 입력한값이 리스트안에 없다면
    if my_choice not in rsp:
        print("다시 입력하세요")
        continue

    # 컴퓨터는 하나를 랜덤으로 뽑아옴
    com_choice = random.choice(rsp)

    # 승리조건들
    # index를 이용하면..?
    win_cond1 = my_choice == "가위" and com_choice == "보"
    win_cond2 = my_choice == "바위" and com_choice == "가위"
    win_cond3 = my_choice == "보" and com_choice == "바위"
    win_conds = [win_cond1, win_cond2, win_cond3]

    if my_choice == com_choice:
        print("무승부")
        continue # 다시
    elif True in win_conds:
        print(f"나:{my_choice} vs 컴:{com_choice}")
        print("승리!")
        my_score += 1
    else:
        print(f"나:{my_choice} vs 컴:{com_choice}")
        print("패배..")
        com_score += 1

    print(f"나:{my_score} vs 컴:{com_score}")

    if my_score == 2:
        print("나의 승리!")
        break
    elif com_score == 2:
        print("컴퓨터 승리!")
        break

print("게임종료")