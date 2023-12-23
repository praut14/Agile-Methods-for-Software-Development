from tkinter.font import families
import unittest
# from dateutil.parser import *
import datetime
from datetime import date
from datetime import datetime
import gedcom_parser
from Riya_Userstories_Sprint2 import us13, us14




individuals = gedcom_parser.individual_parser("gedcom_test.ged")
families = gedcom_parser.family_parser("gedcom_test.ged")


class TestGedcomFile(unittest.TestCase):

    def test_us13(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertTrue(us13(individuals))
        

    def test_us14(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertTrue(us14(individuals, families))


if __name__ == '__main__':
    unittest.main()
