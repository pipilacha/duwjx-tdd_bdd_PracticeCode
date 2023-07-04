"""
Test Cases TestAccountModel
"""
import json
from unittest import TestCase
from models import db
from models import app
from models.account import Account, DataValidationError
from random import randrange

ACCOUNT_DATA = {}

class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """ Connect and load data needed by tests """
        db.create_all()

        global ACCOUNT_DATA

        with open('tests/fixtures/account_data.json') as json_data:
            ACCOUNT_DATA = json.load(json_data)

    @classmethod
    def tearDownClass(cls):
        """Disconnect from database"""
        with app.app_context():
            db.session.close()

    def setUp(self):
        """Truncate the tables"""
        db.session.query(Account).delete()

    def tearDown(self):
        """Remove the session"""
        db.session.remove()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_account(self):
        """Test creating an account"""
        account = Account(**ACCOUNT_DATA[randrange(len(ACCOUNT_DATA))])
        account.create()
        self.assertEqual(len(account.all()), 1)

    def test_create_all_accounts(self):
        """Test creating all accounts"""
        for data in ACCOUNT_DATA:
            account = Account(**data)
            account.create()
        self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))

    def test_update_an_account(self):
        """Test updating an account"""
        NEW_NAME = "Juana la cubana"
        data = ACCOUNT_DATA[randrange(len(ACCOUNT_DATA))]
        account = Account(**data)
        account = account.create()
        account.name = NEW_NAME
        account.update()
        self.assertEqual(account.find(account.id).name, NEW_NAME)

    def test_update_an_account_with_empty_id(self):
        """Test updating an account with empty id"""
        account = Account(**ACCOUNT_DATA[randrange(len(ACCOUNT_DATA))])
        # assertRaises(the raised exception, the function, the params the function needs)
        self.assertRaises(DataValidationError, account.update)

    def test_delete_an_account(self):
        """Test deleting an account"""
        account1 = Account(**ACCOUNT_DATA[0])
        account1.create()
        account2 = Account(**ACCOUNT_DATA[1])
        account2.create()
        self.assertEqual(2, len(Account.all()))
        account1.delete()
        self.assertEqual(1, len(Account.all()))
        account2.delete()
        self.assertEqual(0, len(Account.all()))

