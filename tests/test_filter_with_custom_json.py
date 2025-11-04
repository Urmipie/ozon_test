import pytest

from main import height_to_meters, filter_heroes

class TestFilterHeroes:
    def test_height_units(self):
        # проверка корректности сравнения роста с разными единицами измерения
        heroes = [
            {
                'id': 1,
                'height': height_to_meters("1.75 meters"),
                'gender': 'Male',
                'working': True
            },
            {
                'id': 2,
                'height': height_to_meters("2.5 cm"),
                'gender': 'Male',
                'working': True
            },
        ]
        assert filter_heroes(heroes, 'Male', True)[0]['id'] == 1

    def test_empty_dict(self):
        assert filter_heroes({}, "Male", False) == []

    def test_no_matches(self):
        heroes = [
            {
                'id': 1,
                'height': height_to_meters("1.75 meters"),
                'gender': 'Male',
                'working': True
            },
            {
                'id': 2,
                'height': height_to_meters("2.5 cm"),
                'gender': 'Male',
                'working': True
            },
        ]
        assert filter_heroes(heroes, "Female", True) == []
