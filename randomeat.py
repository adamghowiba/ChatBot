import random

random_places = ['Chick-Fila',
                 'Zaxbys',
                 'McDonalds',
                 'Backyard Bruger',
                 'Checkers',
                 'Costco',
                 'KFC']
random_previous = random_places.copy()


# print(random_previous)
def pick_random_place():
    """
    Random place excluding already output results

    :return: Random place
    """
    global random_previous

    if len(random_previous) == 0:
        random_previous = random_places.copy()
        print("All choices shown... resetting")
        return

    random_choice = random.choice(random_previous)
    random_previous.remove(random_choice)

    print("Your random place to eat is......", random_choice)