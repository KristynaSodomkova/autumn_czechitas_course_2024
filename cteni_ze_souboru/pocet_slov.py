"""
Stáhněte si odevzdanou slohovou práci. Zadání bylo sepsat text o nejméně 150ti slovech pojednávající o našem hlavním městě, soubor je ulozen jeko praha.txt.
Napište program, který spočítá počet slov v tomto textu, abychom věděli, zda bylo zadání formálně splněno. Nechte se vést následujícím návodem.

    Nechte váš program otevřít soubor a načíst jednotlivé řádky do seznamu
    Každý řádek převeďte na seznam slov. Slovem se rozumí vše, co je odděleno mezerou nebo novým řádkem
    Vypište na výstup počty slov na každém řádku
    Vypište na výstup celkový počet všech slov v souboru

"""

lines = []

with open("praha.txt", encoding="utf-8") as file:
    for line in file:
        lines.append(line.split())

for line in lines:
    print(len(line))

print(sum(len(line) for line in lines))
all_words = 0
for line in lines:
    all_words += len(line)
print(all_words)