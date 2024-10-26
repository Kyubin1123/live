from selenium import webdriver
from bs4 import BeautifulSoup
import time

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 입력해주세요 : ")
url = base_url + keyword

#크롬 버전으로 자동으로 찾아서 프로그램을 연결시켜줌
driver = webdriver.Chrome() 
driver.get(url)
time.sleep(2)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".view_wrap")

for rank, i in enumerate(results, 1) :
    title = i.select_one(".title_link").text
    writer = i.select_one(".name").text
    
    print(f'[순번] : {rank}')
    print(f'제목 : {title}')
    print(f'작성자 : {writer}')
    print()