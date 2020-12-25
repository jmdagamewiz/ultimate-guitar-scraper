import json

import input
import scraper
import tabs


# TODO: put to .docx file using python-docx module
# TODO: have more error handling capacity


def main():
    link = input.get_link()

    ug_link = "https://tabs.ultimate-guitar.com/tab/"

    json_string = "{}"

    # checks if link from ultimate guitar site
    if ug_link in link:
        json_string = scraper.scrape(link)

    json_obj = json.loads(json_string)
    tab_content = json_obj["store"]["page"]["data"]["tab_view"]["wiki_tab"]["content"]
    cleaned_tab = tabs.clean_tab(tab_content)

    print(cleaned_tab)


if __name__ == "__main__":
    main()
