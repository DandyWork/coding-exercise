import pytest
from palindrome import is_palindrome #calling palindrome.py
from bank import BankAccount   #calling bank.py


# --------------------
# Tests for Palindrome Checker
# --------------------

def test_palindrome_true():
    assert is_palindrome("madam") == True #dibalik jadi madam, True 

def test_palindrome_false():
    assert is_palindrome("hello") == False #dibalik jadi olleh, False

def test_palindrome_single_letter():
    assert is_palindrome("a") == True #dibalik jadi a, True

def test_palindrome_empty_string():
    assert is_palindrome("") == True #kosong dibalik jadi kosong, True (?)


# --------------------
# Tests for BankAccount
# --------------------

def test_deposit_increases_balance():

    account = BankAccount() #declare dulu objectnya
    account.deposit(100) #deposit 100
    assert account.get_balance() == 100 #cek balance harusnya 100

def test_withdraw_decreases_balance():

    account = BankAccount()
    account.deposit(200) #deposit 200
    account.withdraw(50) #tarik 50
    assert account.get_balance() == 150 #pas cek balance harusnya 150

def test_withdraw_cannot_go_negative():
    
    account = BankAccount()
    account.deposit(50) #deposit 50
    account.withdraw(100) #tarik 100, biar negatif
    assert account.get_balance() == 50 #pas cek balance tetep 50, krn gak bisa narik > balance

def test_multiple_operations():

    account = BankAccount()
    account.deposit(100) #deposit 100
    account.withdraw(30) #tarik 30
    account.deposit(50) #deposit 50
    assert account.get_balance() == 120 #100-30+50 = 120, pas balance di cek harusnya 120
