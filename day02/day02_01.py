# 문자열 기능들 - 2(가공)

# 1. 문자열.replace("바꾸고싶은 문자열", "대체될 문자열")
a = "my name is Son" # " " -> "_"
a_replace = a.replace(" ", "_")
a_replace2 = a.replace("Son", "") # 삭제

# 2. 문자열.strip(문자열패턴)
# 문자열처음과 끝에서 매칭되는 문자열패턴을 삭제
a = "  데이터  "
print(a)
a_strip = a.strip() # 문자열기준 좌우공백 제거
a = "**데이터**"
a_strip2 = a.strip("*") # 문자열기준 좌우 "*"들 제거

# 3. upper, lower - 알파벳을 모두 대문자 or 소문자
a = "Hello World"
a_upper = a.upper() # HELLO WORLD
a_lower = a.lower() # hello world

# 도전2) 문자열을 가공하여서
production = "**[SALE] Apple iphone 17 Pro**"
# "apple iphone 17 pro"로 변환시켜 주세요
# strip -> replace -> lower
first_result = production.strip("*")
print(first_result)
second_result = first_result.replace("[SALE] ", "")
print(second_result)
third_result = second_result.lower()
print(third_result)

# 문자열의 기능 ? 함수
# 문자열의 함수는 원본을 훼손하지 않는다.
# 언제나 새로운 값으로 가져온다
print(production)

# 함수의 결과가 값이면 값처럼 사용가능하다
result = production.strip("*").replace("[SALE] ", "").lower()
print(result)

# 문자열 기능들 3 - 검사: 결과로 bool자료형을 가져옴
# 1. startswith(문자열), endswith(문자열)
# 처음과 끝이 무엇인지 검사
email = "python@py.com"
# email에 담긴 값이 py로 시작하나요?
result = email.startswith("py")
print(result)
# email에 담긴 값이 .com으로 끝나나요?
result = email.endswith(".com")
print(result)

# in 연산자 - 존재여부 확인
# 문자열1 in 문자열2
# 문자열2에 문자열1이 포함되나요?
email = "python@py.com"
result = "py" in email
print(result)


