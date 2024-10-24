import requests
from bs4 import BeautifulSoup

# base_url = 

header_user = {"User-Agent" : "Mozilla/5.0 ()"}

url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html,"html.parser")

results = soup.select(".view_wrap")

for i in results:
    