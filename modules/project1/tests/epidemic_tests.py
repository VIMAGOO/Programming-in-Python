# epidemic_tests.py
import pytest
from utils.epidemic_utils import incidence_rate, mortality_rate

def incidence_rate_test():
    assert incidence_rate(30, 20000) == 1.5
    assert incidence_rate(0, 10000) == 0.0
    with pytest.raises(ValueError):
        incidence_rate(10, 0)

def mortality_rate_test():
    assert mortality_rate(5, 100) == 50.0
    assert mortality_rate(0, 1000) == 0.0
    with pytest.raises(ValueError):
        mortality_rate(1, 0)

# Run tests if this file is executed directly
if __name__ == '__main__':
    pytest.main()

