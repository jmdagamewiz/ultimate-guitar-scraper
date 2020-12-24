import requests

# TODO: check if link is from ultimate-guitar


def get_input():
    while True:
        command = input()
        if command.split()[0] == "ugs":
            link = command.split()[1]

            try:
                page = requests.get(link)
                break
            except requests.exceptions.ConnectionError:
                print("Link does not exist. Try again.")

        else:
            print("Wrong command. Try again")

    return link
