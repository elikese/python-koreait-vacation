# 튜플(tuple): 수정과 삭제가 안되는 리스트
# 복사해서만 수정가능(슬라이싱은 가능)

fruits = ("사과", "바나나", "포도", "수박")
# fruits[0] = "망고" 재대입 불가
# del fruits[0] 삭제 x

# 읽기기능들은 가능
print(fruits[0])
# index로 위치 읽기 가능
idx_of_grape = fruits.index("포도")
# in 연산자
print("바나나" in fruits)

# 튜플 언패킹
mr_hong = ("홍길동", "한국", 25, "남자")
name, nation, age, gender = mr_hong

# 값 스왑
a = 10
b = 20
a, b = b, a
print(f"a={a}, b={b}")

coord = (3, -3)
# 조건문을 사용하여 coord가 몇사분면에 있는지 출력
# 원점, x, y축 위에 있는경우 제외
x, y = coord

# 중첩 조건문
if x > 0:
    if y > 0:
        print("1사분면")
    elif y < 0:
        print("4사분면")
elif x < 0:
    if y > 0:
        print("2사분면")
    elif y < 0:
        print("3사분면")