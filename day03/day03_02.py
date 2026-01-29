# input()으로 들어온 데이터는 모두 문자열
# (자료)형변환
str_num = "123" # 문자열
int_num = int(str_num) # str -> int
# print(str_num + 100) # 에러
int_num2 = int(11.0) # float -> int
str_num2 = str(110) # int -> str

# bool자료형 형변환
print(bool("손흥민"))
print(bool(1000))
# bool 형변환시 False 케이스
print(bool(""))
print(bool(0))
print(bool([])) # 비어있는 list,tuple,dict,set
# if 뒤에 bool이 아닌 값이오면 자동형변환

# 상품의 가격을 입력받고
# 가격이 10만원 이상 -> 10프로 할인한 가격(*0.9)
# 가격이 10만원 미만 -> 원래 입력한 가격
# 출력!
input_price = input("가격 입력 >")
price = int(input_price) # str -> int
discount = price * 0.9
discount_cut = 100000

final_price = discount if price >= discount_cut else price



