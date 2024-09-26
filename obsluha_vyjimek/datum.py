"""
Požádej uživatele o zadání data narození ve formátu RRRR-MM-DD.

Nejprve ověř pomocí podmínek, že je zadáno správné datum
- tj. v datu jsou dvě pomlčky a po rozdělení na jednotlivé části obsahuje každá z částí číslo.
Stále je ale možné, že je zadáno nesmyslné datum.
Například je možné zadat datum 31. dubna nebo 29. února pro nepřestupný rok.
Proto přidej modul datetime a pomocí metody fromisoformat() vyzkoušej převod na typ datetime.
Ošetři ValueError, která může být způsobena výše uvedenými případy.
"""

from datetime import datetime


# varianta 1:
# try:
#     datum_narozeni = input("Zadej datum ve formátu RRRR-MM-DD: ")
#     datum_narozeni = datetime.fromisoformat(datum_narozeni)
# except ValueError:
#     print("Zadal jsi nesmyslné datum.")


# varianta 2:
# datum_narozeni = input("Zadej datum ve formátu RRRR-MM-DD: ")
# if len(datum_narozeni) != 10 or datum_narozeni[4] != "-" or datum_narozeni[7] != "-":
#     print("Zadal jsi datum ve špatném formátu.")
#     exit()
# if not datum_narozeni[:4].isnumeric() or not datum_narozeni[5:7].isnumeric() or not datum_narozeni[8:].isnumeric():
#     print("Zadal jsi datum ve špatném formátu.")
#     exit()
# try:
#     datum_narozeni = datetime.fromisoformat(datum_narozeni)
# except ValueError:
#     print("Zadal jsi nesmyslné datum.")


# varianta 3:
# datum_narozeni = input("Zadej datum ve formátu RRRR-MM-DD: ")
# if len(datum_narozeni) != 10 or datum_narozeni[4] != "-" or datum_narozeni[7] != "-":
#     print("Zadal jsi datum ve špatném formátu.")
#     exit()
# try:
#     int(datum_narozeni[:4])
#     int(datum_narozeni[5:7])
#     int(datum_narozeni[8:])
# except ValueError:
#     print("Zadal jsi datum ve špatném formátu.")
#     exit()
# try:
#     datum_narozeni = datetime.fromisoformat(datum_narozeni)
# except ValueError:
#     print("Zadal jsi nesmyslné datum.")


# varianta 4:
def convert_date(date_string):
    try:
        return datetime.fromisoformat(date_string)
    except ValueError:
        print("Zadal jsi nesmyslné datum.")


convert_date(input("Zadej datum ve formátu RRRR-MM-DD: "))

