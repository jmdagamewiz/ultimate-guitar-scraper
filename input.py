import argparse


def get_link():

    parser = argparse.ArgumentParser(description="ultimate guitar chords scraper")
    parser.add_argument("link", help="ultimate guitar page link")

    args = parser.parse_args()

    ug_link = "https://tabs.ultimate-guitar.com/tab/"

    # checks if link from ultimate guitar site
    if ug_link in args.link:
        return args.link
    else:
        raise Exception("Must be valid ultimate guitar link.")
