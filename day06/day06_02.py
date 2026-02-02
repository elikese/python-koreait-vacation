# break & continue
# break를 읽으면 반복문 한번 탈출

for num in range(10):
    # num이 5인 차례라면 탈출
    if num == 5:
        print("5 출현! 탈출!")
        break # 읽으면 코드진행 멈추고 즉시 탈출
        print("내가 실행될까요?")

    print(num) # 5? 안찍힘

# continue를 읽으면 다음 반복을 즉시 실행

for num in range(10):
    if num == 5:
        print("5출현! 다음숫자!")
        continue # 코드진행 멈추고 즉시 다음반복

    print(num) # 5? 안찍힘

# 0~9 숫자중 짝수만
# continue를 써서 출력
for num in range(10):
    # 홀수 조건
    if num % 2 != 0:
        continue
    print(num)

scores = [90, 80, 100, 50, 45]
# 60점 이상 점수들의 평균점수
# 60점 이상에서 ~ 하겠다
# 60점 미만에서 ~ 안하겠다
# continue 사용
score_sum = 0 # 누적합변수
count = 0
for score in scores:
    if score < 60:
        continue
    score_sum += score
    count += 1