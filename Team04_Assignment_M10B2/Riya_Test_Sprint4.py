import unittest
from datetime import datetime
from gedcom_parser import individual_parser, family_parser
from Riya_Userstories_Sprint4 import us31, us32

# Load individuals and families from GEDCOM file
individuals = individual_parser("gedcom_test.ged")
families = family_parser("gedcom_test.ged")

class TestGedcomFile(unittest.TestCase):

    def test_us31(self):
        # Test the consistency of naming patterns
        result = us31(individuals, families)
        self.assertEqual(result, [])

    def test_us32(self):
        # Test the verification of marriage anniversaries
        result = us32(families)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
