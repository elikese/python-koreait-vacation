# with ~ as 문법
# 자원반납이 코드실행 후 꼭 필요한경우

# file = open()
with open("./example.txt", "w", encoding="utf-8") as f:
    # with ~ as 사용하면, 들여쓰기가 끝나면 자동 자원반납
    # 에러가 발생하더라도 자동반납
    # as 변수 -> 대입받을 변수
    f.write("Hello world!")

# python자료형들을 저장할 파일형식
# [{},{}...{}] 이런경우 -> txt는 표현에 한계존재
# 참고) csv, xml...
# 현대 표준 - JSON 파일형식 (데이터를 주고받는 형식)
"""
[
    {
        "name": "홍길동",
        "age": 30
    },
    {
        "name": "김길동",
        "age": 33
    }
]
"""

# json을 파이썬에서 다루는법
import json # 코드 빌려오기

dict_data = {
    "name": "홍길동",
    "age": 30,
    "address": "부산시"
}

# json 쓰기
with open("./data.json", "w", encoding="utf-8") as f:
    # dump(파이썬데이터, f(파일변수), 아스키, 들여쓰기)
    # 아스키: 한글이 포함되면 False로 지정
    # 들여쓰기: 4칸 들여써라
    json.dump(
        dict_data,
        f,
        ensure_ascii=False,
        indent=4
    )

# json 파일 읽기
with open("./data.json", "r", encoding="utf-8") as f:
    read_json = json.load(f)
    # 파일에서 읽어온 json을 알아서 파이썬데이터로 변환
    print(read_json)

# json 파일 수정 - 덮어쓰기
with open("./data.json", "w", encoding="utf-8") as f:
    read_json.update({
        "age": 31
    })
    json.dump(read_json, f, ensure_ascii=False, indent=4)

# menu.json 파일을 파이썬으로 불러와서
# 오뎅 2000원 추가, 라면 5500원으로 인상하여
# 다시 menu.json으로 저장하여 주세요

# menu.json파일을 파이썬으로 불러오기
# 함수로 내가 작성할 것만 매개변수로 작성
# json 불러오기 함수
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        read_data = json.load(f)
        return read_data

# json 저장하기 함수
def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

menu_data = load_json("./menu.json")
print(menu_data)
menu_data.update({
    "라면": 5500,
    "오뎅": 2000
})
save_json("./menu.json", menu_data)

save_json("./nums.json", [1,2,3,4,5])