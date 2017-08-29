import requests
from bs4 import BeautifulSoup
import browsercookie
import re
from watch_these.get_subs import get_sub_list

sub_list = get_sub_list('../watch_these/subs.txt')
my_headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Language': 'en-US'}
cj = browsercookie.firefox()
r = requests.get("https://www.youtube.com/feed/subscriptions", headers=my_headers, cookies=cj)
soup = BeautifulSoup(r.text, "lxml")
urls = []
video_titles = []
new_video_channels = []
container = soup.find('div', class_="feed-item-container browse-list-item-container yt-section-hover-container compact-shelf shelf-item branded-page-box vve-check clearfix ")
for video in container.findAll('div', class_='yt-lockup-content'):
    try:
        channel = video.find('a', href=re.compile('.*/user/.*'))
        channel_name = channel.text
        print(channel_name)
    except AttributeError:
        channel = video.find('a', href=re.compile('.*/channel/.*'))
        channel_name = channel.text
        print(channel_name)
    '''
    try:
        channel_link = video.find('a', href=re.compile('.*/user/.*')).attrs['href']
    except AttributeError:
        channel_link = video.find('a', href=re.compile('.*/channel/.*')).attrs['href']
    print(channel_link)
    channel = channel_link[6:]
    '''

    if channel_name in sub_list:
        video_link_object = video.find('a', href=re.compile('/watch\?.*'))
        video_name = video_link_object.text
        video_titles.append(video_name)
        video_url = "https://www.youtube.com/" + video_link_object.attrs['href']
        urls.append(video_url)
        new_video_channels.append(channel_name)

print(urls)
print(set(new_video_channels))
print(video_titles)
