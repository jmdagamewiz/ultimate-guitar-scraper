import input
import scraper


def main():
    link = input.get_input()
    scraper.scrape(link)


if __name__ == "__main__":
    main()
