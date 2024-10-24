import requests
from bs4 import BeautifulSoup
# 제발 좀 읽혔으면 좋겠는데 아직 파이썬과 플라스크가 모자라나봅니다..

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url="https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input ("검색어를 입력해주세요 : ")

url = base_url + keyword
req = requests.get(url)

html = req.text
soup = BeautifulSoup(html, "html.parser") #인스턴스화

results = soup.select(".view_wrap")

for i in results:
    
    if not i.select_one(".link_ad"): 
        title = i.select_one(".title_link").text
        link = i.select_one(".title_link")['href']
        writer = i.select_one(".name").text
        dsc = i.select_one(".dsc_link").text
    
        print(f'검색 키워드 : {keyword}')
        print(f'블로그 제목 : {title}')
        print(f'블로그 작성자 : {writer}')
        print()