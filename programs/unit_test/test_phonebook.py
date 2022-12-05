import unittest
from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        # phonebook = PhoneBook()
        self.phonebook.add("Bob", "12345")
        number = self.phonebook.lookup("Bob")
        self.assertEqual("12345", number)
    
    def test_missing_name(self):
        # phonebook = PhoneBook()
        with self.assertRaises(KeyError):
            self.phonebook.lookup("Alice")
    
    # @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        # phonebook = PhoneBook()
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Alice", "0987")
        self.assertTrue(self.phonebook.is_consistent())
    
    def test_is_consistent_with_duplicate_entires(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Alice", "12345")
        self.assertFalse(self.phonebook.is_consistent())
    
    def test_is_consistent_with_duplicate_prefix(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Alice", "123")
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("Bob", "12345")
        self.assertIn("Bob", self.phonebook.get_names())
        self.assertIn("12345", self.phonebook.get_numbers())
        # here two asserts are ok because there are essentially testing the same thing, the add method