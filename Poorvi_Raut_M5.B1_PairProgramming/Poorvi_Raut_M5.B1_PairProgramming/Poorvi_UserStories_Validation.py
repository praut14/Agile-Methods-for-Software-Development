import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime
# from tkinter.font import families




# Poorvi Raut User Story US01: Dates (birth, marriage, divorce, death) should not be after the current date

def us01(individuals, families):
    today = date.today()
    current_date = today.strftime("%Y-%m-%d")

    for individual in individuals:
        # Check birthdate
        if individual.birthday != "NA" and individual.birthday > current_date:
            print(f"Error: Individual {individual.id} has a birth date ({individual.birthday}) in the future.")
            return False

        # Check death date
        if individual.deathday != "NA" and individual.deathday > current_date:
            print(f"Error: Individual {individual.id} has a death date ({individual.deathday}) in the future.")
            return False

    for family in families:
        # Check marriage date
        if family.married != "NA" and family.married > current_date:
            print(f"Error: Family {family.id} has a marriage date ({family.married}) in the future.")
            return False

        # Check divorce date
        if family.divorced != "NA" and family.divorced > current_date:
            print(f"Error: Family {family.id} has a divorce date ({family.divorced}) in the future.")
            return False

    print("Test to check Dates (birth, marriage, divorce, death) should not be after the current date")
    return True





# Pair Programming code - Nancy Gupta and Poorvi Raut
#  Poorvi Raut Collaborated with Namcy Gupta on pair programming assignment for us02- to check number of marriages in the family
# jointly done by both - alternatively switching roles of driver and navigator
def us02(individuals,families):
    for family in families:
        marriage_date = family.married
        if marriage_date != 'NA':
            marriage_date = marriage_date.split("/")
            marriage_date = date(int(marriage_date[0]), int(marriage_date[1]), int(marriage_date[2]))
            husband = next(ind for ind in individuals if ind.id == family.husbandId)
            husband_birth_date = husband.birthday.split("/")
            husband_birth_date = date(int(husband_birth_date[0]), int(husband_birth_date[1]), int(husband_birth_date[2]))
            wife = next(ind for ind in individuals if ind.id == family.wifeId)
            wife_birth_date = wife.birthday.split("/")
            wife_birth_date = date(int(wife_birth_date[0]), int(wife_birth_date[1]), int(wife_birth_date[2]))

            # Check if husband's age at marriage is less than 14
            if (marriage_date - husband_birth_date).days < 14*365:
                print("ERROR: FAMILY: US10: Husband's age at marriage is less than 14 years old - Marriage Date: {} : Husband Birth Date: {}".format(family.married, family.husbandObj.birthday))
                return False

            # Check if wife's age at marriage is less than 14
            if (marriage_date - wife_birth_date).days < 14*365:
                print("ERROR: FAMILY: US10: Wife's age at marriage is less than 14 years old - Marriage Date: {} : Wife Birth Date: {}".format(family.married, family.wifeObj.birthday))
                return False

    print('Test to check number of marriages in the family - passed successfully')
    return True
