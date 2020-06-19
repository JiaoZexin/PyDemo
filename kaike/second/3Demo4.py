import requests;
from bs4 import BeautifulSoup;
res=requests.get('https://xiaoke.kaikeba.com/example/canteen/index.html');
html=res.text;
soup=BeautifulSoup(html,'html.parser')
print(soup)
items=soup.find_all(class_='item-description')
for item in items:
    title=item.find(class_='desc-title')
    description=item.find(class_='desc-step')
    print(title.text,description.text)