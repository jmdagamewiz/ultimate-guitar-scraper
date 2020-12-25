

def clean_tab(tab_string):
    tab_string = tab_string.replace("[tab]", "")
    tab_string = tab_string.replace("[/tab]", "")
    tab_string = tab_string.replace("[ch]", "")
    tab_string = tab_string.replace("[/ch]", "")

    return tab_string
