from tkinter.font import families
import unittest
# from dateutil.parser import *
import datetime
from datetime import date
from datetime import datetime
import gedcom_parser
from Poorvi_UserStories_BadSmell import us01




individuals = gedcom_parser.individual_parser("gedcom_test.ged")
families = gedcom_parser.family_parser("gedcom_test.ged")


class TestGedcomFile(unittest.TestCase):

    def test_us01(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        #families = gedcom_parser.family_parser("gedcom_test.ged")
        #self.assertTrue(us01(individuals,families))
    def test1_us01(self):     
        self.assertTrue(us01(individuals, []))
    def test1_us01(self):        
        self.assertTrue(us01([], []))
   
           

if __name__ == '__main__':
    unittest.main()