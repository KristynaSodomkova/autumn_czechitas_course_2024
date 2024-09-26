# PREVOD PISMEN
# Uložte si do proměnné jmeno svoje jméno.
# Pomocí volání vhodných metod jej převeďte nejdříve na malá písmena a poté na velká písmena.

jmeno = "Kristyna Sodomkova"
print(jmeno.lower())
print(jmeno.upper())

#  CISLA JAKO TEXT
# Mějme seznam celých čísel zadaných jako text

hodnoty = ['12', '1', '7', '-11']

# Potřebujeme k třetímu číslu v seznamu přičíst 4, aby výsledek vypadal takto:

treti_hodnota = hodnoty[2]
treti_hodnota = int(treti_hodnota)
vysledek = treti_hodnota + 4
hodnoty[2] = vysledek
print(hodnoty)

# CISLA V TEXTU
# Máme obdobné zadání jako v předchozím cvičení, avšak tentokrát máme čísla zadána nikoliv v seznamu, ale v řetězci oddělená mezerou:

hodnoty = '12.1 1.68 7.45 -11.51'

# K poslednímu číslu v seznamu chceme přičíst 0.25 tak, aby výsledek vypadal takto
# hodnoty = '12.1 1.68 7.45 -11.26'
list_hodnoty = hodnoty.split(" ")
posledni_hodnota = list_hodnoty[-1]
posledni_hodnota = float(posledni_hodnota)
vysledek = posledni_hodnota + 0.25
print(vysledek)
vysledek = str(vysledek)
list_hodnoty[-1] = vysledek
vysledek_hodnoty = " ".join(list_hodnoty)
print(vysledek_hodnoty)
# Určitě se vám budou hodit metody split a join.

# CHYTREJSI CISLA JAKO TEXT
# Mějme seznam celých čísel zadaných jako text

hodnoty = ['12', '1', '7', '-11']

# Potřebujeme k třetímu číslu v seznamu přičíst 4, aby výsledek vypadal takto:

# hodnoty[2] = str(int('7') + 4)
# print(hodnoty)
print(['12', '1', str(int('7') + 4), '-11'])
# print(hodnoty[0] + hodnoty[1] + str(int(hodnoty[2]) + 4) + hodnoty[3])
print(hodnoty[0:2] + [(str(int(hodnoty[2]) + 4))] + hodnoty [-1:])