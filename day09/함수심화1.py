# 매개변수에 기본값을 할당할 수 있음
def hello(name, nationality="대한민국"):
    print(f"[{nationality}] {name}님 안녕하세요")

# 호출시 매개변수 전부 전달
hello("james", "미국")
# 기본값 설정이 되어있다면, 생략시 기본값 사용
hello("홍길동")

# 파이썬은 매개변수 전달시, 데이터의 순서로 구분
# -> 기본값설정된 매개변수가 나중 순서로 와야한다.

# print함수는 매개변수 갯수가 변해도
# 모두 실행가능 -> *args 패킹
print(1,2,3,4,5,6,7,8,9)

# *args 패킹
# 여러개로 들어온 매개변수를
# 하나의 tuple에 담아 가져온다
def args_ex(*a):
    # 변수앞에 *을 붙혀준다
    # 매개변수명이 *a아니고, a임
    print(a)
    print(type(a))

args_ex(1, 2, 3)

def calc_avg(*numbers):
    num_sum = 0
    for num in numbers:
        num_sum += num
    avg = num_sum / len(numbers)
    return avg

calc_avg(10, 20, 50, 80, 90)

# **kwargs 패킹
# 여러 매개변수를 dict로 포장해서 가져온다
def kwargs_ex(**k):
    print(k)
    print(type(k))

# {a:1, b:2}로 포장되어 매개변수로 전달됨
kwargs_ex(a=1, b=2)

def make_user(username, password, **details):
    user = {
        "username": username,
        "password": password,
    }
    # 옵션으로 입력한 정보는 user마다 다르지만
    # 모두 업데이트해줘야 한다
    # {"job": "학생", "hobby": "독서"}
    user.update(details)
    return user

user1 = make_user("pyman"
          , "123123"
          , job="사무직"
          , hobby="축구"
          )

user2 = make_user("javaman"
          , "456456"
          , hobby="만화책보기"
          )

print(user1)
print(user2)