import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime
# from tkinter.font import families




#Sprint 3 - Riya Divakaran


def us21(families, individuals):
    """
    Ensure that the spouse in a family has the correct gender.

    :param families: List of family objects
    :param individuals: List of individual objects
    :return: True if spouses have the correct gender, False otherwise
    """
    for family in families:
        husband_id = family.husbandId
        wife_id = family.wifeId

        husband = next((ind for ind in individuals if ind.id == husband_id), None)
        wife = next((ind for ind in individuals if ind.id == wife_id), None)

        # Ensure both husband and wife exist and have the correct gender
        if husband and wife:
            if husband.gender == 'F':
                print(f"ERROR: US21: Husband {husband.name} (ID: {husband.id}) in family {family.id} has the incorrect gender.")
                return False

            if wife.gender == 'M':
                print(f"ERROR: US21: Wife {wife.name} (ID: {wife.id}) in family {family.id} has the incorrect gender.")
                return False

    print("US21: Spouses have the correct gender.")
    return True

def us22(individuals, families):
    """
    Ensure the age difference between spouses is appropriate in the family.

    :param individuals: List of individual objects
    :param families: List of family objects
    :return: True if age difference between spouses is appropriate, False otherwise
    """
    for family in families:
        husband_id = family.husbandId
        wife_id = family.wifeId

        # Find husband and wife details
        husband = next((ind for ind in individuals if ind.id == husband_id), None)
        wife = next((ind for ind in individuals if ind.id == wife_id), None)

        if husband and wife:
            husband_birth_date = datetime.strptime(husband.birthday, "%Y/%m/%d").date()
            wife_birth_date = datetime.strptime(wife.birthday, "%Y/%m/%d").date()

            # Calculate the age difference
            age_difference = abs((husband_birth_date - wife_birth_date).days) / 365

            # Define the allowed age difference between spouses, for instance, less than 120 years
            if age_difference >= 120:  # Adjust the threshold as needed
                print(f"ERROR: US22: The age difference between spouses in Family {family.id} is not appropriate.")
                print(f"  - Husband: {husband.name} (Birthdate: {husband.birthday})")
                print(f"  - Wife: {wife.name} (Birthdate: {wife.birthday})")
                return False

    print("US22: Age difference between spouses is appropriate.")
    return True
