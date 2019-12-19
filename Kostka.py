'''Program do wykonania rzutu kością
o wybranej liczbie ścianek'''

import random

n = int(input('Ile ścianek ma kość? '))

kostka = random.randrange(1, n)

def wizualizacja(kostka:int):
    if kostka > 9:
        return print(f'-----------\n|         |\n|   {kostka}    |\n|         |\n-----------')
    else:
        return print(f'-----------\n|         |\n|    {kostka}    |\n|         |\n-----------')

wizualizacja(kostka)