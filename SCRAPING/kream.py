from selenium import webdriver
from bs4 import BeautifulSoup

#셀레니움에 다양한 옵션을 적용시키기 위한 패키지
from selenium.webdriver.chrome.options import Options

#클래스, 아이디를 CSS_SELECTOR을 이용하기 위한 패키지
from selenium.webdriver.common.by import By
#키보드의 입력 형태를 코드로 작성하기 위한 패키지
from selenium.webdriver.common.keys import Keys

import time

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

options_ = Options()
options_.add_argument(f'User_Agent={user}')
options_.add_experimental_option("detach", True) #자동으로 꺼지지 않음
options_.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options_)

url = "https://kream.co.kr/"
driver.get(url)
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("나이키")
time.sleep(0.3)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(0.5)

for i in range(20):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)
    
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".product_card")

for item in items:
    product_name = item.select_one(".translated_name").text
    #print(product_name)
    if "후드" in product_name:
        category = "상의"
        product_name
