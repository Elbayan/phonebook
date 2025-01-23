import pytest

from storage.storage import add_entry

def add_entry()
# Очищаем STORAGE перед каждым тестом
@pytest.fixture(autouse=True)
def clear_storage():
    global STORAGE
    STORAGE = []


class


def test_insert():
    # Проверка добавления записи
    insert('Ivan', 'Ivanov', '1234567890')
    assert len(list()) == 1
    assert list()[0] == {'name': 'Ivan', 'surname': 'Ivanov', 'tel': '1234567890'}

def test_get_existing_record():
    # Добавляем и проверяем получение записи
    insert('Ivan', 'Ivanov', '1234567890')
    record = get('1234567890')
    assert record == {'name': 'Ivan', 'surname': 'Ivanov', 'tel': '1234567890'}

def test_get_non_existing_record():
    # Проверка получения записи, которая не существует
    record = get('1111111111')
    assert record is None

def test_list():
    # Проверка получения всех записей
    insert('Ivan', 'Ivanov', '1234567890')
    insert('Petr', 'Petrov', '0987654321')
    all_records = list()
    assert len(all_records) == 2
    assert all_records == [
        {'name': 'Ivan', 'surname': 'Ivanov', 'tel': '1234567890'},
        {'name': 'Petr', 'surname': 'Petrov', 'tel': '0987654321'}
    ]

def test_delete_existing_record():
    # Проверка удаления записи
    insert('Ivan', 'Ivanov', '1234567890')
    deleted_record = delete('1234567890')
    assert deleted_record == {'name': 'Ivan', 'surname': 'Ivanov', 'tel': '1234567890'}
    assert len(list()) == 0

def test_delete_non_existing_record():
    # Проверка удаления несуществующей записи
    deleted_record = delete('1111111111')
    assert deleted_record is None
