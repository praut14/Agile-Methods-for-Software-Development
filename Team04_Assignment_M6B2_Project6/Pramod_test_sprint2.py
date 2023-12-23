from tkinter.font import families
import unittest
# from dateutil.parser import *
import datetime
from datetime import date
from datetime import datetime
import gedcom_parser
# from gedcom_parser import us02, us07, us01
from Pramod_Userstories_validation02 import us15, us16

individuals = gedcom_parser.individual_parser("gedcom_test.ged")
families = gedcom_parser.family_parser("gedcom_test.ged")


class TestGedcomFile(unittest.TestCase):

    def test_us15(self):
        self.assertTrue(us15(individuals,families))

    def test_us16(self):
        self.assertTrue(us16(individuals,families))



if __name__ == '__main__':
    unittest.main()

