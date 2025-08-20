import re


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def validate_integrity(input: int):
    '''function that takes an integer and returns a boolean
    indicating whether if it passes the DIC integrity check'''
    if input < 1:
        return False
    digits = break_into_digits(input)
    return (input / sum(digits) % 1) == 0


def break_into_digits(input: int) -> list[int]:
    digits: list[int] = []
    remainder: int = input
    while remainder > 0:
        digits.insert(0, remainder % 10)
        remainder = remainder // 10
    return digits


def bulk_filter(max_num: int):
    '''Implemented as a generator function, can be coalesced to list at call
    site if needed.'''
    for x in range(0, max_num + 1):
        if validate_integrity(x):
            yield x
