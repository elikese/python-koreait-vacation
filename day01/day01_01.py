print("Hello World!")
# 주석: 컴퓨터가 아닌 사람이 읽도록 작성한 메모
# 코드는 위에서 아래로 실행된다.
print("World Hello!")

# 변수
# "=" 은 같다는 의미가 아님
# 우변에 있는 데이터를 좌변에 대입
# 문자데이터 -> ""안에 작성
name = "홍길동"
age = 25

# 콘솔에 내용을 출력하는 기능
# 변수를 출력하면, 변수가 가지고 있는 데이터 출력
print(name)
print(age)

# 재사용성
greet = "world"
print(greet) # ctrl + D -> 해당줄 복사
print(greet)
print(greet)

greet = "hello" # 재 대입
# 이전값을 덮어쓰게 됨
print(greet)

# 변수의 작명방식
# 1. 변수는 띄어쓰기 x
# 스네이크 명명법: my_name
# 파스칼 명명법: myName
# 2. 예약어 사용 x
# 이미 문법키워드인 단어는 변수사용x

# 파이썬의 기본자료형
name = "홍길동" # 문자열 - str
age = 25 # 정수 - int
pi = 3.14 # 실수 - float
isMale = True # 불 - bool

# type(데이터)
# -> 해당데이터의 자료형이 문자로 제공됨
print(type(pi))

# 입력 - input(문자열)
# 1. 문자열이 먼저 출력됨
# 2. 콘솔에 데이터 입력 + 엔터 ->
# 주의) 엔터칠때까지 해당 코드라인에서 정지
# my_data = input("아무거나 입력 >")
# print(my_data)

# name 변수에 이름을 입력받아보세요
# 이름을 출력시켜 보세요!
name = input("이름 >>")

# 문자열끼리 더하면 이어붙는다.
print("제 이름은 " + name + "입니다.")








