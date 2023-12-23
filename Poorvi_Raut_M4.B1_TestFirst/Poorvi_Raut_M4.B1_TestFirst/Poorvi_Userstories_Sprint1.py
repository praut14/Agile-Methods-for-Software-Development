import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime
# from tkinter.font import families


#Sprint 1 -Poorvi Raut
def us03(individuals, families):
    for family in families:
        husband = None
        wife = None

        # Find the husband and wife in the family
        for individual in individuals:
            if individual.id == family.husbandId:
                husband = individual
            elif individual.id == family.wifeId:
                wife = individual

        if husband is not None and husband.deathday != "NA":
            deathdate = husband.deathday.split("/")
            date_of_death = date(
                int(deathdate[0]),
                int(deathdate[1]),
                int(deathdate[2]))

            for child_id in family.children:
                child = next((individual for individual in individuals if individual.id == child_id), None)
                if child is not None:
                    birthdate = child.birthday.split("/")
                    date_of_birth = date(
                        int(birthdate[0]),
                        int(birthdate[1]),
                        int(birthdate[2]))

                    if date_of_birth > date_of_death:
                        print(f'Error: Child {child.id} was born after the death of father {husband.id}')
                        return False

        if wife is not None and wife.deathday != "NA":
            deathdate = wife.deathday.split("/")
            date_of_death = date(
                int(deathdate[0]),
                int(deathdate[1]),
                int(deathdate[2]))

            for child_id in family.children:
                child = next((individual for individual in individuals if individual.id == child_id), None)
                if child is not None:
                    birthdate = child.birthday.split("/")
                    date_of_birth = date(
                        int(birthdate[0]),
                        int(birthdate[1]),
                        int(birthdate[2]))

                    if date_of_birth > date_of_death:
                        print(f'Error: Child {child.id} was born after the death of mother {wife.id}')
                        return False

    print('Test 3 Successfully Passed.')
    return True



