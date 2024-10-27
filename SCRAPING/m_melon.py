from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

user = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

options_ = Options()
options_.add_argument(f"user-agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])

service_ = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_, options=options_)

url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".link-logo").click()
time.sleep(1)

nav_items = driver.find_elements(By.CSS_SELECTOR, ".nav_item")
for item in nav_items:
    if "멜론차트" in item.text:
        item.click()
        break
time.sleep(1)

driver.find_element(By.XPATH, '//button[@onclick = "hasMore2();"]').click()
time.sleep(0.5)

soup = BeautifulSoup(driver.page_source, "html.parser")
results = soup.select_one("#_chartList")
lst = results.select(".list_item")
for i in lst:
    rank = i.select_one(".ranking_num").text
    title = i.select_one(".title.ellipsis").text.lstrip().rstrip()
    name = i.select_one(".name.ellipsis").text
    
    print('순위 : '+ rank)
    print('제목 : '+ title)
    print('가수 : '+ name)
    print()
    
    driver.quit()