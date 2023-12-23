from tkinter.font import families
import unittest
from datetime import date
from gedcom_parser import Individual
from Nancy_Userstories_validation01 import us10

class TestUS10(unittest.TestCase):
    def test_valid_birth_before_death(self):
        # Create an individual with a valid birth date before death date
        individuals = [
            Individual("I1", "John Doe", "M", "1980/01/01", 60, False, "2040/01/01", [], [])
        ]
        families = []
        result = us10(individuals, families)
        self.assertTrue(result)
        print("Test US10 - Valid Birth Before Death passed successfully")

    def test_birth_after_death(self):
        # Create an individual with a birth date after death date
        individuals = [
            Individual("I1", "Jane Smith", "F", "2050/01/01", 90, False, "2020/01/01", [], [])
        ]
        families = []
        result = us10(individuals, families)
        self.assertFalse(result)
        print("Test US10 - Birth After Death Error detected successfully")

    def test_no_individuals(self):
        # Test with no individuals
        individuals = []
        families = []
        result = us10(individuals, families)
        self.assertTrue(result)
        print("Test US10 - No Individuals passed successfully")

    def test_valid_birth_when_alive(self):
        # Create an individual with a valid birth date when still alive (no death date)
        individuals = [
            Individual("I1", "John Doe", "M", "1970/01/01", 50, True, "NA", [], [])
        ]
        families = []
        result = us10(individuals, families)
        self.assertTrue(result)
        print("Test US10 - Valid Birth When Alive passed successfully")

if __name__ == '__main__':
    unittest.main()
