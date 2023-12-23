import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime
# from tkinter.font import families


#Sprint 3 - Kanigiri Pramod

# User Story 23:  List of individuals with multipule marrages
def us23(families):
    marriage_count = {}  # Dictionary to store marriage count for each individual

    # Count the number of marriages for each individual
    for family in families:
        husband_id = family.husbandId
        wife_id = family.wifeId

        if husband_id in marriage_count:
            marriage_count[husband_id] += 1
        else:
            marriage_count[husband_id] = 1

        if wife_id in marriage_count:
            marriage_count[wife_id] += 1
        else:
            marriage_count[wife_id] = 1

    # Find individuals with multiple marriages
    individuals_with_multiple_marriages = [individual for individual, count in marriage_count.items() if count > 1]

    return individuals_with_multiple_marriages

# User Story 24:  List of individuals with no children
def us24(individuals, families):
    individuals_with_children = set()

    # Collect all individuals who are listed as parents in families
    for family in families:
        children = family.childrenId
        individuals_with_children.update(children)

    # Find individuals who are not listed as parents (have no children)
    individuals_with_no_children = [individual for individual in individuals if individual.id not in individuals_with_children]

    return individuals_with_no_children