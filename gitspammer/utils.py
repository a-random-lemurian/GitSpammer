import random

LETTERS = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_letters(length: int):
    return ''.join(random.choices(LETTERS,k=length))