from account import Account


def test_create_account():
    account = Account(10000)
    assert account is not None
def test_account_init_10000_won():
    account = Account(10000)
    ret = account._balance
    assert ret == 10000