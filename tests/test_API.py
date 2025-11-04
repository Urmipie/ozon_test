import pytest
import re

class TestAPI:
    """
    Проверка АПИ-шки на согласованность структуры данных с ожидаемой.
    """
    def test_possible_genders(self, all_heroes_json):
        genders_in_json = set(hero['appearance']['gender'] for hero in all_heroes_json)
        assert genders_in_json == {'Male', 'Female', '-'}, f"unexpected genders in {genders_in_json}"

    def test_metric_height(self, all_heroes_json):
        # У одного объекта рост указан как 0 кг, поэтому тест проваливается
        for hero in all_heroes_json:
            height = hero['appearance']['height'][1]
            assert re.match(r'\d+(\.?\d+)? ((cm)|(meters))', height), \
                f"string '{height}' from id {hero["id"]} have incorrect height format"

    def test_work_not_none(self, all_heroes_json):
        for hero in all_heroes_json:
            assert hero['work']['occupation'] is not None, \
                f"id {hero['id']} has no work occupation"

    def test_unique_id(self, all_heroes_json):
        all_ids = list(hero['id'] for hero in all_heroes_json)
        assert len(set(all_ids)) == len(all_ids), f"id {all_ids} has duplicate ids"
