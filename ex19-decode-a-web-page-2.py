import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")
a = soup.find_all("p")
for e in a:
    print(e.text)