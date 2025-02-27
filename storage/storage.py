STORAGE = []


def add_entry(name, surname, number):
    '''
    Add entry to STORAGE.

    :param name: Name
    :param surname: Surname
    :param number: Phone number
    '''

    STORAGE.append({'name': name, 'surname': surname, 'number': number})


def get_entry(number):
    '''
    Search for a entry in the to STORAGE and returns it.

    :param number: Phone number
    '''

    for entry in STORAGE:
        if entry['number'] == number:
            return entry
    return None


def del_entry(number):
    '''
    Delete a entry from STORAGE.

    :param number: Phone number
    '''

    for i, entry in enumerate(STORAGE):
        if entry['number'] == number:
            return STORAGE.pop(i)
    return None



def get_list():
    '''
    Return all entries from phonebook.
    '''

    return STORAGE
