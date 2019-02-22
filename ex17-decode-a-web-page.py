import requests
from bs4 import BeautifulSoup

r = requests.get("https://en.wikipedia.org/wiki/Main_Page")
data = r.text
soup = BeautifulSoup(data, "lxml")

articles = soup.find_all(class_ = 'mw-jump-link')
for title in articles:
    h = str(title.string).strip()
    if h != 'None':
        print(h)
