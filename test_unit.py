import pytest
from bank_app import *

def test_deposit():
    assert deposit(1000, 500) == 1500
    with pytest.raises(ValueError):
        deposit(1000, -1)

def test_withdraw():
    assert withdraw(1000, 500) == 500
    with pytest.raises(ValueError):
        withdraw(1000, 2000)

def test_interest():
    assert calculate_interest(1000, 10, 1) == 1100
    with pytest.raises(ValueError):
        calculate_interest(-1, 5, 1)

def test_loan():
    assert check_loan_eligibility(6000, 750) is True
    assert check_loan_eligibility(2000, 600) is False
