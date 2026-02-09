# 클래스
# 내가 직접 정의한 자료형

a = 10
b = "abc"
print(type(a))
print(type(b))

# 클래스의 첫글자는 대문자(관례)
class Puppy:
    # __init__(self, 내가 이 클래스에 넣고싶은 데이터들)
    # : 생성자(생성할때 호출되는 함수)
    def __init__(self, name, age):
        # self는 객체 자기 자신을 의미
        # self는 생성될때 할당받은 메모리공간
        # 임의로 name, age같은 저장공간을 만들 수 있음
        # -> 필드 or 멤버변수라고 말함
        self.name = name
        self.age = age
        print(f"{self.name}가 생성되었습니다")

    def bark(self):
        print(f"{self.name}가 짖습니다. 멍멍")
        # self를 통해 각 객체가 가지고 있는
        # 데이터에 따라 서로 다르게 동작할 수 있다.
        # 조건문을 통해 동작을 제한할 수 있다.

# 클래스이름(): 생성자 호출
# Puppy객체 생성
puppy1 = Puppy("초코", 5)
puppy2 = Puppy("뽀삐", 6)
puppy3 = Puppy("뽀삐", 6)
# 같은 데이터를 담더라도 서로 다른 객체다.

# 클래스는 설계도(틀, 양식)이다.
# 그 클래스로 생성된 것은 객체(인스턴스)이다.

# 클래스 내부에 있는 함수는
# 해당 클래스객체.함수()로 호출한다
# 호출한 객체가 self를 전달한다.
puppy1.bark()
puppy2.bark()

# Car 클래스를 작성해주세요
# 저장하는 데이터는 model, speed(현재속도)
# 내부에 drive라는 함수를 정의
# speed가 0 이상이면, {model}이 달립니다! 출력

class Car:
    # Car()작성시 호출됨
    def __init__(self, model, speed):
        # 검증하는 코드 작성
        if speed < 0:
            print("속력은 음수일 수 없습니다")
            return # 예외를 던져야한다. - 나중에

        self.model = model
        self.speed = speed

    def drive(self):
        if self.speed > 0:
            print(f"{self.model}가 달립니다!")
        else:
            print("현재 정지되어 있습니다")

    def brake(self):
        # Car 객체의 속력 감소
        self.speed -= 20
        # 속력이 음수가 될 수 있음
        if self.speed < 0:
            self.speed = 0
        # 객체가 저장한 값을 변경할 때
        # 검증된 값으로 보정할 수 있음

car1 = Car("소나타", 10)
car1.drive() # 호출

car2 = Car("아반떼", 0)
car2.drive()

# 객체지향 프로그래밍
# 객체에 데이터를 저장, 변경할때
# 안전하게 검증된 값만 저장하고 싶다.