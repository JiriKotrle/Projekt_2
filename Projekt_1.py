# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Jiří Kotrle
# email: jirikotrle@gmail.com
# discord: jirikotrle

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

user_password = {'bob':'123', 'ann':'pass123', 'mike':'password123', 'liz':'pass123'}
oddelovac = '- '*40

jmeno = str(input('zadej jmeno: '.upper()))
heslo = str(input('zadej heslo: '.upper()))

print(f'Jméno: {jmeno}')
print(f'Heslo: {heslo}')
print(oddelovac)

pozadovane_heslo = user_password.get(jmeno) # lepší je použít metodu .get(), která mi v případě, že jméno není v množine nevrátí chybu Keyerror (narozdíl od user_password[jmeno])

if jmeno in user_password and heslo == pozadovane_heslo:
    print(f'Vítám tě {jmeno}, můžeš analyzovat jeden ze 3 textů!')
else:
    print('Heslo nebo jméno bylo zadáno špatně. Ukončuji program!')
    quit()

print(oddelovac)

cislo_textu = input('Vyber si text 1,2 nebo 3: ')

if  cislo_textu.isdigit() == False:
    print('Zadaná hodnota není číslo. Ukončuji program!')
    quit()
elif (int(cislo_textu) - 1) < 1 and (int(cislo_textu) - 1) > 2:
    print('Vybrané číslo textu je mimo požadovaný rozsah! Ukončuji program!')
else:
    vybrany_text = TEXTS[int(cislo_textu) - 1]

print(oddelovac)

upraveny_text_znaky = vybrany_text.split() # metoda split() rozdělí řetězec na jednotlivá slova a uloží je do seznamu, slova ale obsahují i znaky (,;? atd.)
upraveny_text = []
for slovo in upraveny_text_znaky:
    nove_slovo = ''.join([znak for znak in slovo if znak.isalnum()]) #odstranění znaků (isalnum() kontroluje, jestli je znak alfanumerický)
    upraveny_text.append(nove_slovo)

pocet_slov1 = len(upraveny_text)
print(f'Celkový počet slov je: {pocet_slov1}')

# zjistí počet slov začínajících velkým písmenem:
pocet_slov2 = sum([1 for slovo in upraveny_text if slovo.istitle() == True])
print(f'Počet slov začínajících velkým písmenem je: {pocet_slov2}')

#zjistí počet slov psaných velkými písmeny:
pocet_slov3 = sum([1 for slovo in upraveny_text if slovo.isupper() == True and slovo.isalpha() == True])
print(f'Počet slov psaných velkými písmeny je: {pocet_slov3}')

#zjistí počet slov psaných malými písmeny:
pocet_slov4 = sum([1 for slovo in upraveny_text if slovo.islower() == True])
print(f'Počet slov psaných malými písmeny je: {pocet_slov4}')

#zjistí počet čísel (ne cifer):
pocet_slov5 = sum([1 for slovo in upraveny_text if slovo.isdigit() == True])
print(f'Počet čísel: {pocet_slov5}')

#zjistí sumu všech čísel (ne cifer):
suma = sum([int(slovo) for slovo in upraveny_text if slovo.isdigit() == True])
print(f'Suma všech čísel: {suma}')

print(oddelovac)

#graf četnosti délek textu:
cetnosti = {}
delka_slov = [len(slovo) for slovo in upraveny_text]
delka_slov_max = int(max(delka_slov))

for cislo in delka_slov:
    if cislo in cetnosti:
        cetnosti[cislo] = cetnosti[cislo] + 1
    else:
        cetnosti[cislo] = 1

print('LEN|','OCCURENCES'.center(10),'|NR.')
print(oddelovac)

for cislo in sorted(cetnosti.keys()):
    cetnost = cetnosti.get(cislo)
    print(f"{cislo:3}|{'*'*cetnost:12}|{cetnost}")
