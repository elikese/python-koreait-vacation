# 반복문 - for문
"""
for 변수 in 전체:
    반복 실행될 코드
전체 -> 컬렉션자료형, 문자열, range()...
반복마다 하나씩 가져올수있는 구조면 ok(__iter__)

변수 -> 순서대로 "대입"받을 변수
"""

print("hello") # 엔터키가 자동포함
print("hello", end=" ") # end로 수정가능
print("hello")

numbers = [0,1,2,3,4,5]
for number in numbers:
    print(number, end=" ")

print() # 엔터
for number in range(10):
    print(number, end=" ")

# range(n) -> 0이상 n미만을 가진 리스트유사체
# range(a, b) -> a이상 b미만을 가진 리스트유사체

# 요소가 필요없으면 _로 표현(관행)
for _ in range(5):
    print("hello world!")

# 1~50까지 홀수끼리, 짝수끼리 나누어 담아보자
odds, evens = [], [] # 튜플 언패킹

for num in range(1, 51):
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

# 1~50까지 누적합을 구해주세요!
num_sum = 0
# [1,2,3,4....50]
for num in range(1, 51):
    num_sum = num_sum + num
print(num_sum)

# 홀수는 홀수끼리, 짝수는 짝수끼리
# 더하여 각각 출력!
even_sum, odd_sum = 0, 0
for num in range(1, 51):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

names = ["김길동", "홍길동", "박길동", "박철호", "박화목"]
# 박 성씨 이름만 모으기
parks = []

for name in names:
    if name[0] == "박":
        parks.append(name)

# for문으로 각 파일명 확인 후
# .exe로 끝나는(endswith) 파일이 있으면
# "{파일명} 발견!, 위험한파일!" 출력!
files = ["report.pdf", "ad.exe",
         "setup.bat", "memo.txt"]

for file in files:
    if file.endswith(".exe"):
        print(f"{file} 발견! 위험한파일!")

# files를 반복하면서 banned_files에 기록된
# 확장자로 끝나면 출력
banned_files = [".exe", ".bat"]
for file in files:
    # 각 file 확장자 추출
    dot_idx = file.index(".")
    ext = file[dot_idx:]
    # 추출한 확장자가 banned에 있는지?
    if ext in banned_files:
        print(f"{file}발견! 위험한 파일!")


# 2중 for문
# 바깥반복 한번당 안쪽 반복 전체가 도는 구조

# 일주일
for day in range(1, 8):
    print(f"{day}일 살았습니다")

# 한달
for week in range(1, 5):
    print(f"{week}주 시작!")
    for day in range(1, 8):
        print(f"    {day}일 살았습니다")
    print(f"{week}주 끝!")

# 구구단
"""
2 x 1 = 2
2 x 2 = 4
...
2 x 9 = 18
"""

print(f"{2}단 시작!")
for num in range(1, 10):
    print(f"{2} x {num} = {2 * num}")
print(f"{2}단 끝!")

# 3단 완성!
print(f"{3}단 시작!")
for num in range(1, 10):
    print(f"{3} x {num} = {3 * num}")
print(f"{3}단 끝!")

# 4단 완성!
print(f"{4}단 시작!")
for num in range(1, 10):
    print(f"{4} x {num} = {4 * num}")
print(f"{4}단 끝!")

# 2중 for문으로 9단까지 출력!
# num = range(2,10)[0] - 대입이 생략되어있음
for dan in range(2, 10):
    print(f"{dan}단 시작!")
    for num in range(1, 10):
        print(f"    {dan} x {num} = {dan * num}")
    print(f"{dan}단 끝!")


# 두 리스트 비교
s1 = ["a", "b", "c"]
s2 = ["b", "d", "com", "c"]
# s1과 s2 리스트의 같은 요소가 몇개?
count = 0
for x in s1:
    for y in s2:
        if x == y:
            count += 1



