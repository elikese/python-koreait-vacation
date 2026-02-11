# 클래스 변수
# 클래스내부에도 데이터를 저장할 수 있음
# 해당 클래스 객체들이 모두 공유가능

class Student:
    # 클래스변수
    school_name = "파이썬 대학교"
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1
        if Student.count > 3:
            print("정원초과! 현재 3명")
            return # 예외(에러)를 발생시켜야함


st1 = Student("김학생")
st2 = Student("최학생")

# 객체로 클래스변수 읽기
print(st1.school_name)
print(st2.school_name)

# 클래스로 클래스변수 읽기
print(Student.school_name)

st1.age = 21 # 임의로 필드추가 ok
# 임의로 필드추가가 된것이지, 클래스변수 수정x
st1.school_name = "자바 대학교"

print(st1.school_name) # 필드 조회
print(st2.school_name) # 클래스 변수 조회
print(Student.school_name)

# 수정하려면 클래스로 접근해야 수정가능
Student.school_name = "자바 대학교"

# 번호표를 생성할때마다 num이 1씩 증가되서
# 생성되게끔 코드를 작성해 주세요. - 클래스변수 활용
class NumberTicket:
    count = 0
    def __init__(self):
        NumberTicket.count += 1
        self.num = NumberTicket.count
        print(f"{self.num}번 번호표 발급완료")

NumberTicket()
NumberTicket()
NumberTicket()
