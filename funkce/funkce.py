# NASOBENI

# Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.
def mult(a, b):
    return a * b

# FUNKCE PRO PREVODY JEDNOTEK

# Převod kilometrů na míle a zpět
# Napište dvě funkce: kilometry_na_mile(kilometry) a mily_na_kilometry(mile), které provedou převod mezi kilometry a mílemi.
def kilometry_na_mile(kilometry):
    return kilometry * 0.621371
def mile_na_kilometry(mile):
    return mile / 0.621371

# Převod metrů na stopy a zpět
# Napište funkce: metry_na_stopy(metry) a stopy_na_metry(stopy), které umožňují převod mezi metry a stopami.
def metry_na_stopy(metry):
    return metry * 3.28084
def stopy_na_metry(stopy):
    return stopy / 3.28084

# Převod centimetrů na palce a zpět
# Vytvořte dvě funkce: centimetry_na_palec(centimetry) a palce_na_centimetry(palce), které umožní převod mezi centimetry a palci.
def centimetry_na_palec(centimetry):
    return centimetry * 0.393701
def palce_na_centimetry(palce):
    return palce / 0.393701

# Převod hmotnosti kilogramů na libry a zpět
# Napište funkce: kilogramy_na_libry(kilogramy) a libry_na_kilogramy(libry), které provedou převod mezi kilogramy a librami.
def kilogramy_na_libry(kilogramy):
    return kilogramy * 2.20462
def libry_na_kilogramy(libry):
    return libry / 2.20462

# Převod objemu litrů na galony a zpět
# Vytvořte dvě funkce: litry_na_galony(litry) a galony_na_litry(galony), které umožní převod mezi litry a galony.
def litry_na_galony(litry):
    return litry * 0.264172
def galony_na_litry(galony):
    return galony / 0.264172

# Převod rychlosti kilometrů za hodinu na míle za hodinu a zpět
# Napište funkce: kmh_na_mph(kmh) a mph_na_kmh(mph), které umožní převod rychlosti mezi kilometry za hodinu a míli za hodinu.
def kmh_na_mph(kmh):
    return kmh * 0.621371
def mph_na_kmh(mph):
    return mph / 0.621371

# Převod teploty ze stupňů Celsia na Fahrenheit a zpět
# Vytvořte dvě funkce: celsia_na_fahrenheit(teplota) a fahrenheit_na_celsia(teplota), které umožňují převod teploty mezi stupni Celsia a stupni Fahrenheit.
def celsia_na_fahrenheit(teplota):
    return teplota * 1.8 + 32
def fahrenheit_na_celsia(teplota):
    return (teplota - 32) / 1.8


# RAMECEK

# Napiš funkci, která jako parametr převezme řetězec a vytiskne jej obalen hvězdičkami.
#
# Zadej slovo: ahoj
# ********
# * ahoj *
# ********
#
# Nápověda: 8 * '*' == '********'

def ramecek(text):
    print(8 * "*")
    print("*", text, "*")
    print(8 * "*")
ramecek("cau")
# Bonus: Znak, kterým se má text obalit, bude zadán také jako parametr.

def ramecek_se_znakem(text, znak):
    print(8 * znak)
    print(znak, text, znak)
    print(8 * znak)

ramecek_se_znakem("toodles", "#")

# MESIC NAROZENI
# Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo.
# Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup.
# Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.
#
#     Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.

def month_of_birth(rc):
    mesic = int(rc[2:4])
    if mesic > 50:
        mesic -= 50
    return mesic
print(month_of_birth("9207054439"))
print(month_of_birth("9555125899"))


# HOTEL
# Napiš funkci total_price, která vypočte cenu noci v hotelu. Funkce bude mít dva parametry - persons a breakfast.
# Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. Funkce vrátí výslednou cenu.
# Parametr breakfast je nepovinný a výchozí hodnota je False.
# Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True).

def total_price(persons, breakfast=False):
    cena = 850 * persons
    if breakfast:
        cena += 125 * persons
    return cena
print(total_price(3))
print(total_price(2, True))
