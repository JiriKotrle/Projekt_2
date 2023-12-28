# projekt_2.py: druhý projekt do Engeto Online Python Akademie
# author: Jiří Kotrle
# email: jirikotrle@gmail.com
# discord: jirikotrle

import random
import time
oddelovac = '-'*40
print(oddelovac)
print('Ahoj, vítám tě u hry Bulls & Cows!')
print(oddelovac)
print('''Vytvořil jsem náhodné 4 místné číslo,
kde je každá z číslic unikátní a 
zároveň toto číslo neobsahuje 0.
Tvým úkolem je toto číslo uhodnout!''')
print(oddelovac)

#Vytvoření náhodného čísla
while True:
    number = str(random.randint(1000, 9999))   
    # Zkontrolujte, zda číslo nezačíná nulou:
    if number[0] == '0':
        continue
        # Zkontrolujte, zda jsou všechny číslice unikátní:
    if len(set(number)) == 4:
        break

print(number)
    
cas_zacatek = time.time() # Zaznamenání počátečního času
opak = 0 # počet pokusů uhodnout
while True:
    cislo = input('Hádej jaké číslo jsem vytvořil:')
    opak = opak + 1 # počet pokusů uhodnout
    print(oddelovac)

    if (len(cislo) != 4 or len(set(cislo)) != 4 
    or int(cislo[0]) == 0 or cislo.isdigit() != True):
        print('Číslo je špatně zadané!')
        continue

    bull_s = 0
    cow_s = 0
    upr_number = str(number) # převedu číslo na string abych ním mohl iterovat
    for i in range(0,4): # rozsah pro 4 čísla
        if str(cislo)[i] == str(number)[i]: # kontrola stejných pozic čísel
            bull_s += 1
            upr_number = upr_number.replace(str(number)[i],'') # tam kde je shoda, odstraním danou číslici
            cow_s = sum([1 for x in cislo if x in upr_number])
        else:
            cow_s = sum(1 for x in cislo if x in upr_number)

    if bull_s == 1:
         print(f'Bull: {bull_s}')
    else:
         print(f'Bulls: {bull_s}')

    if cow_s == 1:
         print(f'Cow: {cow_s}')
    else:
         print(f'Cows: {cow_s}')
    
    print(oddelovac)

    if bull_s == 4 and cow_s == 0 and opak < 3:
        cas_konec = time.time()
        cas_uhadnuti = cas_konec - cas_zacatek
        print(f'Ano, {cislo} je správné číslo! Počet pokusů: {opak}')
        print(oddelovac) 
        print(f'Výborný výsledek! Celkový čas hádání: {cas_uhadnuti:.2f} sec.')
        break
    if bull_s == 4 and cow_s == 0 and opak >= 3 and opak < 8:
        cas_konec = time.time()
        cas_uhadnuti = cas_konec - cas_zacatek 
        print(f'Ano, {cislo} je správné číslo! Počet pokusů: {opak}')
        print(oddelovac) 
        print(f'Dobrý výsledek! Celkový čas hádání: {cas_uhadnuti:.2f} sec.')
        break
    if bull_s == 4 and cow_s == 0 and opak >= 8:
        cas_konec = time.time()
        cas_uhadnuti = cas_konec - cas_zacatek 
        print(f'Ano, {cislo} je správné číslo! Počet pokusů: {opak}')
        print(oddelovac) 
        print(f'Nic moc výsledek - zkus to znovu! Celkový čas hádání: {cas_uhadnuti:.2f} sec.')
        break


