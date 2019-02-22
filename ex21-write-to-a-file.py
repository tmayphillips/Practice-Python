import requests
from bs4 import BeautifulSoup

r = requests.get("https://en.wikipedia.org/wiki/Main_Page")
data = r.text
soup = BeautifulSoup(data, "lxml")

filename = input("File to save to: ")

with open(filename, 'w') as f:
  for jump_link in soup.find_all(class_="mw-jump-link"): 
      if jump_link.a: 
          f.write(jump_link.a.text.replace("\n", " ").strip())
      else: 
          f.write(jump_link.contents[0].strip())