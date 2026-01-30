# set
# 순서보장 x, 중복허용 x
fruits = {"사과", "바나나", "딸기", "사과"}
print(fruits) # 중복시 하나의 값으로 취급

# 추가
fruits.add("메론")
fruits.update({"체리", "수박"})

# 삭제
fruits.discard("체리") # 해당값 없어도 아무일x
fruits.remove("수박") # 해당값이 없으면 에러
fruits.pop() # 랜덤으로 하나 꺼내옴

# 집합연산
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# 합집합: 합친뒤에 중복제거
print(a | b)
print(a.union(b))

# 교집합: 중복값만 추출
print(a & b)
print(a.intersection(b))

# 차집합: 기존값에서 중복값 제거
print(a - b)
print(a.difference(b))

# 컬렉션자료형끼리는 형변환 ok
my_data = ["01-30", "01-29", "01-30"]
# list인데 중복제거? set 형변환
# f1(f2(f3(),f4()))
# f3 -> f4 -> f2 -> f1
my_data2 = list(set(my_data))

math_class = ["철수", "영희", "영수", "상호"]
eng_class = ["철수", "찬호", "영희", "동숙"]
set_math = set(math_class)
set_eng = set(eng_class)
# 둘다 출석한 학생들 출력
print(set_math & set_eng)
print(set_math.intersection(set_eng))
# 수학만 출석한 학생들 출력
print(set_math - set_eng)
print(set_math.difference(set_eng))

# 팔로잉, 팔로워 둘다 해당되는 이름들만 출력!
following = {
    "민수": True,
    "철수": True,
    "지우": True,
    "나연": True,
}
follower = {"정우", "민수", "나연"}
# dict는 형변환 기준도 key기준
set_following = set(following)
print(set_following & follower)
names = set(following.keys())