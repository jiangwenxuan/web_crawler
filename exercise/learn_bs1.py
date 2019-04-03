import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
r = requests.get(link, headers = headers)

soup = BeautifulSoup(r.text, "html.parser")
first_title = soup.find("h1", class_="post-title").a.text.strip()
print("the first title: ", first_title)

title_list = soup.find_all("h1", class_="post-title")
for i in range(len(title_list)):
    title = title_list[i].a.text.strip()
    print("the %s title is: %s" %(i+1, title))