from tkinter.font import families
import unittest
from datetime import date
from datetime import datetime, timedelta
from gedcom_parser import Individual, Family
from Nancy_Userstories_validation import us27

#Sprint 4 - Nancy Gupta

# us27  List recent births

class TestUS27(unittest.TestCase):
    def test_recent_births_empty_list(self):
        individuals = []
        result = us27(individuals)
        self.assertEqual(result, [])
        print("Test US27 - No recent births found (empty list) passed successfully")

    def test_recent_births_no_birthdays(self):
        individuals = [
            Individual("I1", "John Doe", "M", "1990/01/01", 32, True, "NA", [], []),
            Individual("I2", "Jane Smith", "F", "1991/06/15", 31, True, "NA", [], []),
        ]
        result = us27(individuals)
        self.assertEqual(result, [])
        print("Test US27 - No recent births found (no birthdays) passed successfully")

    def test_recent_births_no_recent_births(self):
        today = datetime.now()
        individuals = [
            Individual("I1", "John Doe", "M", (today - timedelta(days=400)).strftime("%Y/%m/%d"), 2, True, "NA", [], []),
            Individual("I2", "Jane Smith", "F", (today - timedelta(days=800)).strftime("%Y/%m/%d"), 3, True, "NA", [], []),
        ]
        result = us27(individuals)

        expected_list = [(ind.id, ind.name, ind.birthday) for ind in individuals[:1]]
        expected_list.sort()

        self.assertEqual(result, expected_list)
        print("Test US27 - No recent births within the last year passed successfully")

    def test_recent_births_within_last_year(self):
        today = datetime.now()
        last_year = today - timedelta(days=365)
        individuals = [
            Individual("I1", "John Doe", "M", last_year.strftime("%Y/%m/%d"), 1, True, "NA", [], []),
            Individual("I2", "Jane Smith", "F", (today - timedelta(days=30)).strftime("%Y/%m/%d"), 1, True, "NA", [], []),
            Individual("I3", "Bob Johnson", "M", (today - timedelta(days=400)).strftime("%Y/%m/%d"), 2, True, "NA", [], []),
        ]
        result = us27(individuals)

        expected_list = [(ind.id, ind.name, ind.birthday) for ind in individuals[:3]]

        self.assertEqual(result, expected_list)
        print("Test US27 - Recent births within the last year passed successfully")




if __name__ == '__main__':
    unittest.main()