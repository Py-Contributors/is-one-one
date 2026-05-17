"""Sample methods loaded dynamically by is_one_one.py."""


def is_one_unicode_distance():
    """Calculates one from adjacent Unicode code points."""
    return ord("b") - ord("a") == 1


def is_one_using_binary():
    """Parses a binary string to validate one."""
    return int("1", 2) == 1
