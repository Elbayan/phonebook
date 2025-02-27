import pytest
import random

import storage.storage


@pytest.fixture()
def clear_storage():
    global STORAGE
    STORAGE = []


def generate_name(lenght_name=9):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    fake_name = ''.join(random.choice(alphabet) for _ in range(lenght_name))
    return fake_name


def test_add_entry():
    number = []

    name = generate_name()
    surname = generate_name()
    while len(number) < 10:
        number.append(random.randrange(10))

    number = ''.join(str(num) for num in number)

    test_collection = {
        'name': name,
        'surname': surname,
        'number': number
        }

    storage.storage.add_entry(name, surname, number)
    got_storage = storage.storage.get_list()

    assert got_storage == [test_collection]
