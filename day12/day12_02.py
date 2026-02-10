# isinstance 활용

# 시험성적표
class TestScore:
    def __init__(self, name, kor, eng, math):
        # 이름이 문자열이 아니라면
        if not isinstance(name, str):
            print("이름은 문자여야합니다")
            return

        # 국영수 점수는 정수(int)
        # 0 ~ 100 사잇값
        # 국영수 점수 모두 동일한 코드 실행
        for score in [kor, eng, math]:
            if not isinstance(score, int):
                print("점수는 숫자여야 합니다")
                return

            if not (0 <= score <= 100):
                print("점수는 0~100 범위에 있어야합니다")
                return
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    # 국영수 점수의 평균값을 리턴하는 함수
    def get_average(self):
        avg = (self.kor + self.eng + self.math) / 3
        return avg

    # 평균점수가 90이상이면 장학금 대상입니다! 출력
    # 학교이름도 같이 출력, 학교이름이 str객체인지 검사
    def print_scholar(self, school_name):
        # 함수내에서 자기자신의 또다른 함수를 호출
        avg = self.get_average()
        if not isinstance(school_name, str):
            print("학교이름은 문자여야 합니다")
            return

        # 평균점수 90이상일때
        if avg >= 90:
            print(f"{school_name}: 장학금대상입니다!")
        else:
            print(f"장학금대상이 아닙니다 평균: {avg}점")


scores1 = TestScore("철수", 100, 90, 90)
# scores2는 생성 불가
scores2 = TestScore("이상한", -100, 999, 1.1)

scores1.print_scholar("부산대학교")
isinstance(scores1, TestScore) # True / False
print(type(scores1)) # 문자열로 표현