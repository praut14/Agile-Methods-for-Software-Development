import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime
# from tkinter.font import families


#Sprint 3 - Nancy Gupta

# us17 List living married

def us17(individuals, families):
    living_married = []
    
    for family in families:
        husband_id = family.husbandId  # Update attribute names
        wife_id = family.wifeId  # Update attribute names

        husband = next((ind for ind in individuals if ind.id == husband_id), None)
        wife = next((ind for ind in individuals if ind.id == wife_id), None)

        if husband is not None and wife is not None:
            if husband.alive and wife.alive:
                living_married.append(family)

    if len(living_married) > 0:
        print("List of living married couples:")
        for family in living_married:
            print(f"Family ID: {family.id}, Husband: {family.husbandName}, Wife: {family.wifeName}")  # Update attribute names
    else:
        print("No living married couples found.")

    print("Test 17 passed successfully")  
    return living_married


# us18 Siblings spacing

def us18(individuals, families):
    siblings_spacing_errors = []

    for family in families:
        children_ids = family.childrenId  # Adjust to use the 'childrenId' attribute

        if len(children_ids) > 1:
            for i in range(len(children_ids)):
                for j in range(i + 1, len(children_ids)):
                    child1 = next((ind for ind in individuals if ind.id == children_ids[i]), None)
                    child2 = next((ind for ind in individuals if ind.id == children_ids[j]), None)

                    if child1 is not None and child2 is not None:
                        birth_date1 = datetime.strptime(child1.birthday, "%Y-%m-%d")
                        birth_date2 = datetime.strptime(child2.birthday, "%Y-%m-%d")
                        if abs((birth_date1 - birth_date2).days) < 270:
                            siblings_spacing_errors.append(f"FAMILY: US18: Siblings have less than 270 days spacing: {child1.name} and {child2.name}")

    if siblings_spacing_errors:
        for error in siblings_spacing_errors:
            print(error)
        return False

    print('Test 18 passed successfully')
    return True
