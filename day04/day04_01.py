# 컬렉션 자료형
# 리스트(list), 튜플(tuple), 딕셔너리(dict), 셋(set)
# 대량데이터를 한번에 관리위해 -> 관리위해 반복가능한 구조

# 리스트 []
names = ["홍길동", "김길동", "박길동"]
mix_datas = ["홍길동", 20, False, 1 > 0]

# 리스트와 문자열은 공통점 많음(사촌관계)
names = ["홍길동", "김길동", "박길동"]
# 인덱싱
print(names[0]) # "홍길동"
print(names[0][2]) # "동"
# 슬라이싱
print(names[:2])
# len()
print(len(names)) # 3
# in 연산자 - 해당요소가 리스트안에 존재하는가?
print("김길동" in names) # 정확히 일치해야함

fruits = ["사과", "바나나", "포도", "수박"]
# 데이터 읽기 - 인덱싱!
# 데이터의 위치(index)를 찾아주는 기능
idx_of_grape = fruits.index("포도")
print(idx_of_grape) # 2
# 문자열도 index 존재한다!
# find는 일치데이터 x -> -1
# index 일치데이터 x -> 에러

# 데이터 추가
fruits.append("토마토") # 제일 뒷칸으로 추가
fruits.insert(0, "망고") # 특정위치 추가 - 기존요소 밀려남

# 데이터 삭제
del fruits[0] # 0번 인덱스 데이터 삭제
fruits.remove("사과") # "사과"와 일치하는 데이터 삭제
# pop(): 가장 뒷자리 데이터 꺼내옴(변수에 할당)
# pop(index): index의 데이터 꺼내옴
banana = fruits.pop(0)
last_fruit = fruits.pop()

# 데이터 변경
# fruits 0번칸을 "체리"로 덮어씀
fruits[0] = "체리"

# 리스트와 연산자
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
print(nums1 + nums2) # +로 하는 리스트 병합(원본유지)
print(nums1 * 3) # [1, 2, 3]끼리 3번 덧셈한 결과

# nums1(원본)을 수정하여 병합
nums1.extend(nums2)

# 리스트는 어떤 자료형이든 저장가능
# 리스트안에 리스트도 가능
school = [
    ["김철수", "김영희"],
    ["이철수", "이영희"],
    ["박철수", "박영희"]
]
print(school[1][1]) # 이영희
print(school[2][0]) # 박철수

mart = [
    ["사과", "배"],
    ["바나나", "망고"],
    ["딸기", "체리"]
]
cart = []
# 사과, 바나나, 망고, 체리를 cart에 담아서 출력
사과 = mart[0][0]
바나나 = mart[1][0]
망고 = mart[1][1]
체리 = mart[2][1]
cart.append(사과)
cart.append(체리)
cart = cart + mart[1]
print(cart)

nick_names = ["python", "pypy", "pyqt"]
nick_name = input("이름 입력 >")
# 조건문을 활용해서 nick_name이
# 이미 nick_names에 있는 아이디인지 중복체크
# 중복 -> 중복아이디입니다, x -> 사용가능합니다

if nick_name in nick_names:
    print("중복 아이디입니다.")
else:
    print("사용가능합니다.")