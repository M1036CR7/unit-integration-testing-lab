import pytest
from bank_app import *

def test_transfer():
    b1, b2 = transfer(1000, 500, 300)
    assert b1 == 700
    assert b2 == 800

def test_transfer_then_interest():
    b1, b2 = transfer(2000, 1000, 500)
    interest = calculate_interest(b2, 10, 1)
    assert round(interest, 2) == 1650

def test_transfer_fail():
    with pytest.raises(ValueError):
        transfer(1000, 500, 2000)
