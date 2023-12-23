import datetime
from datetime import date
from datetime import datetime, timedelta

#Sprint 4 - Riya Divakaran

def us31(individuals, families):
    """
    User Story 31: List all living people over 30 who have never been married in a GEDCOM file

    :param individuals: List of individual objects
    :param families: List of family objects
    :return: List of unmarried individuals over 30 who are alive
    """
    unmarried_over_30 = []

    for individual in individuals:
        if individual.alive and individual.age > 30 and not individual.spouse:
            unmarried_over_30.append(individual)

    if unmarried_over_30:
        print("US31: Unmarried individuals over 30 who are alive:")
        for person in unmarried_over_30:
            print(f"  - {person.id}: {person.name} (Age: {person.age})")
        return unmarried_over_30
    else:
        print("US31: No unmarried individuals over 30 who are alive found.")
        return []

def us32(families):
    error_messages = []
    marriage_dates = set()

    # Check for valid and unique marriage anniversaries
    for family in families:
        if family.married:
            try:
                marriage_date = datetime.strptime(family.married, "%Y/%m/%d").date()
                if marriage_date in marriage_dates:
                    error_messages.append(f"ERROR: US32: Duplicate marriage anniversary found in Family {family.id}.")
                else:
                    marriage_dates.add(marriage_date)
            except ValueError:
                error_messages.append(f"ERROR: US32: Invalid marriage date format in Family {family.id}.")

    # Check for missing marriage events
    for family in families:
        if not family.married:
            error_messages.append(f"ERROR: US32: Missing marriage event in Family {family.id}.")

    if error_messages:
        for message in error_messages:
            print(message)
        return False
    else:
        print("US32: Marriage anniversaries verified.")
        return True


