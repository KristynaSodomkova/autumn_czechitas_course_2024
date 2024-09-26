# POHYBY NA ÚČTU
# Mějme seznam pohybů na nějakém bankovním účtu:
pohyby = [1200, -250, -800, 540, 721, -613, -222]
#
#     Vypište v pořadí třetí pohyb z uvedeného seznamu.
print(pohyby[2])
#     Vypište všechny pohyby kromě prvních dvou.
print(pohyby[2:])
#     Vypište kolik je všech pohybů dohromady.
print(len(pohyby))
#     Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
print(max(pohyby))
print(min(pohyby))
#     Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.
print(sum(pohyby))

# PRUMER
# Mějme proměnnou s, ve které předpokládáme uložený nějaký seznam.
# Sestavte v výraz (vzoreček), který spočítá průměrnou hodnotu v takovém seznamu.
# Otestujte jej na seznamech různých délek.

s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
v = sum(s)/len(s)
print(v)

# ROZPETI
# Postupujte obdobně jako v úložce Průměr, ale tentokrát sestavte výraz pro výpočet rozpětí,
# tedy rozdílu mezi minimální a maximální hodnotou.

r = max(s)-min(s)
print(r)

# BONUSOVE UKOLY
# Sestavte výraz, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s.
# U seznamů liché délky je střed jasně definovaný, ovšem u seznamů sudé délky nám padne mezi dvě čísla.
# V takovém případě vyberte jako střed číslo blíže ke konci seznamu.

s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
prostredni_cislo = s[len(s) // 2]
print(prostredni_cislo)


# STRED SEZNAMU PODRUHE
# Sestavte vzoreček, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s.
# Tentokrát však u seznamů sudé délky vyberte jako střed číslo blíž k začátku seznamu.
s = [1, 2, 3, 4, 5, 6, 7, 8]

if len(s) % 2 == 0:
    prostredni_cislo = s[len(s) // 2 - 1]
    print(prostredni_cislo) # tato varianta se vutiskne pokud je pocet prvku v seznamu sudy
else:
    prostredni_cislo = s[len(s) // 2]
    print(prostredni_cislo) # tato varianta se vutiskne pokud je pocet prvku v seznamu lichy