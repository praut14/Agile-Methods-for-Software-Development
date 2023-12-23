import datetime
# Poorvi us01 Bad Smell UserStory Validation of Refractored code

# Bad Smell 1: Define a consistent date format
DATE_FORMAT = "%Y-%m-%d"

def validate_date(date_str):
    """
    Validate a date string.

    Args:
        date_str (str): A date string in the specified format.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    try:
        datetime.datetime.strptime(date_str, DATE_FORMAT)
        return True
    except ValueError:
        return False
#Bad Smell 2:  Validate dates (birth, marriage, divorce, death) should not be after the current date.
def us01(individuals, families, current_date=None):
    """

    Args:
        individuals (list): A list of individual objects.
        families (list): A list of family objects.
        current_date (str): The current date in the specified format.

    Returns:
        bool: True if all dates are valid, False otherwise.
    """
    if current_date is None:
        current_date = datetime.date.today().strftime(DATE_FORMAT)

    for individual in individuals:
        if individual.birthday != "NA" and not validate_date(individual.birthday):
            raise ValueError(f"Invalid birth date for Individual {individual.id}: {individual.birthday}")

        if individual.deathday != "NA" and not validate_date(individual.deathday):
            raise ValueError(f"Invalid death date for Individual {individual.id}: {individual.deathday}")

    for family in families:
        if family.married != "NA" and not validate_date(family.married):
            raise ValueError(f"Invalid marriage date for Family {family.id}: {family.married}")

        if family.divorced != "NA" and not validate_date(family.divorced):
            raise ValueError(f"Invalid divorce date for Family {family.id}: {family.divorced}")

    return True
print("Test to check Dates (birth, marriage, divorce, death) should not be after the current date")
    