import json

import input
import scraper
import tabs
import docx_handler


# TODO: put to .docx file using python-docx module
# TODO: have more error handling capacity
# TODO: update requirements.txt


def main():
    link = input.get_link()

    ug_link = "https://tabs.ultimate-guitar.com/tab/"

    json_string = "{}"
    title = "default_title"

    # checks if link from ultimate guitar site
    if ug_link in link:
        # TODO: fix this pls...
        title, json_string = scraper.scrape(link)

    json_obj = json.loads(json_string)

    tab_content = json_obj["store"]["page"]["data"]["tab_view"]["wiki_tab"]["content"]
    cleaned_tab = tabs.clean_tab(tab_content)

    docx_handler.write_to_doc(title, cleaned_tab)


if __name__ == "__main__":
    main()
