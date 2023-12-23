from tkinter.font import families
import unittest
from datetime import date
from gedcom_parser import Individual, Family
from Nancy_Userstories_validation import us17

#Sprint 3 - Nancy Gupta

# us17 List living married

class TestUS17(unittest.TestCase):
    def test_living_married(self):
        individuals = [
            Individual("I1", "John Doe", "M", "1980/01/01", 42, True, "NA", [], []),
            Individual("I2", "Jane Smith", "F", "1982/02/15", 40, True, "NA", [], []),
        ]

        families = [
            Family("F1", "1990/05/20", "NA", "I1", "John Doe", "I2", "Jane Smith", []),
        ]

        result = us17(individuals, families)
        self.assertTrue(result)
        print("Test US17 - Living Married Couples passed successfully")

    def test_no_living_married(self):
        individuals = [
            Individual("I1", "John Doe", "M", "1980/01/01", 42, True, "NA", [], []),
            Individual("I2", "Jane Smith", "F", "1982/02/15", 40, False, "1990/05/20", [], []),
        ]

        families = [
            Family("F1", "1990/05/20", "NA", "I1", "John Doe", "I2", "Jane Smith", []),
        ]

        result = us17(individuals, families)
        self.assertEqual(result, [])
        print("Test US17 - No Living Married Couples passed successfully")

    def test_single_individual(self):
        individuals = [
            Individual("I1", "John Doe", "M", "1980/01/01", 42, True, "NA", [], []),
        ]

        families = []

        result = us17(individuals, families)
        self.assertEqual(result, [])
        print("Test US17 - Single Individual passed successfully")

if __name__ == '__main__':
    unittest.main()