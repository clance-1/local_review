# python
import pytest
from password import generate_password

@pytest.mark.parametrize("length", [0, 1, 5, 10, 32])
def test_generate_password_length(length):
    pwd = generate_password(length)
    assert isinstance(pwd, str)
    assert len(pwd) == length

def test_generate_password_negative_raises():
    with pytest.raises(ValueError):
        generate_password(-1)