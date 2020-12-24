import input
import scraper


def main():
    link = input.get_link()

    ug_link = "https://tabs.ultimate-guitar.com/tab/"

    # checks if link from ultimate guitar site
    if ug_link in link:
        scraper.scrape(link)


if __name__ == "__main__":
    main()
