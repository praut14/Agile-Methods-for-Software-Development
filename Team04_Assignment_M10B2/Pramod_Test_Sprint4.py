import unittest
from datetime import datetime
from gedcom_parser import individual_parser, family_parser
from Pramod_Usersstories_Sprint4 import us33, us34

# Load individuals and families from GEDCOM file
individuals = individual_parser("gedcom_test.ged")
families = family_parser("gedcom_test.ged")

class TestGedcomFile(unittest.TestCase):

    def test_us33(self):
        # Testing the Consistency Check for Sibling Birth Order
        result = us33(individuals)
        self.assertTrue(result)

    def test_us34(self):
        # Testing the Validation of Age at Marriage
        result = us34(individuals, families)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
