from models.address import Address
import pytest

def test_create_address():
    address = Address(street="123 Main St", city="Anytown", postal_code=12345)
    assert address.street == "123 Main St"
    assert address.city == "Anytown"
    assert address.postal_code == 12345

def test_address_types():
    address = Address(street="123 Main St", city="Anytown", postal_code=12345)
    assert isinstance(address.street, str)
    assert isinstance(address.city, str)
    assert isinstance(address.postal_code, int)
