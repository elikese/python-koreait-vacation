# 클래스 - 상속
# 두개 이상의 클래스가 공통코드가 많을때
# 상위(부모)클래스를 정의해서 묶어 줄 수 있음

class Pet:
    def __init__(self, name, age):
        print("Pet의 생성자 호출!")
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}가 밥을 먹습니다")

    def sleep(self):
        print(f"{self.name}가 잠듭니다")

# 클래스이름(상위클래스) - 상속
# Dog 클래스에 breed필드를 추가해주세요
class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f"{self.name}: 멍멍!")

    # 부모의 함수를 재정의 -> 부모의 함수는 가려짐
    # 오버라이딩
    # 권장) 함수이름, 매개변수 동일
    def eat(self):
        print(f"{self.name}가 사료를 먹습니다.")

# Dog클래스에는 생성자 없지만, 부모에 정의된걸 사용
dog1 = Dog("초코", 5, "리트리버")
dog1.eat() # 부모의 dog함수 호출

# MRO(method resolution order)
# 자식클래스 객체가 호출한 함수가 자식클래스에 없으면
# 파이썬은 부모클래스에 해당함수를 찾으러 감

# Pet을 상속받는 Cat 클래스 정의
# eat함수를 오버라이딩
# print(f"{self.name}가 캣잎을 먹어요")
class Cat(Pet):
    # 부모로부터 물려받은 필드말고
    # Cat만 가지는 필드는 어떻게 정의?
    def __init__(self, name, age, color):
        # super(): 부모의 함수를 호출하게 해주는 함수
        # super()는 self안에 super영역만 리턴하는 함수
        super().__init__(name, age)
        self.color = color

    def eat(self):
        print(f"{self.name}가 캣잎을 먹어요")

    def play(self):
        super().sleep() # 부모의 sleep()
        super().eat() # 부모의 eat()
        # 상속받은 자식 객체는 super(부모)영역이 구분되어있음
        # self는 super를 포함한다
        # 필드, 함수가 동일한경우,
        # 일반적인 조회, 호출 -> 자식
        # super() 명시하면 -> 부모


# isinstance와 상속
# self는 super를 포함한다
# -> 해당 클래스 정보가 포함되어 있냐?
result = isinstance(dog1, Pet)
print(f"dog1이 Pet클래스 출신? : {result}")



class Payment:
    def __init__(self):
        print("결제 시스템 초기화")

    def pay(self, price):
        pass

class Kakao(Payment):
    def pay(self, price):
        if price >= 15000:
            return price * 0.95

        return price

class Naver(Payment):
    def pay(self, price):
        if price >= 15000:
            return price - 1000

        return price

def order(price, payment):
    is_payment = isinstance(payment, Payment)
    if not is_payment:
        print("올바른 결제방식을 선택하십시오")
        return

    final_price = payment.pay(price)
    print(f"총 결제금액: {final_price}")


price = 20000
kakao = Kakao()
naver = Naver()

order(price, kakao)



