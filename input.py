import argparse
import find_path


def get_args():

    dl_location = find_path.get_download_path()

    parser = argparse.ArgumentParser(description="ultimate guitar chords scraper",
                                     usage="ugs UG_link [-h] [--dl [DOWNLOAD_LOCATION]] [--tp KEY] [--hide]")
    parser.add_argument("UG_link", help="ultimate guitar page link")

    parser.add_argument("--dl", metavar="DOWNLOAD_LOCATION",
                        nargs="?",
                        const=dl_location,
                        help="download info to a .docx file")

    parser.add_argument("--tp", metavar="KEY",
                        choices=["+1", "+2", "+3", "+4", "+5", "+6", "+7", "+8", "+9", "+10", "+11",
                                 "-1", "-2", "-3", "-4", "-5", "-6", "-7", "-8", "-9", "-10", "-11",
                                 "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#",
                                 "Ab", "Bb", "Db", "Eb", "Gb"],
                        help="transpose tab to another key")

    parser.add_argument("--hide", help="hide tab info", action="store_true", default=False)

    args = parser.parse_args()

    main_ug_link = "tabs.ultimate-guitar.com/tab/"

    # checks if link from ultimate guitar site
    if main_ug_link in args.UG_link:
        return args
    else:
        raise Exception("Must be valid ultimate guitar link.")
