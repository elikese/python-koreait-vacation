# range()가 반환하는 유사리스트
# 리스트로 사용하려면 형변환
num_list = range(1, 11)
num_list = list(num_list) # 형변환

foods = ["계란", "우유(상함)", "사과", "수박(상함)"]
# (상함)이 포함된 문자열에 (상함)을 제거해달라
# 파이썬 for문은 인덱스 정보x
# 1st loop: food = foods[0] -> 값을 복사한 것
for food in foods:
    if "(상함)" in food:
        food.replace("(상함)", "")

print(foods) # 원본 보존

# 순서(인덱스)정보가 for문에 필요
# enumerate(리스트): 리스트 각 데이터를 (인덱스, 데이터) 튜플로 변환
# ["계란", "우유"] -> [(0, "계란"), (1, "우유")]
# sample = enumerate(foods)
# print(list(sample))

for food_tuple in enumerate(foods):
    index, food = food_tuple # 튜플언패킹
    print(f"{index}: {food}")

# 최종형태
for index, food in enumerate(foods):
    if "(상함)" in food:
        # 리스트[index] = 수정데이터
        foods[index] = food.replace("(상함)", "")

print(foods)

# 도전1
fruits = ["사과", "바나나", "포도", "체리"]
# 홀수 인덱스에 있는 과일들만 출력해주세요!
# (0, "사과")
for idx, fruit in enumerate(fruits):
    if idx % 2 != 0:
        print(fruit)

# 도전2
coords = [(3, -3), (2, 3), (1, -2), (5, 6)]
my_coord = []
# 1사분면에 해당하는 좌표만 my_coord에 추가해주세요
for coord in coords:
    x, y = coord
    if x > 0 and y > 0:
        my_coord.append(coord)
        print(f"({x},{y})")

# 딕셔너리.items()
# -> [(key, value)...]
menu = {
    "김밥": 3000,
    "라면": 4000,
    "돈까스": 7000
}

for food, price in menu.items():
    print(f"{food}: {price}")

scores = {
    "철수": 85,
    "영희": 55,
    "민수": 70,
    "지영": 40
}
# items()사용하셔서 점수가 60이상인 학생이름 출력
for name, score in scores.items():
    if score >= 60:
        print(f"{name}님 합격입니다!")



