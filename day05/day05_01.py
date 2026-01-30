# 딕셔너리(dict)
# 리스트, 튜플 -> index숫자로 데이터 보관
# dict는 숫자대신 key라는 데이터로 보관
mr_park = {
    "이름": "박철수",
    "나이": 30,
    "성별": "남자",
    "취미": "유튜브시청"
}

# 생성자 방식
mr_park = dict(
    이름 = "박철수",
    나이 = 30,
    성별 = "남자",
    취미 = "유튜브시청"
)

# 데이터 읽기
print(mr_park["이름"]) # value 조회
print(mr_park.get("이름")) # 방법2

# 추가, 수정
# 이미 있던 key에 value를 대입하면 수정
# 없던 key에 value를 대입하면 추가
mr_park["나이"] = 31 # 기존 30을 덮어씀
mr_park["직장"] = "코리아아이티" # 생성(추가)

# 추가, 수정 한번에
mr_park.update({
    "나이": 32, # 수정
    "국적": "대한민국" # 추가
})

# 제거
del mr_park["직장"] # 삭제
hobby = mr_park.pop("취미") # 꺼내오기

menu = {
    "김밥": 3000,
    "라면": 4000,
    "돈까스": 7000
}
# menu에 떡볶이(5000) 추가
# 라면가격을 5000으로 인상
menu.update({
    "떡볶이": 5000,
    "라면": 5000
})
# 김밥과 라면을 먹으면 내야할 금액출력
kimbab = menu["김밥"]
ramen = menu["라면"]
print(kimbab + ramen)

# len - 가지고있는 key갯수
print(len(menu))

# in 연산자 - key가 있는지?
print("김밥" in menu)
print("떡볶이" in menu)


menu = {
    "김밥": 3000,
    "라면": 4000,
    "돈까스": 7000
}
# key들만 list로 모아오기
# ["김밥", ..."돈까스"]
menu_names = menu.keys()
# 리스트로 사용하려면 list로 형변환
menu_names = list(menu_names)
print(menu_names)

# value들만 list로 모아오기
menu_prices = menu.values()
menu_prices = list(menu_prices)
print(menu_prices)

# items(): (key, value) 쌍으로 튜플로 묶여서 리스트에 모아줌
# [(k,v), (k,v)....]
menu_items = menu.items()
menu_items = list(menu_items)
print(menu_items)

# [('김밥', 3000), ('라면', 4000), ('돈까스', 7000)]
k, v = menu_items[0] # 0번칸 튜플을 튜플언패킹
print(f"{k}: {v}원")

# dict의 value에는 모든 자료형 저장 가능
# dict의 key에는 불변형(원본변형 안됨) 저장 가능

# 튜플도 key로 사용가능
my_foodie = {
    (5, 10): "양식맛집",
    (10, 10): "중식맛집",
    (15, 10): "일식맛집",
}
# (15, 10)좌표가 my_foodie에 있는지 확인하는 조건문
# 맛집이면 해당 맛집의 이름을 출력
my_location = (15, 10)
if my_location in my_foodie:
    name = my_foodie[my_location]
    print(name)