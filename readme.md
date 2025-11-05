# Установка
```commandline
pip install -r requirements.txt
```

# Использование
```commandline
python main.py
```
# Запуск тестов

```commandline
python -m pytest
```
[Основной набор тестов](tests/test_heroes.py)

[Тесты со своими данными (не в основных потому что в задании указано не использовать моки,
но я решил всё же добавить)](tests/test_filter_with_custom_json.py)

[Тесты на соответствие данных из АПИ с ожидаемыми.](tests/test_API.py) В данных из АПИшки у одного героя рост указан в
килограммах, поэтому один тест проваливается.