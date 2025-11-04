import pytest

from main import get_heroes_by_gender_and_employment, height_to_meters


class TestGetHeroesByGenderAndEmploymentErrors:
    def test_lowercase_gender(self):
        with pytest.raises(ValueError):
            get_heroes_by_gender_and_employment('male', False)

    def test_wrong_gender(self):
        with pytest.raises(ValueError):
            get_heroes_by_gender_and_employment('nonmale', False)


class TestGetHeroesByGenderAndEmploymentReturns:
    """
    Сравнивать полученный вывод с ожидаемым используя JSON из API как-то неправильно,
    но по заданию нужно не использовать моки
    """

    def test_male_employed(self):
        result = get_heroes_by_gender_and_employment('Male', True)
        assert result['id'] == 681

    def test_male_unemployed(self):
        result = get_heroes_by_gender_and_employment('Male', False)
        assert result['id'] == 728

    def test_female_employed(self):
        result = get_heroes_by_gender_and_employment('Female', True)
        assert result['id'] == 284

    def test_female_unemployed(self):
        result = get_heroes_by_gender_and_employment('Female', False)
        assert result['id'] == 42

    def test_unmarked_employed(self):
        result = get_heroes_by_gender_and_employment('-', True)
        assert result['id'] == 409

    def test_unmarked_unemployed(self):
        result = get_heroes_by_gender_and_employment('-', False)
        assert result['id'] == 287


class TestUnitConversion:
    def test_meters(self):
        assert height_to_meters("12 meters") == 12

    def test_centimeters(self):
        assert height_to_meters("10 cm") == 0.10

    def test_float(self):
        assert height_to_meters("0.1 meters") == 0.1

    def test_wrong_unit(self):
        assert height_to_meters("12 kg") == 0

    def test_zero(self):
        assert height_to_meters("0 cm") == 0