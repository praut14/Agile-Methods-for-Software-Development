
import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime
# from tkinter.font import families


#Sprint 4 -Pramod Kumar Kanigiri
 # User Story 33: Consistency Check for Sibling Birth Order
def us33(individuals):
    individuals_with_multiple_marriages = []

    # Create a dictionary to track the number of marriages for each individual
    marriage_count = {}

    # Iterate through individuals to count marriages
    for person in individuals:
        if person.spouse:
            marriage_count.setdefault(person.id, 0)
            marriage_count[person.id] += len(person.spouse)

    # Identify individuals with multiple marriages
    for person_id, count in marriage_count.items():
        if count > 1:
            individuals_with_multiple_marriages.append(person_id)

    return individuals_with_multiple_marriages

# User Story 34: Validation of Age at Marriage
def us34(individuals, families):
    for family in families:
        # Check if marriage date is available
        if family.married != "NA":
            marriage_date = datetime.strptime(family.married, '%Y/%m/%d')

            # Check husband's age at marriage
            husband = next((ind for ind in individuals if ind.id == family.husbandId), None)
            if husband and husband.birthday != "":
                birth_date_husband = datetime.strptime(husband.birthday, '%Y/%m/%d')
                age_at_marriage_husband = marriage_date.year - birth_date_husband.year - ((marriage_date.month, marriage_date.day) < (birth_date_husband.month, birth_date_husband.day))
                if age_at_marriage_husband < 14:
                    print(f"Warning: Husband {husband.name} (ID: {husband.id}) had marriage at age {age_at_marriage_husband}")

            # Check wife's age at marriage
            wife = next((ind for ind in individuals if ind.id == family.wifeId), None)
            if wife and wife.birthday != "":
                birth_date_wife = datetime.strptime(wife.birthday, '%Y/%m/%d')
                age_at_marriage_wife = marriage_date.year - birth_date_wife.year - (
                        (marriage_date.month, marriage_date.day) < (birth_date_wife.month, birth_date_wife.day))
                if age_at_marriage_wife < 14:
                    print(f"Warning: Wife {wife.name} (ID: {wife.id}) had marriage at age {age_at_marriage_wife}")
    return True