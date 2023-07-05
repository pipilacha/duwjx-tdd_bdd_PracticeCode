"""
AccountFactory class using FactoryBoy

Documentation on Faker Providers:
    https://faker.readthedocs.io/en/master/providers/baseprovider.html

Documentation on Fuzzy Attributes:
    https://factoryboy.readthedocs.io/en/stable/fuzzy.html

"""
import factory
from datetime import datetime
from factory.fuzzy import FuzzyChoice, FuzzyDate
from models.account import Account

class AccountFactory(factory.Factory):
    """ Creates fake Accounts """

    #allows AccountFactory to call methods from the class
    class Meta:
        model = Account

    # Add attributes here...
    id = factory.Sequence(lambda n: n)
    name = factory.Faker("name")
    email = factory.Faker("email")
    phone_number = factory.Faker("phone_number")
    disabled = FuzzyChoice(choices=[True, False])
    #LazyFunction only generate the timestamp when the account is created
    date_joined = factory.LazyFunction(datetime.utcnow)  # do not execute the function, just name id, no ()
