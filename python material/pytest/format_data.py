
def format_data_for_display(peoples: list[dict]) -> list[str]:
    """
    The function should output a list of strings that include each person’s full name
    (their given_name followed by their family_name), a colon, and their title:
    """
    #do some code and return the desire results
    return [
        f"{people['given_name']} {people['family_name']}: {people['title']}"
        for people in peoples
    ]
