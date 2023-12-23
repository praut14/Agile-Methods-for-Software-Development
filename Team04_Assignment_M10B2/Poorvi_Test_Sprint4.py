
from tkinter.font import families
import unittest
from gedcom_parser import individual_parser, family_parser
from Poorvi_UserStories_Sprint4 import  us29, us30 
 
# Load individuals and families from GEDCOM file
individuals = individual_parser("gedcom_test.ged")
families = family_parser("gedcom_test.ged")

class TestGedcomFile(unittest.TestCase):

 def test_us29(self):
        # Test the list of marital statuses of families
        marital_status_dict = us29(families)
        self.assertTrue(isinstance(marital_status_dict, dict))  # Ensure the result is a dictionary
        for family_id, status in marital_status_dict.items():
            self.assertIsInstance(status, str)  # Ensure each marital status is a string

def test_us30(self):
    # Test the list of birthdates of individuals
        birthdate_dict = us30(individuals)
        self.assertTrue(isinstance(birthdate_dict, dict))  # Ensure the result is a dictionary
        for name, date_of_birth in birthdate_dict.items():
            self.assertIsInstance(date_of_birth, datetime.date)  # Ensure each birthdate is a datetime.date object

if __name__ == '__main__':
    unittest.main()