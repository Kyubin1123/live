import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "http://www.cgv.co.kr/movies/?It=1&ft=0"
req = requests.get(url, headers = header_user)
html = req.text
soup = BeautifulSoup(html, "html.parser")

for d_day in soup.select(".dday"):
    d_day.decompose()

results = soup.select(".box-contents")

for rank, i in enumerate(results, 1):
    title = i.select_one(".title").text
    reserve = i.select_one(".percent").text.replace("예매율", "").strip()
    release_info = i.select_one(".txt-info").text.replace("재개봉", "").strip()
    
    release_date = release_info.replace("개봉", "").strip()
    
    print(f'[순위] {rank}')
    print(f'제목 : {title}')
    print(f'예매율 : {reserve}')
    print(f'개봉일자 : {release_date}')
    print()
    
    