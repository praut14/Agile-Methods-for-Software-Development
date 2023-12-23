

import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime
# from tkinter.font import families


#Sprint 4 -Poorvi Raut
 # User Story 29: Display Marital Status of Families
def us29(families):
    marital_status_dict = {}
    for family in families:
        marital_status = family.get_marital_status()
        if marital_status:
            marital_status_dict[family.id] = marital_status

    if marital_status_dict:
        print('Marital status of families:')
        for family_id, status in marital_status_dict.items():
            print(f'Family ID: {family_id}, Marital Status: {status}')
        return marital_status_dict
    else:
        print('No marital status found for families.')
        return {}

# User Story 30: Display Birthdate of Each Individual
def us30(individuals):
    birthdate_dict = {}
    for individual in individuals:
        birthdate = individual.get_birthdate()
        if birthdate:
            birthdate_dict[individual.name] = birthdate

    if birthdate_dict:
        print('Birthdate of each individual:')
        for name, date_of_birth in birthdate_dict.items():
            print(f'Name: {name}, Birthdate: {date_of_birth}')
        return birthdate_dict
    else:
        print('No birthdates found for individuals.')
        return {}