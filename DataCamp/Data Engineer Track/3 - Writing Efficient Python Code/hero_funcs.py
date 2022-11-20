import numpy as np

heroes = ['Batman', 'Superman', 'Wonder Woman']
hts = np.array([188.0, 191.0, 183.0])
wts = np.array([95.0, 101.0, 74.0])

print('Heroes: ', heroes)
print('Height: ', hts)
print('Weight: ', wts)


def convert_units(heroes, heights, weights):
    new_hts = [ht * 0.39370 for ht in heights]  #List comprehension
    new_wts = [wt * 2.20462 for wt in weights]

    hero_data = {}  # new dictionary using literal syntax

    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])
    return hero_data


print(convert_units(heroes, hts, wts))
