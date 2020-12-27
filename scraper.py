import requests
from bs4 import BeautifulSoup


def scrape(link):
    # accepts ultimate guitar link and returns json

    page = requests.get(link)
    html = BeautifulSoup(page.text, "lxml")

    title = html.title.text
    title = title.replace(" CHORDS", "")
    title = title.replace(" @ Ultimate-Guitar.Com", "")
    print(title)

    div = html.body.find("div", class_="js-store")
    div_attrs = div.attrs

    # data-content attribute of div contains JSON text
    # which contains the tab
    json_data = div_attrs["data-content"]

    return [title, json_data]

