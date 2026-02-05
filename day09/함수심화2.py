# 고차함수: 매개변수로 함수를 전달받음
def calc(x, y, fn):
    result = fn(x, y)
    return result
# 콜백함수: 매개변수로 전달되는 함수
def plus(x, y):
    return x + y
# 람다함수: 이름이 없는 익명함수
lambda_add = lambda x, y: x + y

# 도전) 두수를 받아서 제곱해서 더하는 콜백함수
# calc함수에 매개변수로 넘겨서 최종결과를 리턴받아 출력
# 도전2) square_add를 람다로 작성
# calc 함수 매개변수에 람다작성
def square_add(x, y):
    return x**2 + y**2

# 고차함수 호출
result1 = calc(10, 20, plus)
result3 = calc(10, 20, lambda x, y: x + y)
print(result1)
result2 = calc(2, 3, square_add)
print(result2)
result4 = calc(2, 3, lambda x, y: x**2 + y**2)
print(result4)

# 람다함수와 자주사용되는 파이썬내장 고차함수
# 1. filter(콜백함수, 리스트)
# 리스트에서 콜백함수 결과가 True인 요소만 남겨줌
nums = [1,2,3,4,5,6]
filter(lambda n: n % 2 == 0,nums)

