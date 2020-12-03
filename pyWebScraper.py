from urllib import request
from bs4 import BeautifulSoup

def scraping():
    # url
    url = "http://www.yomiuri.co.jp/"

    # get html
    html = request.urlopen(url)

    # set BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # get headlines
    headlines = soup.find_all("h3", class_="c-list-title")

    # print headlines
    for headline in headlines:
        print(headline.contents[0], headline.a.string)


if __name__ == "__main__":
    scraping()
