import requests
from bs4 import BeautifulSoup
import browsercookie
import re

my_headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Language': 'en-US'}
cj = browsercookie.firefox()
r = requests.get("https://www.youtube.com/feed/subscriptions", headers=my_headers, cookies=cj)
soup = BeautifulSoup(r.text, "lxml")
container = soup.find('div', class_="feed-item-container browse-list-item-container yt-section-hover-container compact-shelf shelf-item branded-page-box vve-check clearfix ")
for item in container.findAll('a', href=re.compile('.*/user/.*')):
    print(item)

