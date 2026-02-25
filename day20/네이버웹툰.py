from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

url = "https://www.naver.com"
# 파이썬이 내 pc를 사용해서 브라우저를 열고 행동
# 크롬 설치파일 가져오기
driver_manager = ChromeDriverManager().install()
# 셀레니움에 설치
chrome_service = Service(driver_manager)
# 인터넷 창(브라우저) 생성
driver = webdriver.Chrome(service=chrome_service)

def scroll_to(tag):
    script = "arguments[0].scrollIntoView();"
    driver.execute_script(script, tag)


driver.get(url) # 접속
sleep(1.5)

# a태그 - 링크를 가지고있음
webtoon_home_link = driver.find_element(By.CSS_SELECTOR, "#shortcutArea > ul > li:nth-child(9) > a")

# 새창이 열리는 경우에는 get()으로 이동하는게 수월하다
# 같은 페이지에서 이동 -> click()
webtoon_home_url = webtoon_home_link.get_attribute("href")


driver.get(webtoon_home_url) # 재이동
sleep(1.5)

webtoon_menu = driver.find_element(By.CSS_SELECTOR, "#menu > li:nth-child(2) > a")
webtoon_menu.click()
sleep(1.5)

# 월 ~ 일 순서대로 클릭
# 메뉴바 추출
menu_bar = driver.find_element(By.CSS_SELECTOR, "#wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul")

# menu_bar태그에 속해있는 "li > a"들을 찾아야함
menus = menu_bar.find_elements(By.CSS_SELECTOR, "li > a")
menus = menus[1:8] # 월 ~ 일 필터링

for menu in menus:
    print(menu.text) # 월 ~ 일

