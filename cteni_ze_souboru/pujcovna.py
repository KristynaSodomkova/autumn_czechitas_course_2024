"""
Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů.
V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok.
Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

Pozor! V souboru s daty je ještě jeden problém, který není na první pohled vidět!

Napište program, který na výstup vypíše součet všech ujetých kilometrů. Jistě se vám bude hodit metoda řetězců jménem replace().
"""

lines = []

with open("auta.txt", encoding="utf-8") as file:
    for line in file:
        parts = line.split(" ")
        num = parts[1]
        # num.replace(",", ".")
        clean_num = num.strip().replace(",", ".")
        lines.append(float(clean_num))

print(sum(lines))
