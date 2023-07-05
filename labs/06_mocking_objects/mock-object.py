from unittest.mock import Mock

m = Mock()

print(m.foo()) #raises no errors
print(m.foo.called) # returns true
print(m.bar.called) # returns false

# Add an attribute when creating
m = Mock(status_code=200)
print(m.statuts_code)

# Add an attribute after creating
m = Mock()
m.age = 67
print(m.age)

print("\nMock with template")
from requests import Response
m = Mock(spec=Response,
         status_code=404,
         content='{"error":"Not Found"')
try:
    m.foo() # now raises an exception since Response does not have foo method
except BaseException as e:
    print(e)
print(m.json())
print(m.status_code)
print(m.text)