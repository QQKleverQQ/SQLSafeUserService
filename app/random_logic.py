import random

def combine_numbers(user_number: int):
    rand = random.randint(1, 10)
    total = user_number + rand
    if total > 10:
        raise ValueError("Sum exceeds limit 10")
    return total
