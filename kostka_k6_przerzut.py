'''Program rzuca kością 6-ścienną
i przerzuca przy wyniku 6'''


import random

kostka = random.randrange(1, 7)

print(f'Wyrzuciłeś wynik {kostka}.')

while kostka == 6:
    print('PRZERZUT!')
    kostka = random.randrange(1,7)
    print(f'Wyrzuciłeś wynik {kostka}.')

