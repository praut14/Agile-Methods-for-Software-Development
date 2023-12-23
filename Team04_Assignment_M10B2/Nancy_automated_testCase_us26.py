from tkinter.font import families
import unittest
from datetime import date
from gedcom_parser import Individual, Family
from Nancy_Userstories_validation import us26


#Sprint 4 - Nancy Gupta

# us26 List living singles


class TestUS26(unittest.TestCase):
    def test_valid_living_singles(self):
        individuals = [
            Individual("I1", "John Doe", "M", "1990-01-01", 32, True, "NA", [], []),
            Individual("I2", "Jane Smith", "F", "1991-06-15", 31, True, "NA", [], []),
            Individual("I3", "Single1", "M", "1985-03-10", 36, True, "NA", [], []),
            Individual("I4", "Single2", "F", "1988-07-20", 33, True, "NA", [], [])
        ]

        families = [
            Family("F1", "1992-02-20", "NA", "I1", "John Doe", "I2", "Jane Smith", []),
            Family("F2", "2015-03-10", "NA", "I3", "Single1", "I4", "Single2", []),
        ]

        result = us26(individuals, families)
        self.assertTrue(result)
        print("Test US26 - Valid Living Singles passed successfully")

    def test_no_living_singles(self):
        individuals = [
            Individual("I1", "John Doe", "M", "1990-01-01", 32, True, "NA", [], []),
            Individual("I2", "Jane Smith", "F", "1991-06-15", 31, True, "NA", [], []),
            Individual("I3", "Deceased1", "M", "1985-03-10", 36, False, "2022-01-01", [], []),
            Individual("I4", "Deceased2", "F", "1988-07-20", 33, False, "2020-02-15", [], [])
        ]

        families = [
            Family("F1", "1992-02-20", "NA", "I1", "John Doe", "I2", "Jane Smith", []),
            Family("F2", "2015-03-10", "NA", "I3", "Deceased1", "I4", "Deceased2", []),
        ]

        result = us26(individuals, families)
        self.assertTrue(result)
        print("Test US26 - No Living Singles passed successfully")

    def test_mixed_living_status(self):
        individuals = [
            Individual("I1", "John Doe", "M", "1990-01-01", 32, True, "NA", [], ["I2"]),
            Individual("I2", "Jane Smith", "F", "1991-06-15", 31, True, "NA", ["I1"], []),
            Individual("I3", "Deceased1", "M", "1985-03-10", 36, False, "2022-01-01", [], []),
            Individual("I4", "Single2", "F", "1988-07-20", 33, True, "NA", [], [])
        ]

        families = [
            Family("F1", "1992-02-20", "NA", "I1", "John Doe", "I2", "Jane Smith", ["I4"]),
            Family("F2", "2015-03-10", "NA", "I3", "Deceased1", "I4", "Single2", []),
        ]

        result = us26(individuals, families)
        self.assertTrue(result)
        print("Test US26 - Mixed Living Status passed successfully")

    def test_single_parent_with_child(self):
        individuals = [
            Individual("I1", "SingleParent", "M", "1980-01-01", 42, True, "NA", [], ["I2"]),
            Individual("I2", "Child", "F", "2005-03-10", 16, True, "NA", ["I1"], [])
        ]

        families = [
            Family("F1", "1990-05-20", "NA", "I1", "SingleParent", "NA", "NA", ["I2"]),
        ]

        result = us26(individuals, families)
        self.assertTrue(result)
        print("Test US26 - Single Parent with Child passed successfully")


if __name__ == '__main__':
    unittest.main()