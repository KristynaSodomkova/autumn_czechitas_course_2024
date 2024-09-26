"""
Nasimulujme si fungování bankovní aplikace, konkrétně žádost o převod peněz z účtu.
Na začátku si vytvoř program balance.txt a do něj vlož nějaké číslo. Toto číslo reprezentuje aktuální zůstatek na účtu.

Přečti hodnotu v souboru, převeď ji na číslo a ulož ji do proměnné account_balance.
Čtení souboru i převod na číslo ošetři pomocí výjimek. Následně se zeptej uživatele (uživatelky), kolik peněz chce převést na jiný účet.
Ošetři pomocí výjimky, že uživatel (uživatelka) zadal(a) číslo.
Dále vyvolej ValueError v případě, že zadaná částka je záporná nebo vyšší než zústatek na účtu.
Pokud je vše v pořádku, spočítej nový zůstatek a zapiš ho do souboru balance.txt.
"""

with open("balance.txt", mode="w", encoding="utf-8") as output_file:
    print("1000", file=output_file)

with open("balance.txt", mode="r", encoding="utf-8") as input_file:
    try:
        account_balance = int(input_file.read())
    except ValueError:
        print("Soubor neobsahuje číslo.")

transfer = 0
try:
    transfer = int(input("Kolik chcete převést? "))
    if transfer < 0:
        raise ValueError("Zápornou částku nelze převést.")
    if transfer > account_balance:
        raise ValueError("Nemáte dostatek peněz na účtu.")
    print(f"Zůstatek na účtu: {account_balance - transfer}")
except ValueError:
    print("Je treba zadat kladné číslo menší než zůstatek na účtu.")

with open("balance.txt", mode="w", encoding="utf-8") as output_file:
    print(account_balance - transfer, file=output_file)
