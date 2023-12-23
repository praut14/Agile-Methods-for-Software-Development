import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime
# from tkinter.font import families


#Sprint 3 -Poorvi Raut

# User Story 19:  List of Working individuals
def us19(individuals):
    working_individuals = []
    for individual in individuals:
        if individual.name == "Working":
            working_individuals.append(individual)
    
    if working_individuals:
        print('List of working individuals:')
        for individual in working_individuals:
            print(individual.name)
        return working_individuals
    else:
        print('No working individuals found.')
        return []
# User Story 20: Unique Last Names in the Family

def us20(families):
    dependents_in_families = {}
    for family in families:
        family_dependents = []
        for individual in family.Children:
            family_dependents.append(individual.name)
        dependents_in_families[family.id] = family_dependents

    if dependents_in_families:
        print('List of dependents in each family:')
        for family_id, dependents in dependents_in_families.items():
            print(f'Family ID: {family_id}, Dependents: {", ".join(dependents)}')
        return dependents_in_families
    else:

        print('No families with dependents found.')
        return {}