import random
# ZAROVNANI VYPISU
# Vypište seznam čísel každé na nový řádek zarovnané vpravo na délku nejdelšího čísla.
#
numbers = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
#
# Návod:
#
#     Zjistěte kolik znaků zabírá nejdelší číslo ze seznamu
#     Napište funkci, která dostane řetězec a délku, na kterou má text vyplnit zleva mezerami

# nejdelsi = max(numbers)
numbers_as_str = []
for number in numbers:
    numbers_as_str.append(str(number))
# nejdelsi = len(max(numbers_as_str, key=len))
nejdelsi = 0
for number in numbers_as_str:
    if len(number) > nejdelsi:
        nejdelsi = len(number)
print(nejdelsi)
def zarovnani_vpravo(text, delka):
    print((delka - len(text)) * " ", text)

for number in numbers_as_str:
    zarovnani_vpravo(number, nejdelsi)

# Bonus: funkce bude mít volitelný parametr, jakým znakem má text vyplňovat
def zarovnani_vpravo_bonus(text, delka, znak="."):
    print((delka - len(text)) * znak, text)
for number in numbers:
    zarovnani_vpravo_bonus(str(number), nejdelsi, ".")
# Výstup:
#
#      7728
#        88
#    958621
#      5941
# 959847272
#      3944
#        80
#       521
#     57035
#   3967894
#
# Výstup bonusu:
#
# .....7728
# .......88
# ...958621
# .....5941
# 959847272
# .....3944
# .......80
# ......521
# ....57035
# ..3967894
#
# RULETA

# Napiš funkci, která bude jednoduchou simulací rulety.
# Budeme uvažovat pouze možnost sázení na řady. Uživatel si může vybrat jednu ze tří řad:
#
#     první řada (hodnoty 1, 4, 7 atd.),
#
#     druhá řada (hodnoty 2, 5, 8 atd.),
#
#     třetí řada (hodnoty 3, 6, 9 atd.).
#
#     Zeptej se uživatele, na kterou ze tří řad sází a na výši sázky.
#
#     Vytvoř funkci roulette, která bude mít parametry číslo řady a výši sázky.
#     Pomocí funkce randint z modulu random vygeneruj náhodné číslo v rozsahu od 0 (včetně) do 36.
#     Vyhodnoť, do které řady číslo náleží. Nezapomeň, že 0 nepatří do žádné z řad a pokud padne, uživatel vždy prohrává.
#
#     Funkce roulette vrací hodnotu výhry.
#     Pokud uživatel vsadil na správnou řadu, vyhrává dvojnásobek sázky,
#     v opačném případě nevyhrává nic jeho sázka propadá.
def roulette(rada, vyse_sazky):
    number = random.randint(0, 36)
    # print(f"number is {number}")
    # print(f"rada is {rada}")
    # print(f"vyse_sazky is {vyse_sazky}")
    if number == 0:
        return 0
    if number % 3 == rada:
        return vyse_sazky * 2
    return 0
print(roulette(1, 100))

# ZPREHAZENA PISMENA
# Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena.
# Stačí, když první a poslední písmeno je na své pozici zachováno.
# Napiš funkci, která bude mít jako vstupní parametr slovo a vrátí slovo,
# kde zpřehází všechny znaky kromě prvního a posledního.
#
# Nápověda: random.shuffle()

def zprehazena_pismena(slovo):
    if len(slovo) <= 2:
        return slovo
    first = slovo[0]
    last = slovo[-1]
    middle = list(slovo[1:-1])
    random.shuffle(middle)
    new_middle = "".join(middle)
    return "".join(first + new_middle + last)
print(zprehazena_pismena("czechitas"))

# Super bonus: Napiš program, který takovou funkci využije na delší text více slov.
#
text = '''Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena.
Stačí, když první a poslední písmeno je na své pozici zachováno. Napiš funkci,
která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny
znaky kromě prvního a posledního.
'''
import re
words = re.findall(r'\b\w+\b', text)
separators = re.findall(r'\W+', text) + ['']
shuffled_words = []
for word in words:
    shuffled_words.append(zprehazena_pismena(word))
new_text = ''.join([word + sep for word, sep in zip(shuffled_words, separators)])
print(new_text)
#
# Výstup:
#
# Slvoo je sátle mnžoé pdhlnooě pseířčt, když jsou pcnhíoamá psímnea.
# Stčaí, kydž pvrní a ponsldeí pmínseo je na své pozcii znaáhvoco. Nipaš fcnkui,
# kretá bude mít jkao vsntpuí paaremtr solvo a vátrí solvo, kde zhpezáří všhecny
# zanky krmoě pírhnvo a plísoednho.

# reseni od Jirky
text = '''Slovo je stále možné pohodlně \n přečíst, když jsou pomíchaná písmena.
Stačí, když první a poslední písmeno je na své pozici zachováno. Napiš funkci,
která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny
znaky kromě prvního a posledního.
'''

def zprehazej_slovo(slovo):
    if len(slovo) <= 2:
        return f" {slovo}"
    else:
        prostredni_cast = list(slovo[1:-1])
        random.shuffle(prostredni_cast)
        prostredni_cast = "".join(prostredni_cast)
        return f" {slovo[0]}{prostredni_cast}{slovo[-1]}"

vystup = ""
for slovo in text.split(" "):
    vystup = vystup + zprehazej_slovo(slovo)
print(vystup)

# NAPRAVY
def spocitel_pokutu(pocet_naprav, hmotnost):
    limit = 0
    if pocet_naprav == 2:
        limit = 18
    elif pocet_naprav == 3:
        limit = 25
    elif pocet_naprav == 4:
        limit = 32
    elif pocet_naprav == 5:
        limit = 48

    if hmotnost <= limit:
        return 0
    else:
        return (hmotnost - limit) * 1000


pokuta = spocitel_pokutu(4, 34)
print(pokuta)

vazeni = [
    [4, 33],
    [2, 19],
    [3, 29],
    [3, 27],
    [5, 53],
    [5, 51],
    [2, 20],
]
celkova_pokuta = 0
for vozidlo in vazeni:
    pokuta = spocitel_pokutu(vozidlo[0], vozidlo[1])
    celkova_pokuta = celkova_pokuta + pokuta
print(celkova_pokuta)
