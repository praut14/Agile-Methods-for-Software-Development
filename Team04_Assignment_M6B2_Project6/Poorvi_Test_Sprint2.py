from tkinter.font import families
import unittest
import datetime
from datetime import date
from datetime import datetime
import gedcom_parser
from Poorvi_Userstories_Sprint2 import us11, us12  # Importing the new user stories

# Load individuals and families from GEDCOM file
individuals = gedcom_parser.individual_parser("gedcom_test.ged")
families = gedcom_parser.family_parser("gedcom_test.ged")

class TestGedcomFile(unittest.TestCase):

    def test_us11(self):
        # Test the number of divorces in families
        num_divorces = us11(families)
        self.assertTrue(num_divorces >= 0)  # Ensure the result is non-negative
    def test_us11(self):  
        self.assertTrue(us03([], families))
    def test_us11(self):     
        self.assertTrue(us03(individuals, []))
    def test_us11(self):        
        self.assertTrue(us03([], []))
    def test_us11(self):     
        self.assertTrue(us03(families,individuals))

    def test_us12(self):
        # Test unique last names in families
        self.assertFalse(us12(individuals))
    def test_us12(self):     
        self.assertFalse(us03(individuals, []))
    def test1_us12(self):        
        self.assertTrue(us03([], []))
    def test1_us12(self):     
        self.assertFalse(us03(families,individuals))

if __name__ == '__main__':
    unittest.main()
