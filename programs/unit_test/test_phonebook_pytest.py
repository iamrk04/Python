import pytest
from phonebook import PhoneBook

@pytest.fixture
def phonebook(tmpdir):
    """Provides an empty PhoneBook"""
    phonebook = PhoneBook(tmpdir)
    return phonebook
    # yield phonebook
    # phonebook.clear()

def test_lookup_by_name(phonebook):
    # phonebook = PhoneBook()
    phonebook.add("Bob", "12345")
    assert "12345" == phonebook.lookup("Bob")
    
def test_phonebook_contains_all_names(phonebook):
    # phonebook = PhoneBook()
    phonebook.add("Alice", "12345")
    assert {"Alice"} == set(phonebook.get_names())

def test_missing_name_raises_error(phonebook):
    # phonebook = PhoneBook()
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")