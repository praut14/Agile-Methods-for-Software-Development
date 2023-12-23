from tkinter.font import families
import unittest
from datetime import date
from gedcom_parser import Individual, Family
from Nancy_Userstories_validation import us25

#Sprint 4 - Nancy Gupta

# us25  Order siblings by age

class TestUS25(unittest.TestCase):
    def assertIndividualListEqual(self, list1, list2):
        self.assertEqual(len(list1), len(list2))

        for ind1, ind2 in zip(list1, list2):
            self.assertEqual(ind1.id, ind2.id)
            self.assertEqual(ind1.name, ind2.name)
            self.assertEqual(ind1.gender, ind2.gender)
            self.assertEqual(ind1.birthday, ind2.birthday)
            self.assertEqual(ind1.age, ind2.age)
            self.assertEqual(ind1.alive, ind2.alive)
            self.assertEqual(ind1.deathday, ind2.deathday)
            self.assertEqual(ind1.child, ind2.child)
            self.assertEqual(ind1.spouse, ind2.spouse)

    def test_ordered_siblings(self):
        individuals = [
            Individual("I1", "John Doe", "M", "1980/01/01", 42, True, "NA", [], []),
            Individual("I2", "Jane Smith", "F", "1982/02/15", 40, True, "NA", [], []),
            Individual("I3", "Bob Johnson", "M", "1985/06/20", 37, True, "NA", [], []),
        ]

        families = [
            Family("F1", "1990/05/20", "NA", "I1", "John Doe", "I2", "Jane Smith", ["I3"]),
        ]

        result = us25(individuals, families)
        expected_order = [
            Individual("I3", "Bob Johnson", "M", "1985/06/20", 37, True, "NA", [], [])
        ]

        # Check if the result is a list of Individuals
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], Individual)

        self.assertIndividualListEqual(result, expected_order)
        print("Test US25 - Ordered Siblings by Age passed successfully")


    def test_no_children(self):
        individuals = [
            Individual("I1", "John Doe", "M", "1980/01/01", 42, True, "NA", [], []),
            Individual("I2", "Jane Smith", "F", "1982/02/15", 40, True, "NA", [], []),
        ]

        families = [
            Family("F1", "1990/05/20", "NA", "I1", "John Doe", "I2", "Jane Smith", []),
        ]

        result = us25(individuals, families)
        self.assertEqual(result, [])
        print("Test US25 - No Children in the Family passed successfully")

    def test_single_child(self):
        individuals = [
            Individual("I1", "John Doe", "M", "1980/01/01", 42, True, "NA", [], []),
            Individual("I2", "Jane Smith", "F", "1982/02/15", 40, True, "NA", [], []),
            Individual("I3", "Bob Johnson", "M", "1985/06/20", 37, True, "NA", [], []),
        ]

        families = [
            Family("F1", "1990/05/20", "NA", "I1", "John Doe", "I2", "Jane Smith", ["I3"]),
        ]

        # Remove I3 from the family to simulate a single child family
        families[0].childrenId = []

        result = us25(individuals, families)
        self.assertEqual(result, [])
        print("Test US25 - Single Child in the Family passed successfully")

if __name__ == '__main__':
    unittest.main()