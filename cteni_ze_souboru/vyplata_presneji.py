"""
Zatím jsme výplatu počítali za předpokladu, že každý měsíc odpracujeme stejný počet hodin, což není příliš realistické. Stáhněte si textový soubor vykaz.txt,
 který obsahuje 12 řádků a na každém řádku počet odpracovaných hodin za každý měsíc za poslední rok.

    Otevřete tento soubor ve svém programu a načtěte hodnoty na řádcích do seznamu vykaz.
    Vytiskněte tento seznam do terminálu funkcí print() abyste si ověřili, že jste soubor načetli správně.
    Nechte uživatele zadat na příkazovém řádku hodinovou mzdu. Spočítejte a na výstup vytiskněte celkovou výplatu za celý rok a průměrnou výplatu na jeden měsíc.

"""
lines = []

with open("vykaz.txt", encoding="utf-8") as file:
    for line in file:
        lines.append(int(line))

print(lines)

hourly_wage = int(input("Zadejte hodinovou mzdu: "))
total_wage = sum(lines) * hourly_wage
average_wage = total_wage / 12

print(f"Celková výplata za rok: {total_wage}")
print(f"Průměrná výplata za měsíc: {average_wage}")

