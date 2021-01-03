import input
import guitar_tabs

# hides traceback for better user experience
import sys
sys.tracebacklimit = 0

# save as .exe file and put to C:\Windows\System32 for use in cmd


def main():
    args = input.get_args()
    link = args.UG_link

    try:
        tab = guitar_tabs.GuitarTab(link)

        if args.hide is not True:
            tab.show_info()

        if args.dl is not None:
            tab.download_to(args.dl)

    except KeyError:
        print("Must be valid ultimate guitar link.")
        exit()


if __name__ == "__main__":
    main()
