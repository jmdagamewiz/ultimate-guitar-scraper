import requests

# TODO: check if link is from ultimate-guitar site


def get_input():

    command = input()
    if command.split()[0] == "ugs":
        link = command.split()[1]

        try:
            page = requests.get(link)
        except requests.exceptions.ConnectionError:
            print("Link does not exist. Try again.")

    else:
        print("Wrong command. Try again")

    return link
