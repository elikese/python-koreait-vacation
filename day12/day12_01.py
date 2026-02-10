# 객체지향 프로그래밍

# 은행계좌
# 예금 - 음수를 예금 할 수 없음
# 출금 - 잔액보다 더 출금 할 수 없음
class BankAccount:
    def __init__(self, ac_id, name):
        self.balance = 0 # 모든 계좌객체는 생성시 0원
        self.ac_id = ac_id
        self.name = name

    # 잔액확인
    def check_balance(self):
        print(f"{self.name}님의 계좌잔액: {self.balance}")

    # 예금
    def deposit(self, amount):
        if amount < 0:
            print("예금액은 음수일 수 없습니다")
            return

        self.balance += amount

    # 출금
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"잔액부족, 현재잔액: {self.balance}")
            return

        self.balance -= amount

acc1 = BankAccount("기업001", "고길동")
acc2 = BankAccount("농협001", "둘리")

acc1.deposit(10000)
acc2.deposit(5000)

# 같은 함수를 호출 하지만, 객체가 가지고있는 데이터에 따라
# 서로 다르게 동작
acc1.withdraw(7000)
acc2.withdraw(7000)
acc1.check_balance()
acc2.check_balance() # 출금되지 않았음 - 의도된 동작


# 물컵 클래스
# fill(self, amount) - water에 amount만큼 더하는데,
# # 최대 사이즈넘기면x
# # drink(self, amount) - 현재 water보다 더 마실 수 없음
# check(self)
class Cup:
    def __init__(self, size):
        if size <= 0:
            print("사이즈는 양의 정수여야합니다")
            return

        # self._어쩌고 필드
        self._maker = "다이소"
        self.size = size # 최대용량
        self.water = 0 # 현재 물의 양


    def fill(self, amount):
        # amount만큼 물을 채우면
        # water의 양이 size를 넘어갈까?
        if self.water + amount > self.size:
            print("물이 넘칩니다")
            return

        self.water += amount

    def drink(self, amount):
        # amount가 water보다 크면 모자랄까?
        if amount > self.water:
            print("물이 부족합니다")
            return
        self.water -= amount

cup1 = Cup(500)
cup1.fill(400)
cup1.drink(450)

# 파이썬에서는 객체에 필드를 임의로 추가할 수 있음
cup1.anything = "아무거나"
print(cup1.anything) # 클래스에 정의되어 있지 않음
print(cup1.water)
print(cup1.size)
# 필드명 앞에 '_' 붙히면 .으로 접근시 경고
print(cup1._maker)

a = "10"
a = int(a)

# isinstance(데이터, class)
# 데이터가 class로부터 만들어진 객체냐?
# 맞으면 True, 아니면 False를 리턴

print(isinstance(a, int)) # a가 int 객체?
print(isinstance(a, str)) # a가 str 객체?
print(isinstance(cup1, Cup)) # cup1이 Cup객체?
