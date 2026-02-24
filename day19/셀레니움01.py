from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

url = "https://www.health.kr"

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

search_q = "아세트아미노펜"
drug_name_list = [
    "아세트아미노펜",
    "아로낙",
    "트라세트 세미정",
    "씨오엑스",
    "크리마인",
    "에페손"
]

for search_q in drug_name_list:
    # 접속
    driver.get(url)
    sleep(2) # 대기(로딩)

    # find_element() - 하나 찾기 -> 태그
    # find_elements() - 여러개 찾기 -> [태그,태그...]

    # 브라우저 copy selector로 찾기
    # 일반적으로 입력하는 태그는 <input> 이라는 태그
    # 일반적으로 클릭하는 태그는 <button> 이라는 태그
    search_input_tag = driver.find_element(By.CSS_SELECTOR, "#search_word")
    search_input_tag = driver.find_element(By.ID, "search_word")

    # 태그.send_keys("문자열") : 문자열 입력
    search_input_tag.send_keys(search_q)
    sleep(0.5)

    # 버튼
    search_btn_tag = driver.find_element(By.CSS_SELECTOR, "#searchBar > button.search")
    search_btn_tag.click() # 클릭

    # 새 페이지로 이동하게 되면, 로딩시간을 기다려준다
    sleep(3)

    try:
        drug_link_tag = driver.find_element(By.CSS_SELECTOR, "#tbl_proY > tbody > tr:nth-child(2) > td:nth-child(2)")
        drug_link_tag.click()

        sleep(3)
    except Exception as e:
        print("    -> 검색결과 없습니다. 다음으로 넘어갑니다")
        continue
    else:
        # 효능 효과
        effect_tag = driver.find_element(By.ID, "efficacy_effect")
        scroll_to(effect_tag)
        effect_text = effect_tag.text.strip()
        print(f"효능 및 효과: {effect_text[10:]}")

        sleep(1)

        # 용법 용량
        usage_tag = driver.find_element(By.ID, "usage")
        scroll_to(usage_tag)
        usage_text = usage_tag.text.strip()
        print(f"용법 및 용량: {usage_text[10:]}")