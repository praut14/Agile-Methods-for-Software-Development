from tkinter.font import families
import unittest
from datetime import date
from gedcom_parser import Individual
from Nancy_Userstories_validation01 import us09, us10

class TestUS09(unittest.TestCase):
    def test_valid_age(self):
        # Create an individual with a valid age (less than 150) and no death date
        individuals = [
            Individual("I1", "John Doe", "M", "1980/01/01", 42, True, "NA", [], [])
        ]
        families = []
        result = us09(individuals, families)
        self.assertTrue(result)
        print("Test US09 - Valid Age and No Death Date passed successfully")

    def test_invalid_age(self):
        # Create an individual with an invalid age (more than 150) and no death date
        individuals = [
            Individual("I1", "Jane Smith", "F", "1800/01/01", 160, True, "NA", [], [])
        ]
        families = []
        result = us09(individuals, families)
        self.assertTrue(result)
        print("Test US09 - Invalid Age and No Death Date passed successfully")

    def test_no_individuals(self):
        # Test with no individuals
        individuals = []
        families = []
        result = us09(individuals, families)
        self.assertTrue(result)
        print("Test US09 - No Individuals passed successfully")

    def test_valid_age_with_death_date(self):
        # Create an individual with a valid age (less than 150) and a death date
        individuals = [
            Individual("I1", "John Doe", "M", "1970/01/01", 80, False, "1990/01/01", [], [])
        ]
        families = []
        result = us09(individuals, families)
        self.assertTrue(result)
        print("Test US09 - Valid Age with Death Date passed successfully")

    def test_invalid_age_with_death_date(self):
        # Create an individual with an invalid age (more than 150) and a death date
        individuals = [
            Individual("I1", "Jane Smith", "F", "1800/01/01", 170, False, "1900/01/01", [], [])
        ]
        families = []
        result = us09(individuals, families)
        self.assertFalse(result)
        print("Test US09 - Invalid Age with Death Date passed successfully")

if __name__ == '__main__':
    unittest.main()
