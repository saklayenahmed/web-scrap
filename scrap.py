import requests
import os
from bs4  import BeautifulSoup

path = os.path.dirname(os.path.abspath(__file__))
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

text_file= open(path+'/saved.txt','w')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoateTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoateTags:
        all_text = quoteTag.text+"\n"
        text_file.write(all_text)
        print(all_text)
