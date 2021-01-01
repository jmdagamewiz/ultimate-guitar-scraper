import input
import guitar_tabs
import docx_handler

# hides traceback for better user experience
import sys
sys.tracebacklimit = 0

# save as .exe file and put to C:\Windows\System32 for use in cmd


def main():
    args = input.get_args()
    link = args.UG_link

    try:
        tab = guitar_tabs.GuitarTab(link)

        if args.sh is None:
            tab.show_info()

        if args.dl is None:
            docx_handler.write_to_doc(tab.title, tab.get_clean_tab())
        else:
            print(f"Download location is {args.dl}")

    except KeyError:
        print("Must be valid ultimate guitar link.")


if __name__ == "__main__":
    main()
