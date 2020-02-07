from bs4 import BeautifulSoup
import urllib.request


def search_spider():
    url = "https://en.wikipedia.org/wiki/Deep_learning"
    source_code = urllib.request.urlopen(url)
    plain_text = source_code
    soup = BeautifulSoup(plain_text, "html.parser")
    title = soup.find('title')
    result = soup.findAll('a')
    print(title)
    print(result)
    for a in result:
        link = a.get('href')
        print(link)


search_spider()
