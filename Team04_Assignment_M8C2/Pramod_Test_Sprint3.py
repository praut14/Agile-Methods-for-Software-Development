from tkinter.font import families
import unittest
import datetime
import unittest
from gedcom_parser import individual_parser, family_parser
from Pramod_Userstories_Sprint3 import us23, us24

# Load individuals and families from GEDCOM file
individuals = individual_parser("gedcom_test.ged")
families = family_parser("gedcom_test.ged")

class TestGedcomFile(unittest.TestCase):

    def test_us23(self):
        # Test the list of working individuals
        multi_married = us23(families)
        self.assertTrue(isinstance(multi_married, list))  # Ensure the result is a list
        for i in multi_married:
            print(i)

    def test_us24(self):
        # Test the list of working individuals
        no_child = us24(individuals,families)
        self.assertTrue(isinstance(no_child, list))  # Ensure the result is a list
        for i in no_child:
            print(i.name)

if __name__ == '__main__':
    unittest.main()
