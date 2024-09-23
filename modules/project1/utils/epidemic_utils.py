# epidemic_utils.py

def incidence_rate(new_cases, total_population):
    """
    Calculates the incidence rate per 1000 people.
    
    :param new_cases: Number of new cases.
    :param total_population: Total population.
    :return: Incidence rate.
    """
    if total_population <= 0:
        raise ValueError("The total population must be greater than zero.")
    return (new_cases / total_population) * 1000


def mortality_rate(deaths, total_cases):
    """
    Calculates the mortality rate per 1000 people.
    
    :param deaths: Number of deaths.
    :param total_cases: Total number of cases.
    :return: Mortality rate.
    """
    if total_cases <= 0:
        raise ValueError("The total number of cases must be greater than zero.")
    return (deaths / total_cases) * 1000
