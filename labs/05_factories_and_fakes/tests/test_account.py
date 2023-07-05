"""
Test Cases TestAccountModel
"""
import json
from random import randrange
from unittest import TestCase
from models import db
from models.account import Account, DataValidationError
from factories import AccountFactory

ACCOUNT_DATA = {}

class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        db.create_all()  # make our sqlalchemy tables
        global ACCOUNT_DATA
        with open('tests/fixtures/account_data.json') as json_data:
            ACCOUNT_DATA = json.load(json_data)

    @classmethod
    def tearDownClass(cls):
        """Disconnext from database"""
        db.session.close()

    def setUp(self):
        """Truncate the tables"""
        self.rand = randrange(0, len(ACCOUNT_DATA))
        db.session.query(Account).delete()
        db.session.commit()

    def tearDown(self):
        """Remove the session"""
        db.session.remove()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_all_accounts(self):
        """ Test creating multiple Accounts """
        for data in ACCOUNT_DATA:
            # account = Account(**data)
            account = AccountFactory()
            account.create()
        self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))

    def test_create_an_account(self):
        """ Test Account creation using known data """
        # data = ACCOUNT_DATA[self.rand] # get a random account
        # account = Account(**data)
        account = AccountFactory()
        account.create()
        self.assertEqual(len(Account.all()), 1)

    def test_update_an_account(self):
        """Test updating an account"""
        NEW_NAME = "Juana la cubana"
        #data = ACCOUNT_DATA[self.rand]
        # account = Account(**data)
        account = AccountFactory()
        account = account.create()
        account.name = NEW_NAME
        account.update()
        self.assertEqual(account.find(account.id).name, NEW_NAME)

    def test_update_an_account_with_empty_id(self):
        """Test updating an account with empty id"""
        # account = Account(**ACCOUNT_DATA[self.rand])
        account = AccountFactory()
        account.id = None
        # assertRaises(the raised exception, the function, the params the function needs)
        self.assertRaises(DataValidationError, account.update)

    def test_delete_an_account(self):
        """Test deleting an account"""
        # account1 = Account(**ACCOUNT_DATA[0])
        account1 = AccountFactory()
        account1.create()
        # account2 = Account(**ACCOUNT_DATA[1])
        account2 = AccountFactory()
        account2.create()
        self.assertEqual(2, len(Account.all()))
        account1.delete()
        self.assertEqual(1, len(Account.all()))
        account2.delete()
        self.assertEqual(0, len(Account.all()))

    def test_repr_as_string(self):
        "Test representing an account as a string"
        account = Account(name="Foo")
        self.assertEqual(str(account), "<Account 'Foo'>")

    def test_to_dict(self):
        """Test to dict"""
        # data = ACCOUNT_DATA[self.rand]
        # account = Account(**data)
        account = AccountFactory()
        result = account.to_dict()
        self.assertIsInstance(result, dict)
        self.assertEqual(result["name"], account.name)
        self.assertEqual(result["email"], account.email)
        self.assertEqual(result["phone_number"], account.phone_number)
        self.assertEqual(result["disabled"], account.disabled)

    def test_from_dict(self):
        """Test from dict"""
        data = ACCOUNT_DATA[self.rand]
        account = Account()
        account.from_dict(data)
        self.assertEqual(data["name"], account.name)
        self.assertEqual(data["email"], account.email)
        self.assertEqual(data["phone_number"], account.phone_number)
        self.assertEqual(data["disabled"], account.disabled)

