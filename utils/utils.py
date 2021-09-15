import random
import string


def create_random_string(length=10):
    return "".join(
        [random.choice(string.ascii_letters + string.digits) for i in range(length)]
    )


def count_letters(text):
    return sum(c.isalpha() for c in text)


def count_digits(text):
    return sum(c.isdigit() for c in text)
