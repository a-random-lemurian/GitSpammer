import random

LETTERS = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_letters():
    return ''.join(random.choices(LETTERS,k=12))