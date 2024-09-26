"""
Uvažuj program, který čte knížku ze seznamu na základě indexu.
Ošetři s použitím výjimky možnou chybu, že program skončí chybou.
"""
try:
    knihy = ["Problém tří těles", "Temný les", "Vzpomínka na Zemi"]
    index = int(input("Zadej index knihy: "))
    print(knihy[index])
except IndexError:
    print("Taková kniha v seznamu není.")
