from unittest.mock import Mock


"""
A plain old object
"""

def test_plain_object():
    fake_object_1 = FakeClass()
    fake_object_2 = Mock()
    

class FakeClass():
    pass



"""
An object with methods
"""
def test_object_with_methods():
    fake_object = FakeClassWithMethods()
    assert fake_object.greet() == "hello, world"

    fake_object_2 = Mock()
    fake_object_2.greet.return_value = "hello, world"
    assert fake_object_2.greet() == "hello, world"

class FakeClassWithMethods():
    def greet(self):
        return "hello, world"
    

"""
An object with methods that we can verify have been called
"""

def test_object_with_verified_methods():
    fake_object = FakeClassWithVerifiedMethods()
    assert fake_object.greet("Afzaa") == "Hello, Afzaa!"
    assert fake_object.greet_has_been_called == True


class FakeClassWithVerifiedMethods():
    def __init__(self):
        self.greet_has_been_called = False

    def greet(self, name):
        self.greet_has_been_called = True
        assert name == "Afzaa"
        return "Hello, Afzaa!"
    

def test_mock_with_verified_methods():
    fake_object = Mock()
    fake_object.greet.return_value = "Hello, Afzaa!"

    assert fake_object.greet("Afzaa") == "Hello, Afzaa!"
    fake_object.greet.assert_called()
    fake_object.greet.assert_called_with("Afzaa")


