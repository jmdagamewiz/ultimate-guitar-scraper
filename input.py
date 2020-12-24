import requests


def get_link():

    command = ""
    link = ""
    try:
        command, link = input().split()

    # handles ValueError and IndexError in one line
    except (ValueError, IndexError) as e:
        print("Invalid format.")

    if command == "ugs":

        try:
            page = requests.get(link)
        except requests.exceptions.ConnectionError:
            print("Link does not exist. Try again.")

    else:
        print("Wrong command.")
        print("Try again.")

    return link
