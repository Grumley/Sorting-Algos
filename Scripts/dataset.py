import random


def random_list(mini=0, maxi=100):
    ordered_list = list(range(mini, maxi + 1))
    random.shuffle(ordered_list)
    return ordered_list
