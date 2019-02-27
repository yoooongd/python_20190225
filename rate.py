import requests
from bs4 import BeautifulSoup

url="https://search.naver.com/search.naver?query=환율"
res=requests.get(url)
soup=BeautifulSoup(res.text, "html.parser")
#current=soup.select_one("#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_bx > div.rate_spot._rate_spot > div.rate_tlt > h3 > a > span.spt_con.dw > strong")
#print(current.text)

country=soup.select("#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_table_bx._table > table > tbody > tr")


for s in country:
    a=s.select_one("th > a > span")
    b=s.select_one("td:nth-child(2) > span")
    print(a.text+":"+b.text)
    
