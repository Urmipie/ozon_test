from requests import get
from typing import Literal
from itertools import product

API_URL = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'

def height_to_meters(height_string: str) -> float:
    height_units = {'cm': 1/100, 'meters': 1}
    height, unit = height_string.split()
    return float(height) * height_units[unit] if unit in height_units else 0
    # У одного объекта рост указан как 0 кг, поэтому обнуление роста если единица измерения неправильная


def get_heroes() -> list:
    heroes = get(f"{API_URL}/all.json").json()

    return [
        {'id': int(hero['id']),
        'height': height_to_meters(hero['appearance']['height'][1]),
        'gender': hero['appearance']['gender'],
        'working': hero['work']['occupation'] != '-'}
        for hero in heroes
    ]


def filter_heroes(heroes: list, gender: str, working: bool):
    return sorted(filter(lambda hero: hero['gender'] == gender and hero['working'] == working, heroes),
                  key=lambda x: x['height'], reverse=True)


def get_heroes_by_gender_and_employment(gender: Literal['Male', '-', 'Female'], working: bool):
    if gender not in ['Male', '-', 'Female']:
        raise ValueError('invalid gender')
    heroes = filter_heroes(get_heroes(), gender, working)
    return heroes[0] if heroes else []


if __name__ == "__main__":
    print('gender\t|\tworking\t|\ttallest hero id\n')
    for i in product(['Male', '-', 'Female'], [True, False]):
        print(i[0].ljust(5), i[1], get_heroes_by_gender_and_employment(i[0], i[1])['id'], sep='\t|\t')