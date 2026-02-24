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

# 지역의 현재 온도를 네이버검색을 통해 파이썬으로 출력해주세요
local_list = ["부산", "대구", "대전"]

weathers = []
# [["부산", "9.3"],[],[],[]]

for local in local_list:
    driver.get(url)
    sleep(2)

    input_tag = driver.find_element(By.CSS_SELECTOR, "#query")
    input_tag.send_keys(f"{local} 날씨")
    sleep(0.5)

    btn_tag = driver.find_element(By.CSS_SELECTOR, "#sform > fieldset > button")
    btn_tag.click()
    sleep(2)

    temp_tag = driver.find_element(By.CSS_SELECTOR, "#main_pack > section > div > div:nth-child(1) > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.weather_graphic > div.temperature_text > strong")
    temperature = temp_tag.text.strip()[5:]
    temperature = temperature.strip()
    weathers.append([local, temperature])
    print(f"현재 {local}: {temperature}")

driver.quit() # 셀레니움 종료

# 크롤링한 날씨를 엑셀파일로 만들어주세요
# 엑셀파일이름: "weather_20260224.xlsx"
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "크롤링날씨"

header = ["지역", "현재기온"]
ws.append(header)
for weather in weathers:
    ws.append(weather)

wb.save("./weather_20260224.xlsx")
print("엑셀 저장완료!")