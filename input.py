import argparse


def get_args():

    # TODO: understand how arguments get their values
    parser = argparse.ArgumentParser(description="ultimate guitar chords scraper")
    parser.add_argument("UG_link", help="ultimate guitar page link")

    parser.add_argument("--dl", nargs=1, metavar="DOWNLOAD_LOCATION",
                        help="download info to a .docx file")

    parser.add_argument("--tp", nargs=1, metavar="KEY",
                        choices=["+1", "+2", "+3", "+4", "+5", "+6", "+7", "+8", "+9", "+10", "+11",
                                 "-1", "-2", "-3", "-4", "-5", "-6", "-7", "-8", "-9", "-10", "-11",
                                 "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#",
                                 "Ab", "Bb", "Db", "Eb", "Gb"],
                        help="transpose tab to another key")

    # TODO: fix this. Argument accepts true even if --sh False is input
    parser.add_argument("--sh", type=bool, choices=[False], metavar="BOOL",
                        help="show tab info to screen")

    args = parser.parse_args()

    main_ug_link = "tabs.ultimate-guitar.com/tab/"

    # checks if link from ultimate guitar site
    if main_ug_link in args.UG_link:
        return args
    else:
        raise Exception("Must be valid ultimate guitar link.")

