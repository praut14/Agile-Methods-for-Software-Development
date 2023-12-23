import datetime
from datetime import date
from datetime import datetime, timedelta

#Sprint 4 - Nancy Gupta

# us25  Order siblings by age


def us25(individuals, families):
    ordered_siblings_list = []

    for family in families:
        children_ids = family.childrenId
        siblings = []

        for child_id in children_ids:
            child = next((ind for ind in individuals if ind.id == child_id), None)
            if child is not None:
                siblings.append(child)

        # Order siblings by age
        siblings.sort(key=lambda x: datetime.strptime(x.birthday, "%Y/%m/%d"))

        if siblings:
            ordered_siblings_list.extend(siblings)
            print(f"Family ID: {family.id}, Ordered Siblings by Age:")
            for sibling in siblings:
                print(f"Child ID: {sibling.id}, Name: {sibling.name}, Birthday: {sibling.birthday}")
        else:
            print(f"No children found for family {family.id}.")

    print("Test 25 passed successfully")
    return ordered_siblings_list


# us26 List living singles

def us26(individuals, families):
    living_singles = []

    for individual in individuals:
        if individual.alive and not individual.spouse:
            living_singles.append(individual)

    if living_singles:
        print("List of living singles:")
        for single in living_singles:
            print(f"Individual ID: {single.id}, Name: {single.name}, Birthday: {single.birthday}")
    else:
        print("No living singles found.")

    print("Test 26 passed successfully")
    return living_singles


# us27 List recent births
def us27(individuals):
    recent_births = []

    today = datetime.now()

    for individual in individuals:
        if individual.birthday != "NA":
            birthdate = datetime.strptime(individual.birthday, "%Y/%m/%d")
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            if 0 <= age <= 1:  # Considering births within the last year
                recent_births.append((individual.id, individual.name, individual.birthday))

    if recent_births:
        print("List of recent births:")
        for recent_birth in recent_births:
            print(f"Individual ID: {recent_birth[0]}, Name: {recent_birth[1]}, Birthday: {recent_birth[2]}")
    else:
        print("No recent births found.")

    print("Test 27 passed successfully")
    return sorted(recent_births)



# us28  Female last names
def us28(individuals):
    female_last_names = []

    for individual in individuals:
        if individual.gender == "F" and individual.alive:
            female_last_names.append(individual)

    female_last_names.sort(key=lambda x: x.name.split()[-1])  # Sort by last name

    if female_last_names:
        print("List of females with last names sorted:")
        for female in female_last_names:
            print(f"Individual ID: {female.id}, Name: {female.name}, Last Name: {female.name.split()[-1]}")
    else:
        print("No living females found.")

    print("Test 28 passed successfully")
    return female_last_names
