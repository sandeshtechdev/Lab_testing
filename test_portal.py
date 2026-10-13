import pytest
import portal
import portal_broken

LOGIN_CASES = [
    ("SP24-BSE-056", "demo123", "Login successful"),
    ("SP24-BSE-056", "wrong", "Invalid credentials"),
    ("SP24-BSE-056", "", "Password required"),
    ("SP24-BSE-999", "demo123", "Invalid credentials"),
]

FEE_CASES = [
    (50000, "Paid", 0),
    (20000, "Partially paid", 30000),
    (0, "Invalid amount", 50000),
    (60000, "Overpayment rejected", 50000),
]

@pytest.mark.parametrize("roll,pwd,expected", LOGIN_CASES)
def test_login_correct(roll, pwd, expected):
    assert portal.login(roll, pwd) == expected

@pytest.mark.parametrize("roll,pwd,expected", LOGIN_CASES)
def test_login_broken(roll, pwd, expected):
    assert portal_broken.login(roll, pwd) == expected

@pytest.mark.parametrize("amount,expected_msg,expected_balance", FEE_CASES)
def test_pay_fee_correct(amount, expected_msg, expected_balance):
    msg, bal = portal.pay_fee(amount)
    assert msg == expected_msg
    assert bal == expected_balance

@pytest.mark.parametrize("amount,expected_msg,expected_balance", FEE_CASES)
def test_pay_fee_broken(amount, expected_msg, expected_balance):
    msg, bal = portal_broken.pay_fee(amount)
    assert msg == expected_msg
    assert bal == expected_balance