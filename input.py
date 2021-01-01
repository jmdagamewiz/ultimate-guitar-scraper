import argparse


def get_link():

    # TODO: understand how to receive argument values without disrupting other arguments' values

    parser = argparse.ArgumentParser(description="ultimate guitar chords scraper")
    parser.add_argument("--UG_link", help="ultimate guitar page link")

    # TODO: can you even use nargs="+" if you have more than 1 argument in a program??????
    # TODO: how to get more than 1 value without the program thinking that the link is one of them??
    # EX. ugs --exclude title version author https://tabs.ultimate-guitar.com/tab/yeng-constantino/ikaw-chords-1694457
    # Program throws error saying LINK argument isn't given

    parser.add_argument("--exclude",
                        metavar="tab info",
                        choices=["title", "version", "author", "difficulty", "tuning", "capo", "key", "chords",
                                 "strumming", "tab"],
                        nargs="+",
                        help="exclude certain tab info from full tab")

    parser.add_argument("--include",
                        metavar="tab info",
                        choices=["title", "version", "author", "difficulty", "tuning", "capo", "key", "chords",
                                 "strumming", "tab"],
                        nargs="+",
                        help="include certain tab info from blank tab")

    # TODO: add two optional sub-arguments (for file name and download location)
    parser.add_argument("--download", nargs=1, metavar="FILE_NAME DOWNLOAD_LOCATION",
                        help="download info to a .docx file")

    parser.add_argument("--transpose", nargs=1, metavar="KEY",
                        choices=["+1", "+2", "+3", "+4", "+5", "+6", "+7", "+8", "+9", "+10", "+11",
                                 "-1", "-2", "-3", "-4", "-5", "-6", "-7", "-8", "-9", "-10", "-11",
                                 "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#",
                                 "Ab", "Bb", "Db", "Eb", "Gb"],
                        help="transpose tab to another key")
    parser.add_argument("--show", type=bool, default=True, metavar="BOOL",
                        help="show tab info to screen")

    args = parser.parse_args()

    ug_link = "tabs.ultimate-guitar.com/tab/"

    # checks if link from ultimate guitar site
    if ug_link in args.UG_link:
        return args.UG_link
    else:
        raise Exception("Must be valid ultimate guitar link.")


get_link()
