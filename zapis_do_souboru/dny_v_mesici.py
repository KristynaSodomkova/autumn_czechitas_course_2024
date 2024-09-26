"""
Napište program, který bude mít přímo v kódu zapsaný počet dní v jednotlivých měsících takto:

pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

Nechte váš program vypsat tento seznam do souboru s názvem kalendar.txt, každé číslo na jeden řádek.
"""

pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open("kalendar.txt", mode="w", encoding="utf-8") as output_file:
    for number in pocty_dni:
        print(number, file=output_file)
