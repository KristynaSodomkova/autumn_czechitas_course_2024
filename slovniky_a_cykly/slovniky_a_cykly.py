"""
VYSVEDCENI 2
Uvažujme vysvědčení, které máme zapsané jako slovník.

    Napiš program, který spočte průměrnou známku ze všech předmětů.
    Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.
"""
import math

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

prumerna_znamka = sum(school_report.values()) / len(school_report)
print(prumerna_znamka)
for predmet, znamka in school_report.items():
    if znamka == 1:
        print(predmet)

"""
CTENARSKY DENIK
Gustav je vášnivým čtenářem detektivek z našeho nakladatelství a navíc si zapisuje knihy, které přečetl. 
Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.

    Napiš program, který spočte celkový počet stran, které Gustav přečetl.
    Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.
"""
books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

# celkovy_pocet_stran = sum([book["pages"] for book in books])
celkovy_pocet_stran = 0
for book in books:
    celkovy_pocet_stran += book["pages"]
print(celkovy_pocet_stran)
# pocet_oblibenych_knih = len([book for book in books if book["rating"] >= 8])
pocet_oblibenych_knih = 0
for book in books:
    if book["rating"] >= 8:
        pocet_oblibenych_knih += 1
print(pocet_oblibenych_knih)

"""
POZNAVACI ZNACKY
V následujícím slovníků je evidence automobilů. 
Klíčem jsou státní poznávací značky (SPZ) a hodnotou je jméno majitele vozu. 
Napiš program, který vypíše všechny majitele, jejichž vozidlo je registrováno v Plzeňském kraji, 
tj. na druhém místě (index 1!) řetězce v klíči je písmeno P.
"""
plates = {"4A2 3000": "František Novák",
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár",
    "1P5 5269": "Marta Nováková",
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král"}

for plate in plates:
    if plate[1] == "P":
        print(plates[plate])

"""
RECEPTY
Pohlédněte na následující reprezentaci receptu:
"""
recept = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}
"""
Uložte si tuto strukturu do proměnné recept na začátek nového programu. 
Vypište pomocí funkce print kolik bude celé jídlo stát korun zaokrouhlené na celé koruny nahoru.
"""
celkova_cena = 0
# for ingredience in recept["ingredience"]:
#     cena = float(ingredience[2].split(" ")[0])
#     celkova_cena += cena
for ingredince in recept["ingredience"]:
    cena_s_kc = ingredince[2]
    cena_bez_kc = cena_s_kc.split(" ")[0]
    cena_jako_cislo = float(cena_bez_kc)
    celkova_cena += cena_jako_cislo
print(math.ceil(celkova_cena))
# print(celkova_cena)