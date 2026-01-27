# str(문자열)의 여러 기능들
name = "홍길동"
age = 25

# 문자열을 조립하는 방법들
# 1. format()
# {}로 문자열 사이에 변수가 들어갈 자리를 만들고
# 순서에 맞춰서 .format(변수1, 변수2)를 작성
introduce = "안녕하세요, 저는 {}이고, {}살 입니다.".format(name, age)
print(introduce)

# 2. f-string
introduce = f"안녕하세요, 저는 {name}이고, {age}살 입니다."

# 도전!
# input으로 이름과 동네이름을 입력받아주세요
# "저는 ~이고, ~에서 왔습니다"
# 문장을 조립해서 출력해주세요!
# name = input("이름 입력 >>")
# address = input("동네 입력 >>")
#
# intro = f"저는 {name}이고, {address}에서 왔습니다."
# print(intro)

# 문자열은 순서가 존재한다.
# 문자열은 여러 문자들이 모인 데이터이다.
word = "Hello, world!"

# 문자열의 길이(=문자 갯수)
# len(문자열): 해당 문자열의 길이를 가져옴
len_of_word = len(word)
print(f"word의 문자갯수: {len_of_word}")

# 해당칸에 있는 문자 조회 - 인덱싱
print(word[4]) # word의 4번째 문자

# 슬라이싱
# 문자열데이터[시작번호:끝번호]
# 시작번호 이상 ~ 끝번호 미만
print(word[0:5]) # 0번부터 5미만(4) 잘라와!

word = "Hello, world!"
# 도전!) 1. word 변수 인덱싱하여 "r"만 출력해주세요
print(word[9])
print(word[-4])
# 2. "world"만 슬라이싱하여 출력해주세요
# 7 ~ 11
print(word[7:12])

# 뒤에서부터 index 카운트가능
# 가장뒤가 -1
my_str = "Hello, world!"
print(my_str[-1]) # !
print(my_str[:5]) # 0 생략가능
print(my_str[7:]) # 뒤 생략시 끝까지

# 주민번호 뒷자리 모두 *로 치환
ssn = "991111-1234567"
result = ssn[:7] + ("*" * 7)
print(result)

# len(문자열) -> 문자열의 문자 갯수 가져온다
# 문자열.find(문자): 해당 문자의 index를 가져온다

# 1. ssn "-"의 index 구하기
index_of_dash = ssn.find("-")
print(index_of_dash) # 디버깅(확인)

# 2. 뒷자리 추출
last_ssn = ssn[index_of_dash + 1:]

# 3. 뒷자리 문자 갯수
len_last_ssn = len(last_ssn)
print(len_last_ssn)

# 4. 앞자리 + "-" 추출
first_ssn = ssn[:index_of_dash + 1]

result = first_ssn + "*" * len_last_ssn
print(result)

# 도전!) 이메일에서 아이디만 추출
# 조건) 아이디가 바뀌더라도 아이디만 추출
# find, "@", 슬라이싱
email = "python-man2222@py.com"
# 1. "@"의 index를 찾는다
index_of_at = email.find("@")

# 2. 처음부터 @의 index미만까지 슬라이싱
username = email[:index_of_at]
print(username)