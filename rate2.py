

import requests
from bs4 import BeautifulSoup

url="http://finance.daum.net/exchanges"
res=requests.get(url)
soup=BeautifulSoup(res.text, "html.parser")

country=soup.select("#boxContents > div.tableB > div.box_contents > div > table > tbody > tr")

print(country)

#boxContents > div.tableB > div.box_contents > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > a
#boxContents > div.tableB > div.box_contents > div > table > tbody > tr:nth-child(3) > td:nth-child(1) > a.
#boxContents > div.tableB > div.box_contents > div > table > tbody > tr.first > td.first
# for s in country:
#     a=s.select_one("td > a")
#     print(a.text)
    