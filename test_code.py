import pytest
from palindrome import is_palindrome #calling palindrome.py
from bank import BankAccount   #calling bank.py


# --------------------
# Tests for Palindrome Checker
# --------------------

def test_palindrome_true():
    # "madam" is the same forwards and backwards → should return True
    assert is_palindrome("madam") == True

def test_palindrome_false():
    # "hello" is not the same backwards ("olleh") → should return False
    assert is_palindrome("hello") == False

def test_palindrome_single_letter():
    # A single letter (like "a") is always a palindrome → should return True
    assert is_palindrome("a") == True

def test_palindrome_empty_string():
    # Empty string "" is often considered a palindrome → should return True
    assert is_palindrome("") == True


# --------------------
# Tests for BankAccount
# --------------------

def test_deposit_increases_balance():
    # Start with empty account
    account = BankAccount()
    # Deposit 100 → balance should now be 100
    account.deposit(100)
    assert account.get_balance() == 100

def test_withdraw_decreases_balance():
    # Deposit 200 first
    account = BankAccount()
    account.deposit(200)
    # Withdraw 50 → balance should be 150
    account.withdraw(50)
    assert account.get_balance() == 150

def test_withdraw_cannot_go_negative():
    # Deposit only 50
    account = BankAccount()
    account.deposit(50)
    # Try to withdraw 100 → should not be allowed, balance stays 50
    account.withdraw(100)
    assert account.get_balance() == 50

def test_multiple_operations():
    # Start empty account
    account = BankAccount()
    # Deposit 100 → balance 100
    account.deposit(100)
    # Withdraw 30 → balance 70
    account.withdraw(30)
    # Deposit 50 → balance 120
    account.deposit(50)
    assert account.get_balance() == 120
