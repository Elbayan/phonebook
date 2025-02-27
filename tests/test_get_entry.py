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


def add_entry(iter_count=5):
    list_numbers = []
    for _ in range(iter_count):
        number = []

        name = generate_name()
        surname = generate_name()
        while len(number) < 10:
            number.append(random.randrange(10))

        number = int(''.join(str(num) for num in number))
        list_numbers.append(number)

        storage.storage.add_entry(name, surname, number)


    return list_numbers

def test_get_entry():

    known_numbers = add_entry()
    test_number = random.choice(known_numbers)
    result = storage.storage.get_entry(test_number)

    assert result is not None
