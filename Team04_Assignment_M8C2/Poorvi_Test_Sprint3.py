from tkinter.font import families
import unittest
import datetime
import unittest
from gedcom_parser import individual_parser, family_parser
from Poorvi_Userstories_Sprint3 import us19, us20

# Load individuals and families from GEDCOM file
individuals = individual_parser("gedcom_test.ged")
families = family_parser("gedcom_test.ged")

class TestGedcomFile(unittest.TestCase):

    def test_us19(self):
        # Test the list of working individuals
        working_individuals = us19(individuals)
        self.assertTrue(isinstance(working_individuals, list))  # Ensure the result is a list
        for individual in working_individuals:
            self.assertEqual(individual.employment_status, "Working")  # Ensure each individual is working

    def test_us20(self):
        # Test the list of dependents in families
        family_dependents = us20(families)
        self.assertTrue(isinstance(family_dependents, dict))  # Ensure the result is a dictionary
        for family_id, dependents in family_dependents.items():
            family = next((f for f in families if f.id == family_id), None)
            self.assertIsNotNone(family)  # Ensure the family with the given ID exists
            for dependent_name in dependents:
                self.assertIn(dependent_name, [ind.name for ind in family.children])  # Ensure each dependent is a child of the family

if __name__ == '__main__':
    unittest.main()
