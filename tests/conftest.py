import pytest
from requests import get

@pytest.fixture
def all_heroes_json():
    return get(f"https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json").json()
