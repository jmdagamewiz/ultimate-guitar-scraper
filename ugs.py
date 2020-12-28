import json

import input
import scraper
import tabs
import docx_handler

# hides traceback for better user experience
import sys
sys.tracebacklimit = 0

# save as .exe file and put to C:\Windows\System32 for use in cmd

def main():
    link = input.get_link()

    try:
        title, json_string = scraper.scrape(link)

        json_obj = json.loads(json_string)

        tab_content = json_obj["store"]["page"]["data"]["tab_view"]["wiki_tab"]["content"]
        cleaned_tab = tabs.clean_tab(tab_content)

        docx_handler.write_to_doc(title, cleaned_tab)

    except KeyError:
        print("Must be valid ultimate guitar link.")


if __name__ == "__main__":
    main()
