import requests
from bs4 import BeautifulSoup


def scrape(link):
    page = requests.get(link)
    html = BeautifulSoup(page.text, "lxml")

    title = html.title.text
    title = title.replace(" CHORDS", "")
    title = title.replace(" @ Ultimate-Guitar.Com", "")
    print(title)
