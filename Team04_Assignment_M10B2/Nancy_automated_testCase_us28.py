from tkinter.font import families
import unittest
from datetime import date
from gedcom_parser import Individual, Family
from Nancy_Userstories_validation import us28

#Sprint 4 - Nancy Gupta

# us28  Female last names


class TestUS28(unittest.TestCase):
    def test_female_last_names_sorted(self):
        individuals = [
            Individual("I1", "Alice Smith", "F", "1990/01/01", 32, True, "NA", [], ["F1"]),
            Individual("I2", "Bob Johnson", "M", "1991/06/15", 31, True, "NA", [], ["F1"]),
            Individual("I3", "Catherine White", "F", "1985/03/20", 36, True, "NA", [], ["F2"]),
            Individual("I4", "David Brown", "M", "1980/12/10", 40, True, "NA", [], ["F2"]),
        ]

        result = us28(individuals)

        # Check if females are sorted by last name
        self.assertEqual(result, [individuals[0], individuals[2]])

    def test_no_living_females(self):
        individuals = [
            Individual("I1", "Alice Smith", "F", "1990/01/01", 32, False, "NA", [], ["F1"]),
            Individual("I2", "Bob Johnson", "M", "1991/06/15", 31, False, "NA", [], ["F1"]),
            Individual("I3", "Catherine White", "F", "1985/03/20", 36, False, "NA", [], ["F2"]),
            Individual("I4", "David Brown", "M", "1980/12/10", 40, False, "NA", [], ["F2"]),
        ]

        result = us28(individuals)

        # Check if the result is an empty list when there are no living females
        self.assertEqual(result, [])

    def test_empty_list(self):
        individuals = []

        result = us28(individuals)

        # Check if the result is an empty list when there are no individuals
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
