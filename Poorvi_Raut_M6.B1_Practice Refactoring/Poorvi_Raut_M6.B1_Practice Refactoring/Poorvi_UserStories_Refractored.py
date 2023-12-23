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






