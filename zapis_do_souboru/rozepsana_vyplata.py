"""
Modifikujte program pro počítání výplaty z předchozí sekce tak, aby nevypisoval průměrnou výplatu za rok,
nýbrž aby vypsal konkrétní vyplacenou částku pro každý měsíc zvlášť.

    Nejprve tyto informace vypište na terminál
    Poté program upravte tak, aby vypsal tyto výsledky do souboru

"""

lines = []

with open("vykaz.txt", encoding="utf-8") as file:
    for line in file:
        lines.append(int(line))

print(lines)

hourly_wage = int(input("Zadejte hodinovou mzdu: "))
for hours in lines:
    print(hours * hourly_wage)

with open("vyplata.txt", mode="w", encoding="utf-8") as output_file:
    for number in lines:
        wage = number * hourly_wage
        print(wage, file=output_file)
