from datetime import datetime, timedelta
import pytest 
from src.data_structure import Account, Transaction

def test_register_and_limit_reduction():
    acct = Account(active = True, available_limit=500)
    txn = Transaction("Walmart", 120, datetime.now())

    acct.register(txn)

    assert acct.available_limit == 380
    assert acct.history[-1] == txn


def test_cannot_spend_over_limit():
    acct = Account(active=True, available_limit=100)
    txn = Transaction("Big‑Spend", 200, datetime.now())

    with pytest.raises(ValueError):
        acct.register(txn)


def test_inactive_account_fails():
    acct = Account(active=False, available_limit=999)
    txn = Transaction("Coffee", 5, datetime.now())

    with pytest.raises(ValueError):
        acct.register(txn)