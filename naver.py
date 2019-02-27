import requests
from bs4 import BeautifulSoup
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a.ah_a > span.ah_k

url="https://naver.com"
res=requests.get(url)
soup=BeautifulSoup(res.text, "html.parser")
#silgum=soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li > a.ah_a > span.ah_k")
silgum=soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li")
for s in silgum:
    n=s.select_one("a>span.ah_k")
    print(n.text)

#print(silgum)