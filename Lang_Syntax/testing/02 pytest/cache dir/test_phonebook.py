import pytest

from phonebook import Phonebook


@pytest.fixture
def phonebook(tmpdir):
    "Provide an empty phone book"
    return Phonebook(tmpdir)
    return phonebook


def test_add_and_lookup_entry(phonebook):
    phonebook.add("Joe", "1234")
    assert "1234" == phonebook.lookup("Joe")


def test_phonebook_gives_access_to_names_and_numbers(phonebook):
    phonebook.add("Alfred", "1234")
    phonebook.add("Bruce", "123")
    assert set(phonebook.names()) == { "Alfred", "Bruce" }


def test_missing_entry_raises_KeyError(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("non-existent")