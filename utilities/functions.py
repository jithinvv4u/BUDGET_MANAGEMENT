
from hashids import Hashids
from configparser import RawConfigParser
from django.conf import settings
config= RawConfigParser(allow_no_value=True)


def encode(value):
    """
    Function to hash encode an integer value.

    Input Params:
        value(int): int value
    Returns:
        hashed string.
    """
    hasher = Hashids(
        min_length=settings.HASHID_MIN_LENGTH,
        salt=settings.HASHID_SALT,
        alphabet=settings.HASHID_ALPHABETS,
    )
    try:
        value = int(value)
        return hasher.encode(value)
    except Exception as e:
        raise ValueError(_("Invalid input {value} for Encoder. Should be of type int").format(value=value))


def decode(value):
    """
    Function to hash decode an encoded value to int.

    Input Params:
        value(str): str value
    Returns:
        int value.
    """
    hasher = Hashids(
        min_length=settings.HASHID_MIN_LENGTH,
        salt=settings.HASHID_SALT,
        alphabet=settings.HASHID_ALPHABETS,
    )
    try:
        return hasher.decode(value)[0]
    except Exception as e:
        raise ValueError(_("Invalid input({value}) for Decoder.").format(value=value))

