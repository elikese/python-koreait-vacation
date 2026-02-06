# 파일입출력.py
# 컴퓨터와 데이터
# cpu: 데이터 연산만
# ram: 단기 기억
# HDD, SSD: 장기 기억

# 파이썬을 통해서 file(장기기억)을 하게 만들 수 있음
# open(파일경로, 파일모드, 인코딩) -> 설정
file = open("./example.txt", "w", encoding="utf-8")
file.write("Hello world!")
file.close()
"""
- 파일경로
1. 절대경로(드라이브부터 실제 파일위치까지)
C:\\python-koreait-vacation\\day10\\파일입출력.py
2. 상대경로(../, ./)
./: 현재파일이 속한 폴더
../: 현재파일위치에서 한단계 상위 폴더

파일입출력.py에서 day08_01.py에 접근하는 상대경로
../day08/day08_01.py

- 파일모드
r: read - 파일 읽어오겠다
w: write - 파일 만들겠다

- 인코딩
컴퓨터는 숫자만 알아 들음
문자들을 숫자로 바꿔줘야 한다
-> 이때 필요한 규칙(인코딩)
euc-kr(관공서), cp949(정부문서), utf-8(웹표준)
"""

# 파일 읽기
file = open("./example.txt", "r", encoding="utf-8")
my_txt = file.read()
print(my_txt)
file.close()

def read_file(path):
    file = open(path, "r", encoding="utf-8")
    txt = file.read()
    file.close()
    return txt

# test.txt, test2.txt를 찾아서 읽고 출력
test_path = "../day05/test.txt"
test2_path = "../day01/box/test2.txt"

test_txt = read_file(test_path)
test2_txt = read_file(test2_path)

print(test_txt)
print(test2_txt)

# "w" 모드는 덮어쓰기
# "a": append 모드는 이어쓰기
file = open("./example.txt", "a", encoding="utf-8")
# \n : 엔터
file.write("\n덮어씌워 지나요2222?")
file.close()

