import requests
from bs4 import BeautifulSoup

# 타겟 인터넷주소 지정(url)
url = "https://quotes.toscrape.com"

# requests로 인터넷통신
response = requests.get(url)
# print(response.text) # HTML골격을 문자열로 가져온다

# 가져온 HTML텍스트를 파이썬객체로 변환
# 태그하나를 파이썬객체 하나로 변환
html = BeautifulSoup(response.text, "html.parser")


# html태그 안에 div태그이면서 클래스속성값이 quote인 태그
first_quote_tag = html.find("div", class_="quote")
print(first_quote_tag.text)

# first_quote_tag안에 span태그이면서, 클래스속성값이 text인 태그
quote_text_tag = first_quote_tag.find("span", class_="text")

# 그 태그가 가진 텍스트
quote_text = quote_text_tag.text
print(quote_text)

# 도전!!!) Albert Einstein을 html부터 시작해서 추출해 주세요!
# 위에서 읽었을때 타겟태그가 제일 먼저 등장할거다라는 가정
author_text = html.find("small", class_="author").text
print("아인슈타인? ", author_text)