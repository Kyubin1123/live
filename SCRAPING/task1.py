import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input ("검색어를 입력해 주세요 : ")

url = base_url + keyword
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".view_wrap")

for i in results:
    if not i.select_one(".link_ad"):
        title = i.select_one(".title_link").text
        writer = i.select_one(".name").text
        
    print(f'검색 키워드 : {keyword}')
    print(f'블로그 제목 : {title}')
    print(f'블로그 작성자 : {writer}')
    print()