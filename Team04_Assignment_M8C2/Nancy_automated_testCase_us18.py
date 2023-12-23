from tkinter.font import families
import unittest
from datetime import date
from gedcom_parser import Individual, Family
from Nancy_Userstories_validation import us18


#Sprint 3 - Nancy Gupta

# us18 Siblings spacing

class TestUS18(unittest.TestCase):
    def test_valid_siblings_spacing(self):
        individuals = [
            Individual("I1", "John Doe", "M", "1990-01-01", 32, True, "NA", [], []),
            Individual("I2", "Jane Smith", "F", "1991-06-15", 31, True, "NA", [], []),
            Individual("I3", "Child1", "M", "2010-03-10", 11, True, "NA", [], ["I4"]),
            Individual("I4", "Child2", "F", "2015-07-20", 6, True, "NA", ["I3"], [])
        ]

        families = [
            Family("F1", "1992-02-20", "NA", "I1", "John Doe", "I2", "Jane Smith", ["I3", "I4"]),
            Family("F2", "2015-03-10", "NA", "I1", "John Doe", "I2", "Jane Smith", [])
        ]

        result = us18(individuals, families)
        self.assertTrue(result)
        print("Test US18 - Valid Siblings Spacing passed successfully")

    def test_no_siblings(self):
        individuals = [
            Individual("I1", "John Doe", "M", "1990-01-01", 32, True, "NA", [], []),
            Individual("I2", "Jane Smith", "F", "1991-06-15", 31, True, "NA", [], [])
        ]

        families = [
            Family("F1", "1992-02-20", "NA", "I1", "John Doe", "I2", "Jane Smith", [])
        ]

        result = us18(individuals, families)
        self.assertTrue(result)
        print("Test US18 - No Siblings passed successfully")

    def test_invalid_siblings_spacing(self):
        individuals = [
            Individual("I1", "John Doe", "M", "1990-01-01", 32, True, "NA", [], []),
            Individual("I2", "Jane Smith", "F", "1991-06-15", 31, True, "NA", [], []),
            Individual("I3", "Child1", "M", "2010-03-10", 11, True, "NA", [], ["I4"]),
            Individual("I4", "Child2", "F", "2010-07-20", 11, True, "NA", [], ["I3"])
        ]

        families = [
            Family("F1", "1992-02-20", "NA", "I1", "John Doe", "I2", "Jane Smith", ["I3", "I4"])
        ]

        result = us18(individuals, families)
        self.assertFalse(result)
        print("Test US18 - Invalid Siblings Spacing passed successfully")

if __name__ == '__main__':
    unittest.main()