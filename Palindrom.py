'''Program sprawdza, czy wpisane słowa są palindromem'''


haslo = input('Wpisz hasło, które chcesz sprawdzić: ')

kontrol = haslo.lower().replace(' ', '')
odwrotne_haslo = kontrol[::-1]

print(f'Twoje hasło: {haslo}')
print(f'Odwrócone hasło: {odwrotne_haslo}')
if kontrol == odwrotne_haslo:
    print(f'Hasło {haslo} JEST palindromem')
else:
    print(f'Hasło {haslo} NIE JEST palindromem')

