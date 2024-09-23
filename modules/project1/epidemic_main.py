# epidemic_main.py

from utils.epidemic_utils import incidence_rate, mortality_rate

def main():
    # Exemple d'ús de les funcions
    population = 20000
    new_cases = 30
    deaths = 5
    total_cases = 100

    indcidence_rateA = incidence_rate(new_cases, population)
    mortality_rateB = mortality_rate(deaths, total_cases)

    print(f"Indicence rating: {indcidence_rateA} per 1000 habitants")
    print(f"Mortality rating: {mortality_rateB} per 1000 habitants")

if __name__ == "__main__":
    main()