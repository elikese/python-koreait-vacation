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

# 람다함수와 자주사용되는 파이썬내장 고차 함수
# 1. filter(콜백함수, 리스트)
# 리스트에서 콜백함수 결과가 True인 요소만 남겨줌
nums = [1,2,3,4,5,6]

res1 = filter(lambda n: n % 2 == 0, nums)
# 필터 결과는 리스트로 형변환
res1 = list(res1)
print(res1)

names = ["김철수", "박철수", "김길동", "최길동"]
# 김씨만 남겨달라
res2 = list(filter(lambda name: name.startswith("김"), names))
print(res2)


# 2. map(요소 조작 함수, 리스트)
nums = [1, 2, 3, 4, 5, 6]
res3 = list(map(lambda n: n**2, nums))
str_nums = ["1", "2", "3", "4"]
res4 = list(map(int, str_nums))
print(res4[0] + 1) # 2?

# 도전) 모든 이름뒤에 고객님 붙히기
# ex) 김철수 -> 김철수고객님
names = ["김철수", "박철수", "김길동", "최길동"]
res5 = map(lambda name: f"{name}고객님", names)
# 3. sorted - 정렬
nums = [30, 55, 1, 4, 11]
# 숫자 -> 오름차순으로 정렬 1 4 11...55
sorted_nums = sorted(nums)
print(sorted_nums)

words = ["banana", "apple", "applepie"]
# 문자 -> 사전순으로 정렬된 결과
sorted_words = sorted(words)
print(sorted_words)

# 기본동작: 작은게 앞으로
# 각 숫자들에 -1 곱한걸 기준으로 정렬해라
desc_nums = sorted(nums, key=lambda n: -1 * n)

# 글자길이가 긴 것이 먼저오게
# 기본동작: 작은게 앞으로
words = ["banana", "apple", "applepie"]
res6 = sorted(words, key=lambda w: -len(w))

# 4. max, min
nums = [30, 55, 1, 5]
max(nums) # 55 -> 가장 큰 숫자
min(nums) # 1 -> 가장 작은 숫자
words = ["banana", "apple", "applepie"]
# 가장 긴 이름
longest_word = max(words, key=lambda w: len(w))

# 도전) max를 사용하여 점수가 가장 높은 사람의 이름을 출력
scores = [
    {"name": "홍길동", "score": 90, "age": 20},
    {"name": "김영희", "score": 90, "age": 22},
    {"name": "최철수", "score": 40, "age": 18},
]

highest_score = max(scores, key=lambda s: s["score"])
print(highest_score["name"])

# 동률처리 - max,min,sorted 모두 동일
# 높은점수인데 동률이면 나이가 많은 사람이름
highest_score_age = max(
    scores,
    # 리턴에 튜플로 적용될 값의 우선순위를 지정가능
    key=lambda s: (s["score"], s["age"])
    )

print(highest_score_age["name"])