import requests
import json

from bs4 import BeautifulSoup


class GuitarTab:

    main_link = "https://tabs.ultimate-guitar.com/tab/"

    def __init__(self, link):
        self.link = link

        # getting html from link
        self.page = requests.get(self.link)
        self.link_html = BeautifulSoup(self.page.text, "lxml")

        # parsing through html for json data
        self.div = self.link_html.body.find("div", class_="js-store")
        self.div_attrs = self.div.attrs
        self.json_data = self.div_attrs["data-content"]
        self.json_obj = json.loads(self.json_data)

        self.song_title = self.json_obj["store"]["page"]["data"]["tab"]["song_name"]
        self.song_artist = self.json_obj["store"]["page"]["data"]["tab"]["artist_name"]
        self.title = self.song_title + " chords by " + self.song_artist
        self.version = self.json_obj["store"]["page"]["data"]["tab"]["version"]
        self.author = self.json_obj["store"]["page"]["data"]["tab"]["username"]

        # TAB METADATA (with possibilities of not existing)
        if "difficulty" in self.json_obj["store"]["page"]["data"]["tab_view"]["meta"].keys():
            self.difficulty = self.json_obj["store"]["page"]["data"]["tab_view"]["meta"]["difficulty"]
        else:
            self.difficulty = None

        if "tuning" in self.json_obj["store"]["page"]["data"]["tab_view"]["meta"].keys():
            self.tuning = self.json_obj["store"]["page"]["data"]["tab_view"]["meta"]["tuning"]["value"]
        else:
            self.tuning = None

        if "capo" in self.json_obj["store"]["page"]["data"]["tab_view"]["meta"].keys():
            self.capo = self.json_obj["store"]["page"]["data"]["tab_view"]["meta"]["capo"]
        else:
            self.capo = None

        if "tonality" in self.json_obj["store"]["page"]["data"]["tab_view"]["meta"].keys():
            self.key = self.json_obj["store"]["page"]["data"]["tab_view"]["meta"]["tonality"]
        else:
            self.key = None
        # ------

        # TODO: how do you show strumming and chords?
        self.chords = None

        if len(self.json_obj["store"]["page"]["data"]["tab_view"]["strummings"]) != 0:
            self.strumming = self.json_obj["store"]["page"]["data"]["tab_view"]["strummings"]
        else:
            self.strumming = None

        self.tab = self.json_obj["store"]["page"]["data"]["tab_view"]["wiki_tab"]["content"]

    def get_clean_tab(self):
        self.tab = self.tab.replace("[tab]", "")
        self.tab = self.tab.replace("[/tab]", "")
        self.tab = self.tab.replace("[ch]", "")
        self.tab = self.tab.replace("[/ch]", "")

        return self.tab

    def show_info(self):
        print(self.title)
        print(f"Ver. {str(self.version)}")
        print()
        print(f"Difficulty: {self.difficulty}")
        print(f"Tuning: {self.tuning}")
        print(f"Capo: {str(self.capo)}")
        print(f"Key: {self.key}")
        print()
        print("Strumming: ")
        print(f"{self.strumming}")
        print("Chords:")
        print(f"{self.chords}")
        print()
        print(self.get_clean_tab())

    def transpose_to(self):
        pass

    def download_to(self):
        pass