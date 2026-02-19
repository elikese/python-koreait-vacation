# 파이썬 내장함수(built-in 함수)
# sum(리스트) -> 리스트 내부의 데이터를 모두 합한 것 리턴
nums = [100, 200, 300, 400]
result = sum(nums)

# min(리스트), max(리스트) -> 리스트 내부에서 최소값, 최대값 리턴
min_val = min(nums)
max_val = max(nums)

# all(리스트): 리스트 내부값들을 모두 and연산
# -> 모두 True면 True

# any(리스트): 리스트 내부값들을 모두 or연산
# -> 하나라도 True면 True
승리조건들 = [True, False, False]
print("승리?", True in 승리조건들)
print("승리?", any(승리조건들))

numbers = [1, 3, 5, 8]
# 짝수가 하나라도 있는가?
result = any([n % 2 == 0 for n in numbers])

names = ["김길동", "최길동", "김철수", "이민수"]
# 도전!) names에 박씨가 한명이라도 있는가?
# startswith("박") 아니면 name[0] == "박"
result2 = any([name[0] == "박" for name in names])
print("박씨있나요? ", result2)

### 함수의 변수 생존범위(스코프)
# 1. 함수안에서 선언된 변수는 함수 안에서만 생존가능
def a():
    name = "홍길동"
    print("name: ", name)

# print(name) # 외부에서는 인식x

# 2. 외부(일반)변수는 함수안에서 "읽기"만 가능
constant = 100
def print_const():
    print("상수: ", constant)
    # constant += 100 변경이 막혀있음

# 3. 외부(일반)변수를 함수안에서 변경시 global
def change_const():
    global constant
    constant += 100

### 문법 끝! ###